from.views import *

from django.urls import path

urlpatterns = [
    path('add',add,name='add'),
    path('',home,name='home')
     ]