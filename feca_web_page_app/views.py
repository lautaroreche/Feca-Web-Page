from django.shortcuts import render
from feca_web_page_app.models import Product


def home(request):
    products = Product.objects.all()
    print(len(products))
    categories = Product.objects.values_list('category', flat=True).distinct()

    context = {
        "products": products,
        "categories": categories,

    }
    return render(request, 'index.html', context)
