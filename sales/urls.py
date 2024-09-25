from django.urls import path
from . import views
from .views import login_view


urlpatterns = [
    path('', views.sales_list, name='sales_list'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('sales_list/', views.sales_list, name='sales_list'),
    path('login/', login_view, name='login'),
]