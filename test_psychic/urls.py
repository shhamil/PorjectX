from django.urls import path
from django.views.generic import TemplateView
from .views import index, UserNumberView

app_name = 'test_psychic'

urlpatterns = [
    path('', index, name='index'),
    path('send_number', UserNumberView.as_view(), name='get_extrasens_quess'),
]
