from rest_framework import generics
from .serializers import SweetSerializer
from sweets.models import Sweet


class SweetsListApiView(generics.ListCreateAPIView):
    queryset=Sweet.objects.all()
    serializer_class=SweetSerializer




class SweetsDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Sweet.objects.all()
    serializer_class=SweetSerializer


     