from django.urls import path

from .import views

urlpatterns = [
    # path('',views.index,name='index'),
    # path('register/', views.register, name='register'),
     path('create/', views.add,name='add'),
     path('list/',views.all_posts,name='list'),
     # path('(?P<pk>\d+)$/',views.show_post,name='post-detail')
     path('<int:pk>/',views.show_post,name='post-show'),

]