from django.contrib import admin

# Register your models here.
from insurance.models import InsuranceProvider, InsurancePackage


class InsuranceProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')


class InsurancePackageAdmin(admin.ModelAdmin):
    list_display = ('provider_name', 'insurance_type', 'package_type', 'price_per_month', 'price_last_updated_at')
    list_filter = ('insurance_type', 'package_type')

    @admin.display(ordering='provider__name')
    def provider_name(self, obj):
        return obj.provider.name


admin.site.register(InsuranceProvider, InsuranceProviderAdmin)

admin.site.register(InsurancePackage, InsurancePackageAdmin)
