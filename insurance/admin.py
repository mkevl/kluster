from django.contrib import admin

# Register your models here.
from insurance.models import InsuranceProvider, InsurancePackage


class InsuranceProviderAdmin(admin.ModelAdmin):
    list_display = ('position', 'name', 'updated_at', 'is_active')


class InsurancePackageAdmin(admin.ModelAdmin):
    list_display = ('provider', 'insurance_type', 'package_type', 'price_per_month', 'price_last_updated_at',
                    'is_best_offer')
    list_filter = ('insurance_type', 'package_type', 'provider')


admin.site.register(InsuranceProvider, InsuranceProviderAdmin)

admin.site.register(InsurancePackage, InsurancePackageAdmin)
