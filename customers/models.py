from enum import Enum

from django.db import models
import uuid as UUID

from insurance.models import InsurancePackage


class CustomerType(Enum):
    company = "company"
    person = "person"


class Customer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=UUID.uuid4, editable=False)
    type = models.CharField(choices=[(ct.value, ct.value) for ct in CustomerType], max_length=40)
    insurance_package = models.ForeignKey(InsurancePackage, related_name="customers", on_delete=models.DO_NOTHING)
    num_beneficiaries = models.PositiveIntegerField(null=False, default=1,
                                                    help_text="Number of beneficiaries for the customer")

    class Meta:
        db_table = "customer"

