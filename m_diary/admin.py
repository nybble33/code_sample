# -*- coding:utf-8 -*-

from django.contrib import admin
from m_diary.models import Item


class ItemAdmin(admin.ModelAdmin):
    ordering = ['-created']
    list_display = ('id', 'title', 'd_item', 'user', 'created', 'finished')
    list_editable = ('d_item', 'finished')
    fields = (
        'd_item',
        'title',
        'user',
        'slug',
        'item_type',
        'short_description',
        'content',
        'created',
        'start_date',
        'deadline',
        'in_work',
        'finished',
        )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def __unicode__(self):
        return self.title

admin.site.register(Item, ItemAdmin)
