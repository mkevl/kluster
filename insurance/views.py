from django.db.models import Q
from rest_framework import viewsets

from insurance.models import InsuranceProvider, InsurancePackage
from insurance.serializers import InsuranceProviderSerializer, InsurancePackageSerializer


class InsuranceProviderViewSet(viewsets.ModelViewSet):
    queryset = InsuranceProvider.objects.all()
    serializer_class = InsuranceProviderSerializer


class InsurancePackageViewSet(viewsets.ModelViewSet):
    queryset = InsurancePackage.objects.all()
    serializer_class = InsurancePackageSerializer

    def list(self, request, *args, **kwargs):
        query_params = request.query_params
        queries = []
        if 'insurance_type' in query_params:
            queries.append(
                Q(insurance_type=query_params.get('insurance_type')))
        if 'package_type' in query_params:
            queries.append(Q(package_type=query_params.get('package_type')))

        if queries:
            self.queryset = self.queryset.filter(*queries)

        return super(InsurancePackageViewSet, self).list(request, *args, **kwargs)
