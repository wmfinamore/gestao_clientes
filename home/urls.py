from django.urls import path
from .views import home, logout_user
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', home, name="home"),
    path('logout/', logout_user, name="logout"),
    path('home2/', TemplateView.as_view(template_name='home2.html'), name="home2"),

]