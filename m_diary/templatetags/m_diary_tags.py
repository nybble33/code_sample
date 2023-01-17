# -*- coding: utf-8 -*-

from django import template
from m_diary.models import Item

register = template.Library()

@register.inclusion_tag('tags/m_diary_item_tree.html')
def items_layout(request, parent=None):
    __layout = Item.objects.filter(item=parent, user=request.user)
    return {
        'request':request,
        'items': __layout
    }
