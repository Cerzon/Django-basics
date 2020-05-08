import os
import json
from django.shortcuts import render
from django.conf import settings
# from django.views.generic import ListView, DetailView

# Create your views here.

# class IndexView(ListView):
#     template_name = 'mainapp/index.html'

def index(request):
    context = {
        'page_title': 'Главная',
        'header_quote': 'В нашей обширной стране обыкновенный автомобиль, предназначенный, по мысли пешеходов, для мирной перевозки людей и грузов, принял грозные очертания братоубийственного снаряда.',
        'content_header': 'Команда профессионалов',
    }
    with open(os.path.join(settings.BASE_DIR, 'mainapp', 'data', 'staff.json'), 'r', encoding='utf-8') as data_file:
        try:
            staff = json.load(data_file)['staff']
        except json.JSONDecodeError:
            staff = None
    if staff:
        context['object_list'] = staff
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'page_title': 'Каталог',
        'header_quote': 'Финансовая пропасть – самая глубокая из всех пропастей, в нее можно падать всю жизнь.',
        'content_header': 'Каталог товаров',
    }
    with open(os.path.join(settings.BASE_DIR, 'mainapp', 'data', 'products.json'), 'r', encoding='utf-8') as data_file:
        try:
            goods = json.load(data_file)['products']
        except json.JSONDecodeError:
            goods = None
    if goods:
        context['object_list'] = goods
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {
        'page_title': 'Контакты',
        'header_quote': 'Параллельно большому миру, в котором живут большие люди и большие вещи, существует маленький мир с маленькими людьми и маленькими вещами. В большом мире людьми двигает стремление облагодетельствовать человечество. Маленький мир далёк от таких высоких материй. У его обитателей стремление одно — как-нибудь прожить, не испытывая чувства голода.',
        'content_header': 'Наши контакты',
    }
    return render(request, 'mainapp/contacts.html', context)