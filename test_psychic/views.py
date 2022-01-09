import random
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings


class UserNumberView(APIView):

    def get(self, request):
        extrasens_guess = request.session[settings.EXTRASENS_GUESS] = {}
        extrasens_guess_list = []
        extrasenses = request.session.get(settings.EXTRASENS)
        i = 1
        for extrasens in extrasenses:
            ext_guess = {"ext_name": extrasens["name"], "ext_guess": random.randint(10, 99)}
            extrasens_guess_list.append(ext_guess)
            extrasens_guess[i] = ext_guess
            i += 1
        return Response(extrasens_guess_list, status=status.HTTP_200_OK)

    def post(self, request):
        user_number = int(self.request.data.get('user_number'))
        extr_guesses = request.session.get(settings.EXTRASENS_GUESS)
        extrasenses = request.session.get(settings.EXTRASENS)
        logs = request.session.get(settings.GUESSES_LOG)
        if not logs:
            logs = request.session[settings.GUESSES_LOG] = {}
        log_id = len(logs) + 1
        i = 1
        for extrasens in extrasenses:
            if extr_guesses[i]["ext_guess"] == user_number:
                extrasens['rating'] += 1
            else:
                extrasens['rating'] -= 1
            i += 1
        log = {"user_number": user_number, "extr_guesses": extr_guesses}
        logs[log_id] = log
        return Response(logs, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def index(request):
    logs = request.session.get(settings.GUESSES_LOG)
    extrasenses = request.session.get(settings.EXTRASENS)
    if not extrasenses:
        extrasenses = request.session[settings.EXTRASENS] = [
            {'name': 'Baba Vanga', 'rating': 50},
            {'name': 'Notredame', 'rating': 50}
        ]
    response = {'logs': logs, 'extrs': extrasenses}
    return Response(response, status=status.HTTP_200_OK)
