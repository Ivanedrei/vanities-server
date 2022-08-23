"""View module for handling requests about woods"""
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from vanitiesapi.models import Wood


class WoodView(ViewSet):
    """vanities views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single wood

        Returns:
            Response -- JSON serialized wood
        """

        wood = Wood.objects.get(pk=pk)
        serializer = woodSerializer(wood)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all wood

        Returns:
            Response -- JSON serialized list of wood
        """

        woods = Wood.objects.all()
        serializer = woodSerializer(woods, many=True)
        return Response(serializer.data)


class woodSerializer(serializers.ModelSerializer):
    """JSON serializer for woods
    """
    class Meta:
        model = Wood
        fields = ('id', 'label')
