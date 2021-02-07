from django.urls import path
from . import views


app_name = 'bikes'

urlpatterns = [
    path('', views.bike_list, name='bike_list'),
    path('<slug:slug>', views.bike_detail, name='bike_detail')
    
]