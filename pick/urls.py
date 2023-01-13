from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.Main.as_view()),
    path('main/<int:pk>/', views.Name.as_view()),
]