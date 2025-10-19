"""
URL configuration for registerback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("apps.register.api.urls")),
    
    path('auth/', include('djoser.urls')),
    
    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='Token Obtain Pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='Token Refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='Blacklist'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='Token Verify'),
]
