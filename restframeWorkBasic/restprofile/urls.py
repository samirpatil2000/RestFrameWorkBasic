from  .import views
from django.urls import path,include

urlpatterns = [
	path('list/', views.ListAuthor.as_view(), name='list'),
	path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
	path('edit/<int:id>/', views.PostUpdateAPIView.as_view(), name='edit'),

]