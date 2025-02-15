from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Spell
from .serializers import SpellSerializer

# Create your views here.


class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    lookup_field = "index"
    http_method_names = ["get"]
    pagination_class = None

    def list(self, request, *args, **kwargs):
        spells = self.get_queryset()
        count = spells.count()

        results = [
            {
                "index": spell.index,
                "name": spell.name,
                "url": f"/api/spells/{spell.index}",
            }
            for spell in spells
        ]

        return Response({"count": count, "results": results})
