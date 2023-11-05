from django.contrib import admin
from core.models import GeneralSettings
from django.contrib.auth.models import User

User.objects.filter(is_superuser=True)

# Register your models here.
admin.site.register(GeneralSettings)


class GeneralSettingAdmin(admin.ModelAdmin):
    class Meta:
        model = GeneralSettings
