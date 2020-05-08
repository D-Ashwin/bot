from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from .views import *


app_name='telegrambot'

urlpatterns = [
    path('webhooks/bot/', csrf_exempt(BotView.as_view())),
]
