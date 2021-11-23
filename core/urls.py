from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Doctores API",
        default_version='v1',
        description="Test description",
        terms_of_service="ApsCreativas",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="ApsCreativas"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('apps.contacts.urls')),
)

# Swagger
urlpatterns += (
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
)
