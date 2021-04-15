from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse # Resposta Http
from django.template import loader
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é massa',
        'products': products
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, pk):
    # prod = Product.objects.get(id=pk)
    prod = get_object_or_404(Product, id=pk)
    context = {
        'product': prod
    }
    return render(request, 'product.html', context)


def error404(request, exception):
    template = loader.get_template('error404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('error500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
