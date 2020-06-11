from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse

from .serializers import (
	 addSerializer,
	listSerializer,
	# listCategorySerializer,
	# showSerializer,
	)

from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response


from mypost.models import Category,Post


from rest_framework.permissions import (
	IsAuthenticated,
	)


from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication

class PostListAPIView(ListAPIView):
	serializer_class = listSerializer
	queryset = Post.objects.all()



class AddPost(CreateAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = addSerializer
	queryset = Post.objects.all()

	def perform_create(self, serializer):
		serializer.save(author = self.request.user.id)
