from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_properties, name='all_properties')  
]
