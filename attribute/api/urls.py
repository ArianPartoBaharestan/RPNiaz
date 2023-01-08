from django.urls import path
from attribute.api import views

urlpatterns = [
    path('AttributeGroup/', views.AttributeGroupView.as_view()),
    path('Attribute/', views.AttributeView.as_view()),
    path('AttributeItem/', views.AttributeItemView.as_view()),
    path('ProductAttribute/', views.ProductAttributeView.as_view()),
]