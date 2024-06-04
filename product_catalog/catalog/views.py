from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    
    if selected_category:
        products = Product.objects.filter(category__id=selected_category)
        context = {
            'categories': categories,
            'products': products,
            'selected_category': selected_category,
        }
    else:
        context = {
            'categories': categories,
        }
    
    return render(request, 'catalog/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})
