from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.envs.models import Envs
from apps.envs.serializers import EnvsModelSerializer


class EnvsViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Envs.objects.all().order_by('id')
    serializer_class = EnvsModelSerializer
    permission_classes = [IsAuthenticated]
