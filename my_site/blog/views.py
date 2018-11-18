from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/view_post.html'

    # def get_slug_field(self):
    #     return slug_field

def create_post(request):
    return render(request, 'blog/create_post.html')


#
# def index(request):
#     latest_post_list = Post.objects.order_by('-pub_date')[:4]
#     context = {'latest_post_list': latest_post_list}
#     return render(request, 'blog/index.html', context)
#
# def view_post(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/view_post.html', {'post': post})
