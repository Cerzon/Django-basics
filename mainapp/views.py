import os
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from authapp.models import HoHooUser
from quotesapp.models import UserQuote
from .models import Category, Product
# from django.views.generic import ListView, DetailView

# Create your views here.

# class IndexView(ListView):
#     template_name = 'mainapp/index.html'

def index(request):
    context = {
        'page_title': 'Главная',
        'content_header': 'Команда профессионалов',
    }
    context['header_quote'] = UserQuote.objects.filter(header=True).order_by('?')[0]
    staff = HoHooUser.objects.filter(public=True)
    if staff:
        context['object_list'] = staff
    return render(request, 'mainapp/index.html', context)


def products(request, category=None):
    context = {
        'page_title': 'Каталог',
        'content_header': 'Каталог товаров',
    }
    context['header_quote'] = UserQuote.objects.filter(header=True).order_by('?')[0]
    context['category_list'] = Category.objects.all()
    goods = Product.objects.all().select_related()
    if category:
        goods = goods.filter(category__slug=category)
    if goods:
        context['object_list'] = goods
    return render(request, 'mainapp/products.html', context)


def product_detail(request, category, product):
    try:
        obj = Product.objects.get(slug=product, category__slug=category)
    except Product.DoesNotExist:
        return HttpResponseRedirect(reverse('mainapp:catalog:index'))
    context = {
        'content_header': 'Страница товара'
    }
    context['header_quote'] = UserQuote.objects.filter(header=True).order_by('?')[0]
    context['page_title'] = 'Товар - {}'.format(obj.name)
    context['object'] = obj
    return render(request, 'mainapp/product_detail.html', context)


def contacts(request):
    context = {
        'page_title': 'Контакты',
        'content_header': 'Наши контакты',
    }
    context['header_quote'] = UserQuote.objects.filter(header=True).order_by('?')[0]
    return render(request, 'mainapp/contacts.html', context)