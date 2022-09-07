import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Card, Board, State
from .serializers import CardSerializers, StateSerializers, BoardSerializers

class CardViewSet(APIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers

    def post(self, request, format=None):
        board_id = request.data.get('board_id')
        boards = Board.objects.filter(id=board_id)
        if not boards.exists():
            # TODO
            return Response({f'Not found board by id = {board_id}'})

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

class CardCreateView(APIView):
    def post(self, request):
        board_id = request.data.get('board_id')
        boards = Board.objects.filter(id=board_id)
        if not boards.exists():
            # TODO
            return Response({f'Not found board by id = {board_id}'})

        board = boards[0]

        state_id = request.data.get('state_id')
        states = State.objects.filter(id=state_id)
        if not states.exists():
            # TODO
            return Response({f'Not found state by id = {state_id}'})

        state = states[0]
        description = request.data.get('description')
        title = request.data.get('title')
        created = datetime.datetime.now()

        validation_data = {'state': state, 'description': description,
                           'title': title, 'board': board,
                           'created': created}

        serializer = CardSerializers(data=validation_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        # TODO
        return Response({f"success': 'New card created"})

class StateCreateView(APIView):
    def post(self, request):
        board_id = request.data.get('board_id')
        boards = Board.objects.filter(id=board_id)
        if not boards.exists():
            # TODO
            return Response({f'Not found board by id = {board_id}'})

        validation_data = {'board': boards[0], 'name': request.data.get('name')}
        serializer = StateSerializers(data=validation_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        # TODO
        return Response({f"success': 'New state for {boards[0].name} created"})

class StatesByBoardView(APIView):
    serializer_class = StateSerializers
    queryset = State.objects.all()

    def post(self, request, format=None):
        board_id = request.data.get('board_id')
        boards = Board.objects.filter(id=board_id)
        if not boards.exists():
            # TODO
            return Response({f'Not found board by id = {board_id}'})

        board = boards[0]

        states = State.objects.filter(board=board)
        states_resp = {{state.name} for state in states}

        return Response({'states': states_resp})


class BoardCreate(APIView):
    serializer_class = BoardSerializers
    queryset = Board.objects.all()

    def post(self, request):
        board_name = request.data.get('board_name')
        serializer = BoardSerializers(data={'name': board_name})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        # TODO
        return Response({'success': 'New board created'})

class BoardViewSet(ListAPIView):
    serializer_class = BoardSerializers
    queryset = Board.objects.all()