from django.urls import path, include
from django.conf import settings
from . import views




urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('view/<int:pk>', views.dream_view, name='dream_view'),
    path('new/', views.dream_create, name='dream_create'),
    path('edit/<int:pk>', views.dream_update, name='dream_update'),
    path('delete/<int:pk>', views.dream_delete, name='dream_delete'),

]
