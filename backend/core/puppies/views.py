from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from .models import Puppy
from .serializers import PuppySerializer


class PuppiesList(ListAPIView):
    """
    List all puppies without pagination
    """
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer


class PuppyDetail(RetrieveAPIView):
    """
    The detail of a single puppy.
    """
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer


class PuppyCreate(CreateAPIView):
    """
        Create A Puppy view
    """
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
