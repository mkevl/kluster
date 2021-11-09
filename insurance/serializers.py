from rest_framework import serializers

from insurance.models import InsuranceProvider


class InsuranceProviderSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = InsuranceProvider
        fields = ["uuid", "name", "price_per_month", "image_url"]
