from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, UpdateView, CreateView
from quotesapp.models import UserQuote
from .models import HoHooUser
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm

# Create your views here.

@login_required
def index(request):
    context = {'page_title': 'Профиль пользователя ' + request.user.username}
    context['content_header'] = context['page_title']
    context['header_quote'] = UserQuote.objects.filter(header=True).order_by('?')[0]
    return render(request, 'authapp/user_detail.html', context)


class UserLoginView(FormView):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('authapp:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Авторизация'
        context['content_header'] = 'Вход для зарегистрированных пользователей'
        context['header_quote'] = UserQuote.objects.filter(header=True).order_by('?')[0]
        return context

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super().form_valid(form)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


class UserProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'authapp/user_update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('authapp:index')
    model = HoHooUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Редактирование данных пользователя ' + self.request.user.username
        context['content_header'] = context['page_title']
        context['header_quote'] = UserQuote.objects.filter(header=True).order_by('?')[0]
        return context


class UserRegisterView(CreateView):
    template_name = 'authapp/signup.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('authapp:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Регистрация'
        context['content_header'] = 'Регистрация нового пользователя'
        context['header_quote'] = UserQuote.objects.filter(header=True).order_by('?')[0]
        return context

    def get_success_url(self):
        user = authenticate(
            username=self.request.POST.get('username'),
            password=self.request.POST.get('password1')
        )
        login(self.request, user)
        return super().get_success_url()