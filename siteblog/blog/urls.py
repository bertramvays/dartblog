from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'), # и вызове пустой страницы будет вызываться ф-я index
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', get_post, name='post'),
]