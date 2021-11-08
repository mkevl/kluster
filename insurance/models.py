import uuid as uuid
from django.db import models
from django.db.models import TextField, DecimalField, UUIDField, DateTimeField, URLField


class InsuranceProvider(models.Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = TextField(null=False)
    price_per_month = DecimalField(decimal_places=2, max_digits=12)
    image_url = URLField(blank=True)
    created_at = DateTimeField(blank=True, auto_now_add=True)
    updated_at = DateTimeField(blank=True, auto_now=True)

    list_display = ('name', 'updated_at')
