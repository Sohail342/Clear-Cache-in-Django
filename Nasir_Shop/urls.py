from django.urls import path
from Nasir_Shop import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path("products/", views.products_list, name="products"),
    path("product/<int:id>/", views.product, name="each_product"),
    path('categories/', views.categories, name="categories"),
    path('category/<str:name>/', views.catogory, name="each_category")
]