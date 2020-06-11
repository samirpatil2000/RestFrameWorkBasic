from rest_framework import serializers
from mypost.models import Post


from rest_framework.serializers import (
	ModelSerializer,
)



class listSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'category',
			'title',
			'text',
		]


class addSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'category',
			'title',
			'text',
		]