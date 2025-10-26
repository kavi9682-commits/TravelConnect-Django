from rest_framework import viewsets
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

