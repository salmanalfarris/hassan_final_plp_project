from django.shortcuts import render

# Create your views here.
from .models import Product
from .forms import ProductForm

def index(request):
     return render(request, 'inventory/index.html')

def inventory_list(request):
    products = Product.objects.all()
    return render(request, 'inventory_list.html', {'inventory_items': products})

def add_edit_product(request, pk=None):
    if pk:
        product = get_object_or_404(Product, pk=pk)
    else:
        product = None
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory_form.html', {'form': form})
