from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.cache import cache


class DetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'registration/account.html'
    context_object_name = 'user_account'
    model = User

    def get_object(self):
        return self.request.user


class LoginView(auth_views.LoginView):
    redirect_authenticated_user = True


class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'registration/admin_password_reset_email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cache.set('from_admin', True)
        return context


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy('admin_password_reset_complete')


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if cache.get('from_admin'):
            context['login_url'] = resolve_url('/admin/login')
        return context
