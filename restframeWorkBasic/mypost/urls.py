from django.urls import path

from .import views

urlpatterns = [
    # path('',views.index,name='index'),
    # path('register/', views.register, name='register'),
     path('create/', views.add,name='add'),
     path('list/', views.Users_all_posts, name='list'),
     # path('(?P<pk>\d+)$/',views.show_post,name='post-detail')
     path('<int:pk>/',views.show_post,name='post-show'),

     path('category/<int:pk>/', views.list_category, name='category'),
     path('userlist/', views.Users_all_posts, name='list'),
     path('update/<int:pk>/', views.update_post, name='update'),
     path('delete/<int:pk>/', views.delete_post, name='delete'),

]