from rest_framework import routers
from django.urls import path, include

from staff.views import *

router = routers.DefaultRouter()
router.register('users', UserSerializerView, basename='users')
router.register('admins', AdminSerializerView, basename='admins')
router.register('institutions', InstitutionSerializerView)
router.register('targets', TargetSerializerView)
router.register('items', ItemSerializerView)
router.register('provinces', ProvinceSerializerView)


urlpatterns = [
    path('staff/', include(router.urls)),
    path('api-auth', include('rest_framework.urls'))
]
