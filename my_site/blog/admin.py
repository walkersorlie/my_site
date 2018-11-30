from django.contrib import admin

from .models import User, Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title']}

admin.site.register(User)
admin.site.register(Post, PostAdmin)
