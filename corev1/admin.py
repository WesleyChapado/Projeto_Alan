from django.contrib import admin
from corev1.organization.models import OrganizationModel
from corev1.plan.models import PlanModel

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



