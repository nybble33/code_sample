from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from m_diary.models import Item

# Create your views here.

@login_required
def diary_index(request):
    items = Item.objects.filter(user=request.user, item=None)
    foo = request.headers['User-Agent']
    context = {
            'items':items,
            #'user_agent': foo,
            'some_local': 'Psh psh',
            }
    #~assert(False)
    return render(request, 'm_diary/m_diary_index.html', context)
