from django.shortcuts import render
from django.views import generic
from . import models


class IndexView(generic.ListView):
    model = models.Resume
    template_name = 'my_cv/index.html'
