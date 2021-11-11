from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from feedback.models import UserFeedback
from feedback.serializers import UserFeedbackSerializer


class UserFeedbackViewSet(ModelViewSet):
    queryset = UserFeedback.objects.all()
    serializer_class = UserFeedbackSerializer

    def update(self, request, *args, **kwargs):
        return Response(status=403)

    def create(self, request, *args, **kwargs):
        return Response(status=403)

    def destroy(self, request, *args, **kwargs):
        return Response(status=403)
