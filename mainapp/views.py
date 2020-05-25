""" mainapp views
"""
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authapp.models import HoHooUser
from .models import Category, Product
# from django.views.generic import ListView, DetailView

# Create your views here.

# class IndexView(ListView):
#     template_name = 'mainapp/index.html'

def index(request):
    """ main page view
    """
    context = {
        'page_title': 'Главная',
        'content_header': 'Команда профессионалов',
    }
    staff = HoHooUser.objects.filter(public=True)
    if staff:
        context['object_list'] = staff
    return render(request, 'mainapp/index.html', context)


def products(request, category=None):
    """ product catalog view
    """
    context = {
        'page_title': 'Каталог',
        'content_header': 'Каталог товаров',
    }
    context['category_list'] = Category.objects.all()
    goods = Product.objects.all().select_related()
    if category:
        goods = goods.filter(category__slug=category)
    if goods:
        context['object_list'] = goods
        context['popular'] = goods.annotate(
            num=Count('slots')).order_by('num')[:4]
    return render(request, 'mainapp/products.html', context)


def product_detail(request, category, product):
    """ product details view
    """
    try:
        obj = Product.objects.get(slug=product, category__slug=category)
    except Product.DoesNotExist:
        return HttpResponseRedirect(reverse('mainapp:catalog:index'))
    context = {
        'content_header': 'Страница товара'
    }
    context['page_title'] = 'Товар - {}'.format(obj.name)
    context['object'] = obj
    context['recomend'] = Product.objects.filter(
        category=obj.category).exclude(pk=obj.pk).order_by('?')[:4]
    return render(request, 'mainapp/product_detail.html', context)


def contacts(request):
    """ contacts page view
    """
    context = {
        'page_title': 'Контакты',
        'content_header': 'Наши контакты',
    }
    return render(request, 'mainapp/contacts.html', context)
