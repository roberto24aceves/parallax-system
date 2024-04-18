from rest_framework.serializers import ModelSerializer
from .models import *

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'slug', 'title', 'content', 'date_posted', 'category', 'tags']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'slug', 'name']

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_date', 'approved_comment']
