from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView


def home(request):
    return render(request, 'home/home.html')


def logout_user(request):
    logout(request)
    return redirect('home')


class HomePageView(TemplateView):
    template_name = 'home/home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel']='Olá, seja bem vindo ao curso de Django advanced'
        return context
