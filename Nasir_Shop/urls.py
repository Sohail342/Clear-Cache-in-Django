from django.urls import path
from Nasir_Shop import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path("products/", views.products, name="products")
]