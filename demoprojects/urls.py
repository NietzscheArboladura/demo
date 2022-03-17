from django.urls import path
from demoprojects.views import *
from django.contrib.auth import views as auth_views



urlpatterns = [

path('', Main.as_view(), name='main'),

]