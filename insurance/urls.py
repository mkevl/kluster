# Routers provide an easy way of automatically determining the URL conf.
from django.urls import path, include
from rest_framework import routers

from insurance.views import InsuranceProviderViewSet

router = routers.DefaultRouter()
router.register(r'', InsuranceProviderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('insurance-providers/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]