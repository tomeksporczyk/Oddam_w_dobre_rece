from rest_framework import mixins, viewsets
from .models import *
from .serializers import *


class UserSerializerView(mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdminSerializerView(mixins.ListModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserSerializer


class InstitutionSerializerView(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer



class ASerializer():
    pass