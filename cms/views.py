# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.conf import settings

from django.core.mail import send_mail
from django.core.mail import EmailMessage

from django.contrib.auth import logout

#import vk_api

from cms.models import Page

# Create your views here.
'''
def index(request):
    return render(request, 'cms/index.html', {})
'''
def index(request):
    foo = 'Foo Variable '
    __user = None
    if request.GET and request.GET['logout'] == '1':
        logout(request)
    if request.user.is_authenticated:
        __user = request.user
    return render(request, 'cms/index.html', {'foo':foo, 'user':__user})

def new_tpl(request):
    if request.user.is_authenticated:
        _username = request.user.username
    else:
        _username = 'out of login'
    context = {'username': _username}
    tpl_name = 'new_tpl'
    try:
        tpl_name = request.GET['tpl']
    except:
        pass
    return render(request, f'cms/{tpl_name}.html', context)

def pages(request):
    pages = Page.objects.filter(status=3)
    return render(request, 'cms/pages.html', {'pages': pages})

def page_detail(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug, status=3)
    if page.show_for_users:
        if not request.user.username in page.show_for_users.split(';'):
            assert(False)
    foo = 'This is the local variable!!!!'
    bar = ['one', 'two', 'three']
    #~assert False
    #~return render(request, 'cms/page_detail.html', {'page': page})
    return render(request, 'cms/page_detail.html', {'page':page, 'foo':foo, 'bar':bar})


def hidden_page_detail(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    return render(request, 'cms/page_detail.html', {'page': page})
    # ~return render(request, 'cms/page_detail.html', {'page':page, 'foo':foo, 'bar':bar})

def send_mail(request):
    '''
    if request.method == 'GET':
        qd = request.GET
    elif request.method == 'POST':
        qd = request.POST

    e_mail_1 = request.GET['email']
    assert(e_mail_1=='ololo1')
    '''
    send_mail(
        'Subject here',
        'Here is the message.',
        'capt@nybble.ru',
        ['wizard@semin-club.ru'],
        #fail_silently=False,
    )

    '''
    send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, ['cadodbd1@gmail.com'])

    email = EmailMessage('Hello', 'World', to=['cadodbd1@gmail.com'])
    email.send()
    '''

    return render(request, 'cms/email.html', {'e_mail_1':e_mail_1})

def rebus(request):
    return render(request, 'cms/rebus.html', {})

def vk_friends(request):

    login, password = '+79157771188', 'olga13'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        foo = error_msg
        assert(False)

    vk = vk_session.get_api()

    responce = vk.friends.get(fields='nickname')
    return render(
        request,
        'cms/vk_friends.html',{
        'total': len(responce['items']),
        'items': responce['items']
        })


def iron_piece(request):
    context={}
    assert False
    return  render(request, 'cms/iron_piece.html', context)
