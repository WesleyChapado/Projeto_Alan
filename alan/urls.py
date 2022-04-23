from django.contrib import admin
from django.urls import re_path, include
from corev1.organization.views import OrganizationView
from user.views import UserCreate, UserList
from user.token.views import TokenView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
	# titulo
    title="Projeto Alan",
	
    # versao
    default_version='v1',
    
    # descrição
    description="Um projeto de treinamento criado por Marco Oliveira.",
    
    #link com os termos de serviço
    #terms_of_service="#",
			
    # contato
    contact=openapi.Contact(email="wesley-chapado@hotmail.com"),
      
    # licença
    #license=openapi.License(name=""),
    ),
    # permissão
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^admin/', admin.site.urls), 
    re_path(r'^v1.0/register/user/list?$', UserList.as_view(), name='Userlist'),
    re_path(r'^v1.0/register/user/create/?$', UserCreate.as_view(), name='UserCreat'),  
    re_path(r'^v1.0/register/organization/?$', OrganizationView.as_view(), name='Organization'),
    re_path(r'^v1.0/register/token/?$', TokenView.as_view(), name='Token'),
    re_path(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
