from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
import anki.models as a_m

def card_index(request):
    context = {}
    cards = a_m.Card.objects.filter(active=True)
    context['cards'] = cards
    return render(request, 'anki/card_index.html', context)


def card_detail(request):
    if request.method == 'GET':
        try:
            _card = a_m.Card.objects.get(pk=request.GET['id'])
        except:
            assert False
    context = {
        'id': _card.id,
        'en_word': _card.en_word,
        'rus_word': _card.rus_word,
        'en_desc': _card.en_description,
        'rus_desc': _card.rus_description,
        }
    return JsonResponse(context)


def card_remove(request):
    if request.method == 'POST':
        try:
            _card = a_m.Card.objects.get(pk=request.POST['id'])
            _card.active = False
            _card.save()
            context = {'result': 'success'}
        except:
            context = {'result': 'error'}
    return JsonResponse(context)