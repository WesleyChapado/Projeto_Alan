from django.contrib import admin
from corev1.models import UserModel, OrganizationModel

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','email', 'organization')
    list_display_links = ('id','first_name')
    search_fields = ('first_name',)
    list_per_page = 20

admin.site.register(UserModel, UserModelAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status','created')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(OrganizationModel, OrganizationAdmin)



