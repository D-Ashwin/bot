import json
import telebot
import requests
import telegram
import random 

from telebot import types
from telebot.types import *

from django.views import View
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import PlayList


bot = telebot.TeleBot("1132917333:AAGBF1elQJq96ERjNNKlt0f7__QQP6hyQH0")

User = get_user_model()


class BotView(View):
    def post(self, request, *args, **kwargs):
        try:
            t_data = json.loads(request.body)
            t_message = t_data["message"]
            t_chat = t_message["chat"]
            chat_id = t_chat["id"]
            try:
                text = t_message["text"].strip().lower()
            except Exception as e:
                return JsonResponse({"ok": "POST request processed"})

            text = text.lstrip("/")
            if text == "start":
                markup = types.InlineKeyboardMarkup()
                itembtna = types.InlineKeyboardButton('Wanna Listen smth Lit ?', switch_inline_query="",callback_data="music")
                itembtnv = types.InlineKeyboardButton('Random YouTube PlayList', switch_inline_query="", callback_data="playlist")
                itembtnc = types.InlineKeyboardButton('Generate Random Number', switch_inline_query="", callback_data="random_num")
                markup.row(itembtna)
                markup.row(itembtnv, itembtnc)
                bot.send_message(chat_id, "Choose one Option:", reply_markup=markup)
            elif text == "help":
                bot.send_message(chat_id, "Hi, How are you? reply with start.")

            else:
                msg = "Unknown command"
                bot.send_message(chat_id,msg)

            return JsonResponse({"ok": "POST request processed"})
        except:
            # Callbacks here
            t_data = json.loads(request.body)
            t_message = t_data["callback_query"]['message']['chat']
            chat_id = t_message.get('id')
            text = t_data["callback_query"]['data']

            if text == "music":
                bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
                sound = settings.SOUNDS_DIR
                bot.send_voice(chat_id=chat_id, voice=open(sound+'/La_Calin.mp3', 'rb'))
            elif text == "playlist":
                count = PlayList.objects.count()
                random_item = PlayList.objects.all()[random.randint(0, count - 1)]
                playlist_url = random_item.url
                msg = str(playlist_url)
                bot.send_message(chat_id,msg)
            elif text == "random_num":
                msg = random.randint(0,100)
                bot.send_message(chat_id,msg)
            else:
                msg = "Unknown command"
                bot.send_message(chat_id,msg)
            return JsonResponse({"ok": "POST request processed"})
