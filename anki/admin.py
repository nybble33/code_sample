from django.contrib import admin

# Register your models here.

import anki.models as a_m


class CardAdmin(admin.ModelAdmin):
    ordering = ['en_word']


admin.site.register(a_m.Card, CardAdmin)
