from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse

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

class ShopUpdate(UpdateView):
    model = Shop
    fields = ['shopname']
    success_url = '/main/'
    template_name = 'general_form.html'

class ShopDelete(DeleteView):
    model = Shop
    success_url = '/main/'
    template_name = "shop_delete.html"

class OptionCreate(CreateView):
    model = Option
    fields = ['drinkname']
    template_name = "general_form.html"

    #新增後重新導向
    def get_success_url(self):
        return '/main/'+str(self.kwargs['pk'])+'/'

    #表單驗證 填上id
    def form_valid(self, form):
        form.instance.shop_id = self.kwargs['pk']
        return super().form_valid(form)

class OptionUpdate(UpdateView):
    model = Option
    fields = ['drinkname']
    template_name = 'general_form.html'
    
    def get_success_url(self):
        return '/main/'+str(self.object.shop_id)+'/'

class OptionDelete(DeleteView):
    model = Option
    template_name = "drink_delete.html"

    def get_success_url(self):
        return reverse('shop_view', kwargs={'pk': self.object.shop_id})
