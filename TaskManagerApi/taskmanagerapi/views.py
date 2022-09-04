from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .models import Card, Board, State
from .serializers import CardSerializers, StateSerializers

# Create your views here.
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializers


class StateViewSet(ListAPIView):
    serializer_class = StateSerializers
    queryset = State.objects.all()

    @classmethod
    def get_extra_actions(cls):
        return []
