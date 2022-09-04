from rest_framework import serializers
from .models import Board, State, Card

class CardSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('description', 'title', 'state_id', 'created', 'id')

class StateSerializers(serializers.Serializer):
    name = serializers.CharField()
    board_id = serializers.IntegerField()

    class Meta:
        model = State
        fields = ('name', )