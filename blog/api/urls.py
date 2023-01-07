from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    path('list/active/' ,  views.ListActiveBlogView.as_view() , name = 'list-active') ,
    path('list/waiting/' , views.ListWaitingBlogView.as_view()) ,
    path('detail/<str:slug>/' , views.RetriveUpdateDestroyBlogView.as_view()) ,
    path('<int:pk>/comments/' , views.ListCommentView.as_view()) ,
    path('comments/create/' , views.CreateCommentView.as_view())

]
