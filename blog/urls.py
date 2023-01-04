from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    path('list/active/' ,  views.ListActiveBlogView.as_view() , name = 'list-active') ,
    path('list/destroy/' , views.ListDestroyBlogView.as_view()) ,
    path('list/waiting/' , views.ListWaitingBlogView.as_view()) ,
    path('create/' , views.CreateBlogView.as_view()) ,
    path('detail/<str:slug>/' , views.RetriveUpdateDestroyBlogView.as_view())


]
