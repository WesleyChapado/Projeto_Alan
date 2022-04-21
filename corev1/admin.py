from django.contrib import admin
from corev1.organization.models import OrganizationModel

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status','created')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(OrganizationModel, OrganizationAdmin)



