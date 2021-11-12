from rest_framework import serializers


class FaqSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    question = serializers.CharField(required=True, max_length=400)
    answer = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        fields = ("uuid", "question", "answer", "created_at", "updated_at")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
