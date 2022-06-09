from django.contrib import admin
from django.urls import re_path
from corev1.folder.views import FolderView
from corev1.organization.views import OrganizationView
from corev1.plan.views import PlanView
from corev1.document.views import DocumentView, OpenPdfView
from user.views import LoginView, UserCreate, UserList
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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
    re_path(r'^v1.0/register/user/list/?$', UserList.as_view(), name='Userlist'),
    re_path(r'^v1.0/register/user/create/?$', UserCreate.as_view(), name='UserCreate'),  
    re_path(r'^v1.0/register/organization/?$', OrganizationView.as_view(), name='Organization'),
    re_path(r'^v1.0/register/plan/?$', PlanView.as_view(), name='Plan'),
    re_path(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^v1.0/register/login/?$', LoginView.as_view(), name='Login'),
    re_path(r'^v1.0/register/folder/?$', FolderView.as_view(), name='Folder'),
    path('v1.0/register/folder/<uuid>', FolderView.as_view()),
    re_path(r'^v1.0/register/document/?$', DocumentView.as_view(), name='Document'),
    path('v1.0/register/document/<uuid>', DocumentView.as_view()),
    re_path(r'v1.0/register/pdf_reader/?$', OpenPdfView.as_view()),
    path('v1.0/register/pdf_reader/<uuid>', OpenPdfView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
