from django.views.generic import TemplateView
from .models import Extrasens
from .extrasens_guess import ExtrasensGuess
from .logs import Logs
import random
from django.conf import settings
from django.shortcuts import render, redirect


class SendNumberView(TemplateView):

    def get(self, request, *args, **kwargs):
        extrasens_guess = ExtrasensGuess(request)
        for extrasens in Extrasens.objects.all():
            extrasens_guess.add(extrasens, random.randint(10, 99))
        return render(request, "test_psychic/send_number.html", {'extrasens_guesses': extrasens_guess})

    def post(self, request, *args, **kwargs):
        user_number = int(self.request.POST.get('user_number'))
        extr_guesses = request.session.get(settings.EXTRASENS_GUESS)
        logs = Logs(request)
        for extr in Extrasens.objects.all():
            logs.add(extr, user_number, extr_guesses[extr.id]['ext_guess'])
        return redirect("test_psychic:index")


class IndexView(TemplateView):

    def get(self, request, *args, **kwargs):
        logs = Logs(request)
        extrs = Extrasens.objects.all()
        return render(request, 'test_psychic/index.html', {'logs': logs, 'extrs': extrs})
