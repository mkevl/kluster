from django.contrib import admin

# Register your models here.
from insurance.models import InsuranceProvider, InsurancePackage

admin.site.register(InsuranceProvider)
admin.site.register(InsurancePackage)
