from django.shortcuts import render
from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)

def create_post(request):
    return render(request, 'blog/create_post.html')

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/view_post.html', {'post': post})
