from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('us/',us,name='us'),
    path('post/<int:post_id>',read,name='post'),
]