from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy, reverse, NoReverseMatch
from django.views import generic
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
import datetime

from .models import Post
from .forms import PostForm


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 4


    def get_queryset(self):
        # return Post.objects.order_by('-pub_date')[:5]
        # return Post.objects.order_by('-pub_date')
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        three_recent_posts = self.get_queryset()[:3]
        context['three_recent_posts'] = three_recent_posts


        # get 4--->rest of posts
        post_exam = self.get_queryset()[3:]
        if not post_exam:
            return context
        else:
            paginator = Paginator(post_exam, self.paginate_by)
            page = self.request.GET.get('page')

            # limit = 4 * page
            # offset = limit - 4
            # post_list = post_exam[offset:limit]  # limiting posts based on current_page
            # total_posts = Posts.objects.all().count()
            # total_pages = total_posts / 4

            try:
                post_exams = paginator.page(page)
            except PageNotAnInteger:
                post_exams = paginator.page(1)
            except EmptyPage:
                post_exams = paginator.page(paginator.num_pages)

            context['posts'] = post_exams

            index = post_exams.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 5 if index >= 5 else 0
            end_index = index + 5 if index <= max_index else max_index
            page_range = paginator.page_range[start_index: end_index]

            context['page_range'] = page_range

            # context = {
            #     'three_recent_posts': three_recent_posts,
            #     'posts': post_exams,
            #     'page_range': page_range,
            # }

            return context


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


"""
What to do if slug isn't unique? Maybe slugify title and compare to slugs in DB to check for uniqueness??? 'slug' is unique in Model, so wonder what would happen?
Ex: Creating a post and there is an error, the post is still added to DB. Debugging errors still add entry to DB, but don't redirect to the detail page

Probably combine both 'create' and 'edit' in one FormView
"""

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    login_url = '/registration/login/'
    template_name = 'blog/create_post.html'
    form_class = PostForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        post = form.save(commit=False)

        # post.author_id = User(request.user.id)
        # self.request.user.pk
        post.author_id = User.objects.get(pk=self.request.user.pk)
        post.pub_date = datetime.datetime.now()
        post.save()

        # OVERRIDES 'success_url'
        return HttpResponseRedirect(reverse('blog:edit-post', kwargs={'slug': post.slug}))


"""
Edit post option should only appear when the user who wrote the post (me) is logged-in
Use permissions?? Check in 'view_post.html' for permissions??
"""
class EditPostView(generic.UpdateView):
    template_name = 'blog/edit_post.html'
    context_object_name = 'specific_blog'
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.

        # Include some checking here for associating Post with User??? (self.request.user.pk)
        post = form.save(commit=False)
        # post.author_id = User.objects.get(pk=1)
        # post.pub_date = datetime.datetime.now()
        post.save()
        return HttpResponseRedirect(reverse('blog:view-post', kwargs={'slug': post.slug}))


class DeletePostView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')


"""
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            # post.author_id = User(request.user.id)
            post.author_id = User.objects.get(pk=1)
            print (post.author_id)
            post.pub_date = datetime.datetime.now()

            try:
                post.save()
                print (post.slug)
                return HttpResponseRedirect(reverse('blog:view-post', kwargs={'slug': post.slug}))
                #return HttpResponseRedirect('http://127.0.0.1:8000/blog/{slug}/'.format(slug=post.slug))
            except (IntegrityError) as e:
                print (type(e))
                # maybe add an error message to template here to tell error
                return render(request, 'blog/create_post.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = User.objects.get(pk=1)
            post.pub_date = datetime.datetime.now()
            post.save()
            return HttpResponseRedirect(reverse('blog:view-post', kwargs={'slug': post.slug}))
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})
"""
