from rest_framework import mixins, viewsets
from .models import *
from .serializers import *


class UserSerializerView(mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = User.objects.filter(is_staff=False)
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


class ProvinceSerializerView(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class TargetSerializerView(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class ItemSerializerView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
