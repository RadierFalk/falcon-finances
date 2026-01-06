from django.contrib import admin
from .models import Company, User


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'company', 'is_staff', 'is_active')
    list_filter = ('company', 'is_staff', 'is_active')
    search_fields = ('email',)
