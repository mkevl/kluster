from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from cluster import settings
from insurance.views import InsuranceProviderViewSet, InsurancePackageViewSet

router = routers.DefaultRouter()
router.register(r'insurance/providers', InsuranceProviderViewSet)
router.register(r'insurance/packages', InsurancePackageViewSet)

urlpatterns = [
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
              ] + router.urls
