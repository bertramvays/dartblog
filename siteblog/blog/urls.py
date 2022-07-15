from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'), # и вызове пустой страницы будет вызываться ф-я index
    path('category/<str:slug>', get_category, name='category'),
]