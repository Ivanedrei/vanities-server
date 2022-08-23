"""View module for handling requests about sizes"""
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from vanitiesapi.models import Size


class SizeView(ViewSet):
    """vanities views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single size

        Returns:
            Response -- JSON serialized size
        """

        size = Size.objects.get(pk=pk)
        serializer = SizeSerializer(size)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all size

        Returns:
            Response -- JSON serialized list of size
        """

        sizes = Size.objects.all()
        serializer = SizeSerializer(sizes, many=True)
        return Response(serializer.data)


class SizeSerializer(serializers.ModelSerializer):
    """JSON serializer for sizes
    """
    class Meta:
        model = Size
        fields = ('id', 'width')
