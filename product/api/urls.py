from django.urls import path, include
from . import views

app_name = 'Product'

urlpatterns = [
    path('list/active-products/',  views.ListActiveProductsView.as_view() , name = 'active-products'),
    path('list/all-products/',  views.ListAllProductsView.as_view() , name = 'all-products'),
    path('create-product/' , views.CreateProductView.as_view() , name = "create"),
    path('detail-product/<int:pk>/' , views.DetailProductView.as_view() , name = "detail"),
]