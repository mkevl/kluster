from rest_framework import routers

from insurance.views import InsuranceProviderViewSet, InsurancePackageViewSet

router = routers.DefaultRouter()
router.register(r'/providers', InsuranceProviderViewSet)
router.register(r'/packages', InsurancePackageViewSet)

urlpatterns = router.urls
