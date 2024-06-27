# demoapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('set-session/', views.set_session, name='set_session'),
]
