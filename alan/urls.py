from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
<<<<<<< HEAD
from corev1.views import OrganizationView, UserView
=======
from corev1.views import UserView
>>>>>>> 4c1e03151ce5a177d1c8621d1a5dd57a435c6ed5

router = routers.DefaultRouter()

# registra suas outras rotas
<<<<<<< HEAD
router.register('user', UserView, basename = 'User')
router.register('organization', OrganizationView, basename = 'Organization')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1.0/register/', include(router.urls))
=======
router.register('register', UserView, basename = 'User')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1.0/', include(router.urls))
>>>>>>> 4c1e03151ce5a177d1c8621d1a5dd57a435c6ed5
]
