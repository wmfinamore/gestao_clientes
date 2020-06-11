"""gestao_clientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from produtos import urls as produtos_urls
from vendas import urls as vendas_urls
from clientes import urls as clientes_urls
from home import urls as home_urls
from gestao_clientes import settings

urlpatterns = [
    path('', include(home_urls)),
    path('clientes/', include(clientes_urls)),
    path('produtos/', include(produtos_urls)),
    path('vendas/', include(vendas_urls)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/',include(debug_toolbar.urls)),
    ] + urlpatterns


admin.site.site_header = 'Gestão de Clientes'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Seja bem vindo ao Gestão de Clientes'