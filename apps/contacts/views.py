from rest_framework import viewsets
from .serializers import ContactSerializer, GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = serializer_class.Meta.model.objects.all()
