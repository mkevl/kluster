from rest_framework import viewsets

from insurance.models import InsuranceProvider
from insurance.serializers import InsuranceProviderSerializer


class InsuranceProviderViewSet(viewsets.ModelViewSet):
    queryset = InsuranceProvider.objects.all()
    serializer_class = InsuranceProviderSerializer
