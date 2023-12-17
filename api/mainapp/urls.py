

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Novalitix test api",
      default_version='v1',
      description="Navalitix API test by Nguetoum anderson",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nguetoumanderson@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('novalitix.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
