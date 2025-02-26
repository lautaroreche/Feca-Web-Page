from django.shortcuts import render
from feca_web_page_app.models import Product


def home(request):
    products = Product.objects.all().order_by('name')
    categories = Product.objects.values_list('category', flat=True).distinct().order_by('category')
    context = {
        "products": products,
        "categories": categories,

    }
    return render(request, 'index.html', context)
