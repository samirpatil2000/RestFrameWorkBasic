from .import views
from django.urls import path,include

urlpatterns = [
	path('list/', views.PostListAPIView.as_view(), name='restpost-list'),
	path('add/', views.AddPost.as_view(), name='restpost-add'),

]