from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

#主畫面
class Main(ListView):
    model = Shop

class Name(DetailView):
    model = Shop

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = Option.objects.filter(shop_id=self.kwargs['pk'])
        context['options'] = options
        return context

class ShopCreate(CreateView):
    model = Shop
    fields = ['shopname']
    success_url = '/main/'
    template_name = 'general_form.html'
