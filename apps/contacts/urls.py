from rest_framework import routers
from .views import ContactViewSet, GroupViewSet

routers = routers.DefaultRouter()
routers.register(r'contacts', ContactViewSet, 'contacts')
routers.register(r'groups', GroupViewSet, 'groups')

urlpatterns = routers.urls
