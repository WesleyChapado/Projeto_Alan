from django.contrib import admin
from corev1.document.models import DocumentModel
from corev1.folder.models import FolderModel
from corev1.organization.models import OrganizationModel
from corev1.plan.models import PlanModel
from corev1.dialog.models import DialogModel

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status','created')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(OrganizationModel, OrganizationAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'max_knowledge_base', 'max_megabyte','max_users', 'plan_type')
    list_display_links = ('id','max_knowledge_base', 'max_megabyte')
    search_fields = ('id',)
    list_per_page = 20

admin.site.register(PlanModel, PlanAdmin)

class FolderAdmin(admin.ModelAdmin):
    list_display = (
        'uuid', 'name',
        'created', 'deleted', 'updated',
        'active', 'user_owner'
    )
    list_display_links = ('uuid', 'user_owner', 'name')
    search_fields = ('uuid', 'user_owner', 'name')
    list_per_page = 20
    
admin.site.register(FolderModel, FolderAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'uuid', 'name',
        'created', 'file_size','file', 'deleted', 'updated',
        'active', 'user_owner'
    )
    list_display_links = ('id','uuid', 'user_owner', 'name', 'file')
    search_fields = ('id', 'uuid', 'user_owner', 'name', 'file')
    list_per_page = 20
    
admin.site.register(DocumentModel, DocumentAdmin)

class DialogAdmin(admin.ModelAdmin):
    list_display = (
        'question', 'answer', 'file', 
        'user_owner', 'dialog_id', 'answer_id',
        'folder_name', 'created'
    )
    list_display_links = ('dialog_id', 'user_owner')
    search_fields = ('dialog_id', 'user_owner')
    list_per_page = 20
    
admin.site.register(DialogModel, DialogAdmin)
