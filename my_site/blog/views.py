from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, NoReverseMatch
from django.views import generic
from django.db import IntegrityError
import datetime

from .models import User, Post
from .forms import PostForm


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/view_post.html'
    context_object_name = 'specific_blog'

    # Should match the value after ':' from url <slug:the_slug>
    slug_url_kwarg = 'slug'

    # Should match the name of the slug field on the model
    slug = 'slug'

    # def get(self, request, *args, **kwargs):
    #     slug = kwargs.get('slug')
    #     slug_id = ... # code here to determine id of slug's category
    #     self.queryset = Post.objects.filter(category=slug_id)[:5]
    #     return super(BlogPostView, self).get(request, *args, **kwargs)

    # def get_slug_field(self):
    #     return slug_field

# What to do if slug isntoo unique?
# Ex: Creating a post and there is an error, the post is still added to DB. Debugging errors still add entry to DB, but don't redirect to the detail page
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = User(request.user.id)
            post.author = request.user
            post.pub_date = datetime.datetime.now()

            try:
                # post.save()

                # return HttpResponseRedirect('view_post', slug=post.slug)
                return HttpResponseRedirect(reverse('view-post', kwargs={"slug": post.slug}))
            # except (NoReverseMatch) as e:
            #     pass
            except (IntegrityError) as e:
                print ("prob")
                print (type(e))
                # maybe add an error message to template here to tell error
                return render(request, 'blog/create_post.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


#
# def index(request):
#     latest_post_list = Post.objects.order_by('-pub_date')[:4]
#     context = {'latest_post_list': latest_post_list}
#     return render(request, 'blog/index.html', context)
#
# def view_post(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/view_post.html', {'post': post})
