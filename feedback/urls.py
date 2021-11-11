from rest_framework import routers

from feedback.views import UserFeedbackViewSet

router = routers.DefaultRouter()
router.register(r'', UserFeedbackViewSet)

urlpatterns = router.urls
