from django.shortcuts import render, redirect
from django.template import engines
from django.shortcuts import render


# Create your views here.

from .models import Order

def sales_list(request):
    sales = Order.objects.all()
    return render(request, 'sales.html', {'sales': sales})
    return render(request, 'sales/sales_list.html')

def analytics_view(request):
    # Your logic here
    return render(request, 'analytics.html')

def add_edit_product(request, product_id=None):
    if request.method == 'POST':
        return redirect('inventory_list')
    return render(request, 'add_edit_product.html', {'product': product})

def login_view(request):
    template_engine = engines['django']
    print(template_engine.template_loaders[0].get_template_names('registration/login.html'))
    return render(request, 'registration/login.html')
