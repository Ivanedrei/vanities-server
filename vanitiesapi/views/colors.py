"""View module for handling requests about Colors"""
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from vanitiesapi.models import Color


class ColorView(ViewSet):
    """vanities views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single color

        Returns:
            Response -- JSON serialized color
        """

        color = Color.objects.get(pk=pk)
        serializer = ColorSerializer(color)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all color

        Returns:
            Response -- JSON serialized list of color
        """

        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)


class ColorSerializer(serializers.ModelSerializer):
    """JSON serializer for colors
    """
    class Meta:
        model = Color
        fields = ('id', 'label')
