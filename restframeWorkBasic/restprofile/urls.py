from  .import views
from django.conf.urls import url

urlpatterns = [
	url('list/', views.ListAuthor.as_view(), name='list'),
]