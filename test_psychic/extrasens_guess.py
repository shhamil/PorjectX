import random

from django.conf import settings
from .models import Extrasens


class ExtrasensGuess(object):

    def __init__(self, request):
        self.session = request.session
        guess = self.session[settings.EXTRASENS_GUESS] = {}
        self.guess = guess

    def add(self, ext, ext_guess):
        extrasens_id = ext.id
        if extrasens_id not in self.guess:
            self.guess[extrasens_id] = {"ext_name": ext.name, "ext_guess": ext_guess}
        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        extrasenses = Extrasens.objects.all()

        for item in self.guess.values():
            yield item
