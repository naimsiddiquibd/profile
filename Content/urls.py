from django.urls import path
from Content.views import Home

urlpatterns = [
    path('', Home, name='Home')
    
]
