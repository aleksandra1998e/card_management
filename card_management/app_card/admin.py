from django.contrib import admin
from .models import Card, Purchase


class PurchaseInLine(admin.StackedInline):
    model = Purchase


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['series', 'number', 'release_date', 'end_date', 'status']
    search_fields = ['series', 'number']
    list_filter = ['release_date', 'end_date', 'status', 'series']
    inlines = [PurchaseInLine]
    actions = ['mark_as_active', 'mark_as_inactive', 'mark_as_expired']

    def mark_as_active(self, request, queryset):
        queryset.update(status='a')

    def mark_as_inactive(self, request, queryset):
        queryset.update(status='n')

    def mark_as_expired(self, request, queryset):
        queryset.update(status='e')

    mark_as_active.short_description = 'Активировать'
    mark_as_inactive.short_description = 'Дективировать'
    mark_as_expired.short_description = 'Просрочена'


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['date', 'amount', 'card']
    list_filter = ['card', 'date']
