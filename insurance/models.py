import uuid as uuid
from enum import Enum

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import DecimalField, UUIDField, DateTimeField, ForeignKey, Max


class InsuranceProvider(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False)
    name_en = models.TextField(blank=True, null=True)
    description = models.TextField(null=False)
    phone = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    provider_image = models.TextField(blank=True, null=True, max_length=500)  # Revert to ImageField
    provider_logo = models.TextField(blank=True, null=True, max_length=500)  # Revert to ImageField
    position = models.PositiveIntegerField(primary_key=False, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        db_table = "insurance_provider"

    def clean(self):
        if self.is_active:
            num_active_providers = InsuranceProvider.objects.filter(is_active=True).exclude(pk=self.uuid).count()
            if num_active_providers > 0:
                raise ValidationError(
                    {"is_active": ["Cannot mark provider as active - other provider is already marked as active"]})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.position is None:
            max_position = InsuranceProvider.objects.filter(name='asd').aggregate(Max('position')).get(
                'position__max') or 0
            self.position = max_position + 1
        super(InsuranceProvider, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class InsuranceType(Enum):
    personal = "health"
    company = "life"


class PackageType(Enum):
    minimal = "minimal"
    basic = "basic"
    improved = "improved"


class InsurancePackage(models.Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provider = ForeignKey(InsuranceProvider, on_delete=models.DO_NOTHING)
    price_per_month = DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    price_last_updated_at = DateTimeField(blank=True, null=True)
    insurance_type = models.CharField(blank=False, choices=[(tag.value, tag.value) for tag in InsuranceType],
                                      max_length=20)
    is_best_offer = models.BooleanField(default=False)
    package_type = models.CharField(blank=False, choices=[(tag.value, tag.value) for tag in PackageType], max_length=20)
    created_at = DateTimeField(blank=True, auto_now_add=True)
    updated_at = DateTimeField(blank=True, auto_now=True)

    class Meta:
        db_table = "insurance_package"

    def __str__(self):
        return f"{self.provider.name} - {self.insurance_type}, {self.package_type}"
