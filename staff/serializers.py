from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="staff:user-detail")

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'is_staff', 'is_active', 'email')


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="staff:institution-detail")

    class Meta:
        model = Institution
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ('id', 'name',)


class TargetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Target
        fields = ('url', 'name',)


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'
