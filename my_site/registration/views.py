from django.contrib.auth import views as auth_views
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class LoginView(auth_views.LoginView):
    redirect_authenticated_user = True


class DetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'registration/account.html'
    context_object_name = 'user_account'
    model = User
