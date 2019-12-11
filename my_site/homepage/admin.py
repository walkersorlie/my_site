import os
import requests
import json as json_py
from django.contrib import admin
from .models import Repository, AboutContent


class RepositoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'pushed_at'
    list_display = ('__str__', 'pushed_at',)
    exclude = ('github_repo_id',)
    readonly_fields = ('url', 'pushed_at',)


    """
    No Add button
    """
    def has_add_permission(self, request):
        return False

    """
    No Delete button
    """
    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):

        url = 'https://api.github.com/graphql'

        id = obj.github_repo_id

        desc = obj.description
        obj.description = desc

        name = obj.repo_name.replace(' ', '-')
        obj.repo_name = name

        repo_url = obj.url[:(obj.url.rindex('/'))+1] + name
        obj.url = repo_url

        mutation = """
            mutation UpdateRepository {
                updateRepository(input: {repositoryId:\"%s\", description:\"%s\", name:\"%s\", homepageUrl:\"%s\"}) {
                    repository {
                        id
                        description
                    }
                }
            }
        """ % (id, desc, name, repo_url)

        api_token = os.environ['MY_SITE_GITHUB_ACCESS_TOKEN']
        headers = {'User-Agent': 'Mozilla/5.0', 'Authorization': 'token %s' % api_token}
        r = requests.post(url=url, json={'query': mutation}, headers=headers)

        super().save_model(request, obj, form, change)


class AboutContentAdmin(admin.ModelAdmin):
    # fields = ('body',)
    empty_value_display = 'Not yet created'
    readonly_fields = ('last_edited',)


admin.site.register(Repository, RepositoryAdmin)
admin.site.register(AboutContent, AboutContentAdmin)
