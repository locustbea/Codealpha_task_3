"""
URL configuration for Restaurant_Management_System project.

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

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu_items/', views.menu_items, name='menu_items'),
    path('menu_items/create/', views.create_menu_item, name='create_menu_item'),
    path('orders/', views.orders, name='orders'),
    path('orders/create/', views.create_order, name='create_order'),
    path('tables/', views.tables, name='tables'),
    path('tables/create/', views.create_table, name='create_table'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/create/', views.create_inventory_item, name='create_inventory_item'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
]
