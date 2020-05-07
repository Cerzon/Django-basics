from django.shortcuts import render
# from django.views.generic import ListView, DetailView

# Create your views here.

# class IndexView(ListView):
#     template_name = 'mainapp/index.html'

def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')