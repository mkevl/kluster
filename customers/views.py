from django.db.models import Q, Count, Sum
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from customers.models import Customer, CustomerType
from customers.serializers import CustomerSerializer


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@api_view(['GET'])
@permission_classes([])
def get_customer_counts(request):
    query_params = request.query_params
    queries = []
    if 'insurance_type' in query_params:
        queries.append(
            Q(insurance_type=query_params.get('insurance_package__insurance_type')))
    if 'package_type' in query_params:
        queries.append(Q(package_type=query_params.get('insurance_package__package_type')))

    queryset = Customer.objects.filter(*queries)
    num_companies = queryset.filter(type=CustomerType.company.value).count()
    beneficiaries_grouped = queryset.values('type').annotate(summed_beneficiaries=Sum('num_beneficiaries')).all()
    total_beneficiaries = 0
    for beneficiary_count_by_type in beneficiaries_grouped:
        total_beneficiaries += beneficiary_count_by_type.get('summed_beneficiaries') or 0

    return Response(status=200, data={'companies': num_companies, 'persons': total_beneficiaries})
