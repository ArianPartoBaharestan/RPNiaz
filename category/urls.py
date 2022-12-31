from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryView.as_view()),
    path('brand', views.BrandView.as_view()),
]