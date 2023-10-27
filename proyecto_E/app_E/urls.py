from django.urls import path 
from . import views  

urlpatterns=[
   path('', views.vista1, name='vista1' ) 
]



