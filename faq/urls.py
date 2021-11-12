from rest_framework import routers

from faq.views import FaqViewSet

router = routers.DefaultRouter()
router.register(r'', FaqViewSet)

urlpatterns = router.urls
