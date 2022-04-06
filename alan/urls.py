from django.contrib import admin
from django.urls import re_path
from corev1.views import OrganizationView, UserView

urlpatterns = [
    re_path('admin/', admin.site.urls), 
    re_path(r'^v1.0/register/user/?$', UserView.as_view(), name='User'), 
    re_path(r'^v1.0/register/organization/?$', OrganizationView.as_view(), name='Organization')
]