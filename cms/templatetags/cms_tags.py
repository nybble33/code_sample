# -*- coding: utf-8 -*-

from django import template
from cms.models import MenuItem

register = template.Library()

@register.inclusion_tag('tags/test.html')
def test(some_arg):
    if some_arg:
        answer = some_arg
    else:
        answer = 'Holy shit'
    return {
        'answer': answer
    }

@register.inclusion_tag('tags/test1.html')
def test1(some_arg):
    if some_arg:
        answer = some_arg
    else:
        answer = 'Holy shit Test1'
    return {
        'answer': answer
    }

@register.inclusion_tag('tags/menu.html')
def n_menu(request, _parent=None):
    __menu_layout = MenuItem.objects.filter(
        parent=_parent).order_by('order',)

    return {'items': __menu_layout}
