from django.conf import settings


class Logs(object):
    def __init__(self, request):
        self.session = request.session
        logs = self.session.get(settings.GUESSES_LOG)
        if not logs:
            logs = self.session[settings.GUESSES_LOG] = {}
        self.logs = logs

    def add(self, ext, user_number, guess):
        log_id = len(self.logs) + 1
        if int(user_number) == int(guess):
            ext.rating += 1
            ext.save()
        else:
            ext.rating -= 1
            ext.save()
        if ext.rating > 100:
            ext.rating = 100
            ext.save()
        if ext.rating < 0:
            ext.rating = 0
            ext.save()
        self.logs[log_id] = {'attempt': ((log_id - 1) // 2) + 1, "user_number": user_number, "ext_name": ext.name, "guess": guess}

        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        for item in self.logs.values():
            yield item