from django.db import models
import uuid


class FrequentlyAskedQuestion(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.TextField(blank=False, null=False, max_length=400)
    answer = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        db_table = 'faq'
