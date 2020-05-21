from django.urls import path
from .views import home, logout_user, HomePageView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', home, name="home"),
    path('logout/', logout_user, name="logout"),
    path('home2/', TemplateView.as_view(template_name='home/home2.html')),
    path('home3/', HomePageView.as_view()),

]