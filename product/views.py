from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products_list = Product.objects.filter(availabel=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product_list = Product.objects.filter(category=category)

    return render(request, 'list.html', {'products' : product_list,
                                         'category': category,
                                         'categories': categories})
