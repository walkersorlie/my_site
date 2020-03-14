from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy, reverse, NoReverseMatch
from django.views import generic
from el_pagination.views import AjaxListView
from django.db import IntegrityError
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

from .models import Post
from .forms import PostForm


class IndexView(AjaxListView):
    template_name = 'blog/index.html'
    page_template = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        # return Post.objects.order_by('-pub_date')[:5]
        # return Post.objects.order_by('-pub_date')
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['three_recent_posts'] = self.get_queryset()[:3]
        context['paginated_posts'] = self.get_queryset()[3:]

        return context


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/view_post.html'
    context_object_name = 'specific_blog'
    query_pk_and_slug = True

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
    template_name = 'blog/create_post.html'
    form_class = PostForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        post = form.save(commit=False)

        # post.author_id = User(request.user.id)
        # self.request.user.pk
        post.author_id = User.objects.get(pk=self.request.user.pk)
        post.pub_date = timezone.now()
        post.save()

        # OVERRIDES 'success_url'
        return HttpResponseRedirect(reverse('blog:view_post', args=[post.slug]))



class MyPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        elif not user_test_result:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

"""
Edit post option should only appear when the user who wrote the post (me) is logged-in
Use permissions?? Check in 'view_post.html' for permissions??

Redirect to view_post if user is logged in but isn't the author.
Somehow set the error message??? This shit don't make much sense. Not sure how to do that
"""
class EditPostView(MyPermissionMixin, generic.UpdateView):
    permission_denied_message = "Only the author can edit this post"

    template_name = 'blog/edit_post.html'
    context_object_name = 'specific_blog'
    model = Post
    form_class = PostForm
    query_pk_and_slug = True

    # def get_context_data(self, **kwargs):
    #     context = super(EditPostView, self).get_context_data(**kwargs)
    #
    #     if 'exception' in kwargs:
    #         context['exception'] = self.get_permission_denied_message()
    #
    #     return context

    def test_func(self):
        # if the author of the post is the same as the person requesting the page, return true
        return self.get_object().author_id.pk == self.request.user.pk

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('blog:view_post', args=[self.get_object().slug]))

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.

        # Include some checking here for associating Post with User??? (self.request.user.pk)
        post = form.save(commit=False)
        # post.author_id = User.objects.get(pk=1)
        # post.pub_date = datetime.datetime.now()
        post.save()
        return HttpResponseRedirect(reverse('blog:view_post', args=[post.slug]))


class DeletePostView(MyPermissionMixin, generic.DeleteView):
    model = Post
    query_pk_and_slug = True
    success_url = reverse_lazy('blog:index')

    def test_func(self):
        # if the author of the post is the same as the person requesting the page, return true
        return self.get_object().author_id.pk == self.request.user.pk

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('blog:view_post', args=[self.get_object().slug]))


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
