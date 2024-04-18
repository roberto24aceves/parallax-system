from django.contrib import admin
from .models import Post
from .models import Category
from .models import Tag
from .models import Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','date_posted')
    list_filter = ('date_posted',)
    search_fields = ('title', 'content')
    ordering = ('date_posted',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author','text','created_date','approved_comment')
    list_filter = ('created_date','approved_comment','post')
    search_fields = ('post', 'author', 'text',)
    ordering = ('created_date',)
