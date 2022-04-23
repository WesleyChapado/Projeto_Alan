from django.contrib import admin
from user.models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','email')
    list_display_links = ('id','first_name', 'last_name', 'email')
    search_fields = ('id','email')
    list_per_page = 20

admin.site.register(UserModel, UserAdmin)
