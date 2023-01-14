from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    
    path('', RedirectView.as_view(url = 'main/')),
    path('main/', views.Main.as_view()),
    path('main/<int:pk>/', views.Name.as_view(), name='shop_view'),
    path('main/create/',views.ShopCreate.as_view()),
    path('main/<int:pk>/update/',views.ShopUpdate.as_view()),
    path('main/<int:pk>/delete/',views.ShopDelete.as_view()),
    path('option/<int:pk>/create/',views.OptionCreate.as_view()),
    path('option/<int:pk>/update/',views.OptionUpdate.as_view()),
    path('option/<int:pk>/delete/',views.OptionDelete.as_view()),

]