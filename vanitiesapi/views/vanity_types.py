"""View module for handling requests about vanity_types"""
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from vanitiesapi.models import VanityType


class VanityTypeView(ViewSet):
    """vanities views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single vanity_type

        Returns:
            Response -- JSON serialized vanity_type
        """

        vanity_type = VanityType.objects.get(pk=pk)
        serializer = VanityTypeSerializer(vanity_type)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all vanity_type

        Returns:
            Response -- JSON serialized list of vanity_type
        """

        vanity_types = VanityType.objects.all()
        serializer = VanityTypeSerializer(vanity_types, many=True)
        return Response(serializer.data)


class VanityTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for vanity_types
    """
    class Meta:
        model = VanityType
        fields = ('id', 'label')
