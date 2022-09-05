from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Card, Board, State
from .serializers import CardSerializers, StateSerializers

# Create your views here.
class CardViewSet(APIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers

    def get(self, request, format=None):
        print(request)
        return Response(Card.objects.all())

    def post(self, request, format=None):
        board_id = request.data.get('board_id')
        boards = Board.objects.filter(id=board_id)
        if not boards.exists():
            return Response({f'not found board by id = {board_id}'})

        board = boards[0]
        response = []

        filter_states = State.objects.filter(board=board)
        for state in filter_states:
            filter_cards = Card.objects.filter(state=state)
            cards_data = []
            for card in filter_cards:
                obj = {'id': card.id,
                 'title': card.title,
                 'description': card.description,
                 'created': card.created}
                cards_data.append(obj)
            response.append({'title': state.name, 'card': cards_data})

        return Response({'board': {'states': response}})


class StateViewSet(APIView):
    serializer_class = StateSerializers
    queryset = State.objects.all()

    @classmethod
    def get_extra_actions(cls):
        return []
