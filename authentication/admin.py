from django.contrib import admin
from .models import AllowedEmail


@admin.register(AllowedEmail)
class AllowedEmailAdmin(admin.ModelAdmin):
    list_display = ('email',)
