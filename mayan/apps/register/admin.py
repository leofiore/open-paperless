from __future__ import unicode_literals

from django.contrib import admin

from .models import DocumentRegisterOut


@admin.register(DocumentRegisterOut)
class DocumentRegisterAdmin(admin.ModelAdmin):
    list_display = (
        'document', 'register_datetime', 'user',
    )
    list_display_links = None
