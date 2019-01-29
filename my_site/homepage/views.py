from django.views import generic
from .models import Repository


class IndexView(generic.ListView):
    template_name = 'homepage/index.html'
    context_object_name = 'repo_list'

    def get_queryset(self):
        return Repository.objects.order_by('-pushed_at')
