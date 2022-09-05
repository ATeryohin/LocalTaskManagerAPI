from rest_framework import serializers
from .models import Board, State, Card

class BoardSerializers(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()

    class Meta:
        model = Board
        fields = ('name', )

class StateSerializers(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
    board = serializers.SerializerMethodField(method_name='get_board')

    def get_board(self, state):
        print('asdasdasdasd')
        return BoardSerializers(state.board)

    class Meta:
        model = State
        fields = ('name', 'board')

class CardSerializers(serializers.HyperlinkedModelSerializer):
    state = StateSerializers()
    description = serializers.CharField()
    title = serializers.CharField()
    board = BoardSerializers()
    created = serializers.DateTimeField()
    id = serializers.IntegerField()

    def get_state(self, card):
        print('in get_state method', card)
        return StateSerializers(card.state)

    def get_board(self, card):
        print('in get_board method', card)
        return BoardSerializers(card.board)

    class Meta:
        model = Card
        # fields = ('title', )
        fields = ('state', 'description', 'title', 'board', 'created', 'id')