from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    Get the ID/username of the current user, and use that here???
    '_auth_user_id' might be the variable name
    readonly_fields = ('author_id',)
    """
    exclude = ('pub_date', 'slug',)
    # prepopulated_fields = { 'slug': ['title']}

admin.site.register(Post, PostAdmin)
