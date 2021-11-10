from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=False)
    type = serializers.CharField(max_length=40)
    insurance_type = serializers.CharField(max_length=20)
    insurance_package_type = serializers.CharField(max_length=20)
    num_beneficiaries = serializers.IntegerField()
    
    class Meta:
        model = Customer
        fields = []

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


def get_customer_count():
    pass
