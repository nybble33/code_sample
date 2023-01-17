from django.db import models
import datetime
#from django_currentuser.db.models import CurrentUserField
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    ITEM_TYPE_CHOICES = (
        (1, 'заметка'),
        (2, 'задача'),
        (3, 'проект'),
        )
    d_item = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        #blank=True,
        #null=True,
        verbose_name='родительская запись'
        )
    slug = models.SlugField(verbose_name='псевдоним', unique=True)
    title = models.CharField(max_length=255, verbose_name='заголовок')
    user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
        verbose_name='создатель'
        )
    item_type = models.IntegerField(
        choices=ITEM_TYPE_CHOICES,
        default=1,
        verbose_name='тип записи'
        )
    short_description = models.CharField(
        max_length=255,
        verbose_name='краткое описание'
        )
    content = models.TextField(verbose_name='описание')
    created = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name='дата создания'
        )
    start_date = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name='дата начала'
        )
    deadline = models.DateTimeField(
        blank=True,
        verbose_name='дедлайн'
        )
    in_work = models.BooleanField(default=True, verbose_name='в работе')
    finished = models.BooleanField(default=False, verbose_name='завершено')

    def childs(self):
        __childs = Item.objects.filter(item=self, user=self.user)
        if not __childs:
            return ''
        else:
            __responce = '<ul>'
            for __child in __childs:
                __responce += '<li>' + __child.title + '</li>'
                if __child.childs():
                    __responce += __child.childs()
            __responce+= '</ul>'
            return __responce

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self):
        super(Item, self).save()

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'записи'
        verbose_name = 'запись'
