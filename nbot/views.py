from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import telebot

# Create your views here.

@csrf_exempt
def webhook(request):
    bot = telebot.TeleBot('1842197193:AAGAkU5t6JYzeBogk2RAl2u-v7HHyNKmnp0')
    bot.send_message(1080427042, 'From nybble site')
    # foo = open('/home/nybble/nybble/mysite/nbot/bot.log', 'a')
    # foo.write('It works!!!!!')
    context = {}
    # return render(request, 'tools/webhook.html', context)
    return JsonResponse({'response': 'OK'})
