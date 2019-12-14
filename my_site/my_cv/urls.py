from django.urls import path
from . import views

app_name = 'my_cv'
urlpatterns = [

    # /my_cv/
    path('', views.IndexView.as_view(), name='index'),
]
