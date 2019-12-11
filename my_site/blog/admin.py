from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    Get the ID/username of the current user, and use that here???
    '_auth_user_id' might be the variable name
    https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_fields
    """

    date_hierarchy = 'pub_date'
    list_display = ('title', 'upper_case_name', 'pub_date')
    fields = ('upper_case_name', 'title', 'body')
    readonly_fields = ('upper_case_name',)
    # prepopulated_fields = { 'slug': ['title']}

    def upper_case_name(self, obj):
        return ("%s" % (obj.author_id.username)).capitalize()
    upper_case_name.short_description = 'Author'


admin.site.register(Post, PostAdmin)
