"""
URL configuration for pampulha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from pampulha.apps.anamnesis.views import (
    AnamnesisModelViewset,
    MonitoringSheetModelViewset,
)
from pampulha.apps.management.views import (
    AuthenticationVerifyView,
    AuthenticationView,
    loggin_as,
)

router_v1 = DefaultRouter(trailing_slash=False)
router_v1.register(
    "monitoring-sheet", MonitoringSheetModelViewset, basename="MonitoringSeet"
)
router_v1.register("anamnesis", AnamnesisModelViewset, basename="Anamnesis")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router_v1.urls)),
    # Token
    path("api/v1/token/", AuthenticationView.as_view(), name="obtain_token"),
    path(
        "api/v1/token/verify/", AuthenticationVerifyView.as_view(), name="obtain_token"
    ),
    path("api/v1/loggin", loggin_as, name="loggin_as"),
]
