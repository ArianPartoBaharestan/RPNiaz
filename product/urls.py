from django.urls import path, include
from . import views

app_name = 'Product'

urlpatterns = [
    path('list-products/',  views.ListProductsView.as_view() , name = 'list'),
    path('create-product/' , views.CreateProductView.as_view() , name = "create"),
    path('detail-product/<int:pk>/' , views.DetailProductView.as_view() , name = "detail"),
    path('image/' , views.ListImageView.as_view())
]