from django.urls import path
from rest_framework import routers

from customers.views import CustomersViewSet, get_customer_counts

router = routers.DefaultRouter()
router.register(r'', CustomersViewSet)

urlpatterns = [
                  path('stats', view=get_customer_counts)
              ] + router.urls
