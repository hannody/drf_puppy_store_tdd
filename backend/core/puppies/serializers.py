from rest_framework import serializers

from .models import Puppy


class PuppySerializer(serializers.ModelSerializer):
    """
    Serializer Class
    """
    class Meta:
        """
        To specify some attributes for the Puppy model serialization
        """
        model = Puppy
        fields = ('id', 'name', 'age', 'breed', 'color',)
