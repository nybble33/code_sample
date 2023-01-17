from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def iron_piece(request):
    return JsonResponse({'response': 'OK'})
