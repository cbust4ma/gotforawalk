"""goforawalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import catalog.views
#pwa
from django.views.generic import TemplateView
#push



from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('devices', FCMDeviceAuthorizedViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),

    #push

    
]

urlpatterns += [
    
    path('sw.js', catalog.views.service_worker),
    path('offline/', TemplateView.as_view(template_name="offline.html")),
    path('catalog/', include('catalog.urls')),
    path(' ', include('pwa.urls')),
]


urlpatterns += [
    # URLs will show up at <api_root>/devices
    # DRF browsable API which lists all available endpoints
    path('api/', include(router.urls)),
    # ...
]

#Add URL maps to redirect the base URL to our application


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)