from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

#主畫面
class Main(ListView):
    model = Shop

# class Name(DetailView):
#     model = Option