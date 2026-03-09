"""
URL configuration for inventory_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.landing_view),
    path("home/", views.home_view ,  name = 'home'),
    path("login/", views.login_view , name = 'login'),
    path("logout/", views.logout_view , name = 'logout'),
    path("reg/", views.register_view),
    path("landing/", views.landing_view, name = 'landing'),
    path("prod/", views.prod_view, name = 'prod'),
    path("add/", views.add_view, name = 'add'),
    path("del/<int:id>", views.delete_view, name = 'del'),
    path("update/<int:id>", views.update_view, name = 'update'),
    path("sup/", views.supplier_view, name = 'sup'),
    path("add_sup/", views.add_supplier, name = 'add_sup'),
    path("del_sup/<int:id>", views.del_supplier, name = 'del_sup'),
    path("update_sup/<int:id>", views.update_supplier, name = 'update_sup'),
]
