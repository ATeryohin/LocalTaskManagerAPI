from rest_framework import serializers
from .models import Board, State, Card

class BoardSerializers(serializers.Serializer):
    name = serializers.CharField()
    # id = serializers.IntegerField()

    class Meta:
        model = Board
        fields = ('name', )

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

class StateSerializers(serializers.Serializer):
    name = serializers.CharField()
    # id = serializers.IntegerField()
    board = serializers.SerializerMethodField(method_name='get_board')

    def get_board(self, state):
        print('asdasdasdasd')
        return BoardSerializers(state.board)

    def create(self, validated_data):
        return State.objects.create(**validated_data)

    class Meta:
        model = State
        fields = ('name', 'board')

class CardSerializers(serializers.Serializer):
    state = StateSerializers()
    description = serializers.CharField()
    title = serializers.CharField()
    board = BoardSerializers()
    created = serializers.DateTimeField()
    # id = serializers.IntegerField()

    def get_state(self, card):
        print('in get_state method', card)
        return StateSerializers(card.state)

    def get_board(self, card):
        print('in get_board method', card)
        return BoardSerializers(card.board)

    def create(self, validated_data):
        return Card.objects.create(**validated_data)

    class Meta:
        model = Card
        # fields = ('title', )
        fields = ('state', 'description', 'title', 'board', 'created', 'id')