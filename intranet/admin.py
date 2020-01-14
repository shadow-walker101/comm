from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import * 


class UserAdmin(BaseUserAdmin):
   
    
    list_display = ('email', 'user_type', 'department', 'username', 'is_admin')
    list_filter = ('is_admin',)
    
    fieldsets = (
        
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('user_type','department')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    
    add_fieldsets = (
         (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_type','department','username', 'password1', 'password2'),
        }),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    
admin.site.register(User, UserAdmin)
