from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include

from staff.views import *

router = routers.DefaultRouter()
router.register('users', UserSerializerView, basename='user')
router.register('admins', AdminSerializerView, basename='admin')
router.register('institutions', InstitutionSerializerView)
router.register('targets', TargetSerializerView)
router.register('items', ItemSerializerView)
router.register('provinces', ProvinceSerializerView)


urlpatterns = [
    path('staff', include(router.urls)),
    url(r'^staff/', include((router.urls, 'staff'), namespace='staff')),
    path('api-auth', include('rest_framework.urls'))
]
