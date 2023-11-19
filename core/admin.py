from django.contrib import admin
from core.models import *
from django.contrib.auth.models import User

User.objects.filter(is_superuser=True)

# Register your models here.
@admin.register(GeneralSettings)


class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','parameters','update_date','create_date']
    search_fields = ['name','description']
    list_editable = ['name','description','parameters']
    class Meta:
        model = GeneralSettings
