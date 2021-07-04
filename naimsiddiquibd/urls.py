"""naimsiddiquibd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Naim Siddiqui - Dashboard"
admin.site.site_title = "Naim Siddiqui - Dashboard"
admin.site.index_title = "Manage Content"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Content.urls')),
    path('banner/', include('banner.urls')),
    path('about/', include('about.urls')),
    path('services/', include('services.urls')),
    path('experience/', include('experience.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('pricing/', include('pricing.urls')),
    path('emails/', include('emails.urls')),
    path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
