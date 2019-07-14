from OWDR.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='first_name')

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'is_staff', 'is_active', 'email')