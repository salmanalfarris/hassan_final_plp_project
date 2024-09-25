from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('add/', views.add_edit_product, name='add_product'),
    path('edit/<int:pk>/', views.add_edit_product, name='edit_product'),
]