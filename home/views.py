from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.views.generic.base import View


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


class MyView(View):
    def get(self, request, *args, **kwargs):
        response = render_to_response('home/home3.html')
        response.set_cookie('cor', 'blue', max_age=1000)
        mycookie = request.COOKIES.get('cor')
        print(mycookie)
        return response
        # return HttpResponse('Hello World!')
        # return render(request, 'home/home3.html')
