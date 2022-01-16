from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mer-masin', views.about, name='about'),
]