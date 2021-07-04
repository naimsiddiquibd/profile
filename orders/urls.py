from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('orders2', views.orders2, name='orders2'),
    path('orders3', views.orders3, name='orders3'),
]
