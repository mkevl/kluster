import uuid as uuid
from enum import Enum

from django.db import models
from django.db.models import TextField, DecimalField, UUIDField, DateTimeField, URLField, CharField, ImageField, \
    ForeignKey


class InsuranceProvider(models.Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = TextField(null=False)
    name_en = TextField(blank=True, null=True)
    key = CharField(null=False, unique=True, max_length=50)
    description = TextField(null=False)
    phone = TextField(blank=True, null=True)
    email = TextField(blank=True, null=True)
    provider_image = ImageField(blank=True)
    provider_logo = ImageField(blank=True)
    created_at = DateTimeField(blank=True, auto_now_add=True)
    updated_at = DateTimeField(blank=True, auto_now=True)

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
