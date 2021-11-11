from rest_framework import serializers

from common.utils import construct_media_url


class UserFeedbackSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    user_full_name = serializers.CharField(max_length=100)
    feedback_text = serializers.CharField(max_length=500)
    image_url = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def get_image_url(self, instance):
        return construct_media_url(instance.image.url)



