from .import views
from django.urls import path,include

urlpatterns = [
	path('list/', views.PostListAPIView.as_view(), name='restpost-list'),
	path('add/', views.AddPost.as_view(), name='restpost-add'),
	path('<int:id>/', views.ShowPost.as_view(), name='restpost-show'),
	path('category/list/', views.CategoryAllAPIView.as_view(), name='restpost-list-caregory'),
	path('list_category/<int:id>/', views.CategoryIdAPIView.as_view(), name='restpost-category-id'),

]