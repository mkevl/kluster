from rest_framework import serializers

from common.utils import construct_media_url
from insurance.models import InsuranceProvider, InsurancePackage


class InsuranceProviderSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=200)
    name_en = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    phone = serializers.CharField(max_length=20)
    site = serializers.URLField(max_length=20)
    provider_image_url = serializers.SerializerMethodField()
    provider_logo_url = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = InsuranceProvider
        fields = ["uuid", "name", "name_en", "description", "image", "created_at", "updated_at", "logo"]

    def get_provider_image_url(self, instance):
        return construct_media_url(instance.provider_image.url)

    def get_provider_logo_url(self, instance):
        return construct_media_url(instance.provider_logo.url)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class InsurancePackageSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    provider = serializers.SerializerMethodField()
    price_per_month = serializers.DecimalField(max_digits=12, decimal_places=2)
    price_last_updated_at = serializers.DateTimeField()
    insurance_type = serializers.CharField(max_length=20)
    package_type = serializers.CharField(max_length=20)

    class Meta:
        model = InsurancePackage
        fields = ["uuid", "provider", "price_per_month", "insurance_type", "package_type", "price_last_updated_at"]

    def get_provider(self, instance):
        provider = instance.provider
        return InsuranceProviderSerializer(instance=provider).data

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
