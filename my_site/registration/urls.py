from django.urls import include, path
from . import views


app_name = 'registration'

urlpatterns = [

    # /registration/...
    # path('', include('django.contrib.auth.urls')),

    # /registration/account/pk
    path('account/<int:pk>/', views.DetailView.as_view(), name='view-account'),
]
