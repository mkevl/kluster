from django.contrib import admin

from feedback.models import UserFeedback


class UserFeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_full_name', 'short_text')

    def short_text(self, obj):
        return obj.feedback_text[:25] + ("..." if (len(obj.feedback_text) > 25) else "")


admin.site.register(UserFeedback, UserFeedbackAdmin)
