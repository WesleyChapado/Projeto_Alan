from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from corev1.views import UserView

router = routers.DefaultRouter()

# registra suas outras rotas
router.register('register', UserView, basename = 'User')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1.0/', include(router.urls))
]
