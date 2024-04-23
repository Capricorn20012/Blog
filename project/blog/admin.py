from django.contrib import admin
from .models import Category, Article, Comment, Profile

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'views', 'created_at']
    list_display_links = ['id', 'title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'article', 'created_at']



admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

