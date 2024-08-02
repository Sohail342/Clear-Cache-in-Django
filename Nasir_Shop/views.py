from django.shortcuts import get_object_or_404, render
from .models import Product
from .models import Category

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products":products})


def contact(request):
    return render(request, "contact.html")



def products_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})


def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'each_product.html', {'product':product})

def categories(request):
    categories = Category.objects.all()
    return render(request, "category.html", {'categories': categories})

def catogory(request, name):
    category = get_object_or_404(Category, name=name)
    products = Product.objects.filter(category=category)
    return render(request, "each_category.html", {'category': category, 'products': products})