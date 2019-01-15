from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    redirect_authenticated_user = True
