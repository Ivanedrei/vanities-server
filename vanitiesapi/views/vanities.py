"""View module for handling requests about vanities"""
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from vanitiesapi.models import Vanities


class VanityView(ViewSet):
    """vanities views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """

        vanity = Vanities.objects.get(pk=pk)
        serializer = VanitySerializer(vanity)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """

        vanities = Vanities.objects.all()
        serializer = VanitySerializer(vanities, many=True)
        return Response(serializer.data)


class VanitySerializer(serializers.ModelSerializer):
    """JSON serializer for vanities
    """
    class Meta:
        model = Vanities
        fields = ('id', 'type', 'color', 'wood', 'size',
                  'price', 'image_url', 'description',
                  'quantity')
