from django.contrib import admin

from customers.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('type', 'insurance_package', 'num_beneficiaries')
    list_filter = ('type', 'insurance_package')


admin.site.register(Customer, CustomerAdmin)
