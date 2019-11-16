from django.contrib import admin
from .models import Repository, AboutContent


class AboutContentAdmin(admin.ModelAdmin):
    fields = ('body',)

admin.site.register(Repository)
admin.site.register(AboutContent, AboutContentAdmin)
