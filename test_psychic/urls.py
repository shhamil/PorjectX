from django.urls import path
from django.views.generic import TemplateView
from .views import SendNumberView, IndexView

app_name = 'test_psychic'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('send_number', SendNumberView.as_view(), name='send_number'),
]