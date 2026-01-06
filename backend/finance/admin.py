from django.contrib import admin
from .models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'is_active')
    list_filter = ('company', 'is_active')
    search_fields = ('name',)
    ordering = ('company', 'name')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'company',
        'transaction_type',
        'amount',
        'category',
        'date',
        'user',
    )

    list_filter = (
        'company',
        'transaction_type',
        'category',
        'date',
    )

    search_fields = ('description',)
    ordering = ('-date',)
    date_hierarchy = 'date'
