from django.urls import path
from .views import index,contact,blog


urlpatterns = [
    path('',index,name='index'),
    path('contact',contact,name='contact'),
    path('blog',blog,name='blog')]