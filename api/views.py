from django.shortcuts import render
from rest_framework import viewsets
from .models import Spell
from .serializers import SpellSerializer

# Create your views here.


class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    lookup_field = "index"
    http_method_names = ["get"]
