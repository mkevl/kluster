import uuid as uuid
from enum import Enum

from django.db import models
from django.db.models import DecimalField, UUIDField, DateTimeField, ForeignKey


class InsuranceProvider(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False)
    name_en = models.TextField(blank=True, null=True)
    key = models.CharField(null=False, unique=True, max_length=50)
    description = models.TextField(null=False)
    phone = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    provider_image = models.ImageField()
    provider_logo = models.ImageField()
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        db_table = "insurance_provider"

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
    price_per_month = DecimalField(decimal_places=2, max_digits=12)
    price_last_updated_at = DateTimeField(blank=True, null=True)
    insurance_type = models.CharField(blank=False, choices=[(tag.value, tag.value) for tag in InsuranceType],
                                      max_length=20)
    package_type = models.CharField(blank=False, choices=[(tag.value, tag.value) for tag in PackageType], max_length=20)
    created_at = DateTimeField(blank=True, auto_now_add=True)
    updated_at = DateTimeField(blank=True, auto_now=True)

    class Meta:
        db_table = "insurance_package"

    def __str__(self):
        return f"{self.provider.name} - {self.insurance_type}, {self.package_type}"
