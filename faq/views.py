from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from faq.models import FrequentlyAskedQuestion
from faq.serializers import FaqSerializer


class FaqViewSet(ModelViewSet):
    queryset = FrequentlyAskedQuestion.objects.all()
    serializer_class = FaqSerializer

    def update(self, request, *args, **kwargs):
        return Response(status=403)

    def create(self, request, *args, **kwargs):
        return Response(status=403)

    def destroy(self, request, *args, **kwargs):
        return Response(status=403)
