from django.contrib import admin

from .models import User, Post

admin.site.register(User)
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['id/title']}
