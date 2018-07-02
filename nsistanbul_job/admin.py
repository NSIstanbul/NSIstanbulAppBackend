from django.contrib.admin import register
from django.core.paginator import Paginator
from django.utils.translation import ugettext_lazy as _

from nsistanbul_job.models import Company, CompanyApp, Job

from import_export.admin import ImportExportModelAdmin

# Register your models here.


@register(Company)
class AdminCompany(ImportExportModelAdmin):
    list_display = ('name', 'email', 'is_deleted')
    list_filter = ('is_deleted',)
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('name', 'email',)
    ordering = ('name',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'icon_url', 'contact_url')
        }),
        (_("Status"), {
            'fields': ('is_deleted',)
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(CompanyApp)
class AdminCompanyApp(ImportExportModelAdmin):
    list_display = ('name', 'company', 'is_deleted')
    list_filter = ('is_deleted',)
    readonly_fields = ('created_at', 'modified_at')
    search_fields = ('name', 'company__name')
    ordering = ('name', 'company')
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('name', 'company', 'icon_url')
        }),
        (_("Status"), {
            'fields': ('is_deleted',)
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )


@register(Job)
class AdminJob(ImportExportModelAdmin):
    list_display = ('position_title', 'company', 'city', 'is_active', 'is_deleted')
    list_filter = ('is_active', 'is_deleted')
    readonly_fields = ('created_at', 'modified_at',)
    search_fields = ('position_title', 'company__name', 'city')
    ordering = ('position_title',)
    paginator = Paginator
    list_per_page = 50
    fieldsets = (
        (None, {
            'fields': ('company', 'city', 'position_title', 'description', 'url')
        }),
        (_("Status"), {
            'fields': ('is_active', 'is_deleted')
        }),
        (_("Date & Time"), {
            'fields': ('created_at', 'modified_at')
        })
    )