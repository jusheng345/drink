from django.urls import path
from . import views

urlpatterns = [
    
    path('main/', views.Main.as_view()),
    path('main/<int:pk>/', views.Name.as_view()),
    path('main/create/',views.ShopCreate.as_view()),
    path('main/<int:pk>/update/',views.ShopUpdate.as_view()),
    path('main/<int:pk>/delete/',views.ShopDelete.as_view()),


]