from rest_framework import viewsets

from insurance.models import InsuranceProvider, InsurancePackage
from insurance.serializers import InsuranceProviderSerializer, InsurancePackageSerializer


class InsuranceProviderViewSet(viewsets.ModelViewSet):
    queryset = InsuranceProvider.objects.all()
    serializer_class = InsuranceProviderSerializer


class InsurancePackageViewSet(viewsets.ModelViewSet):
    queryset = InsurancePackage.objects.all()
    serializer_class = InsurancePackageSerializer
