from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "signup.html")


def contact(request):
    return render(request, "contact.html")



def products(request):
    return render(request, 'products.html')