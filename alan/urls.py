from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from corev1.views import OrganizationView, UserView

router = routers.DefaultRouter()

router.register('user', UserView, basename = 'User')
router.register('organization', OrganizationView, basename = 'Organization')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1.0/register/', include(router.urls))
]
