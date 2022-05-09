from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('register/',register),
    path('login/',loginn),
    path('logout/',logoutt),
    path('track/<st>/',track),
    path('map/<st>/',Map),
    path('api/<st>/',api),
    path('oth_api/<st>/',OthersApi),
        path('del/<st>/',deletes),

]