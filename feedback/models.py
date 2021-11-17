from django.db import models
import uuid


class UserFeedback(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_full_name = models.CharField(blank=False, max_length=100)
    feedback_text = models.TextField(blank=False, max_length=500)
    image = models.TextField(blank=True, null=True, max_length=500)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        db_table = 'user_feedback'

    def __str__(self):
        return self.user_full_name
