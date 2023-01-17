# -*- coding: utf-8 -*-
from django.db import models
import datetime

# Create your models here.


class Page(models.Model):
    STATUS_CHOICES = (
        (1, 'В разработке'),
        (2, 'Требует утверждения'),
        (3, 'Публиковать'),
        (4, 'В архиве'),
    )
    CONTENT_TYPE_CHOICES = (
        (0, 'простой текст'),
        (1, 'html'),
    )
    CATEGORY_CHOICES = (
        (0, 'обычная страница'),
        (1, 'страница блога'),
        (2, 'новость'),
        (3, 'статья'),
    )
    title = models.CharField(max_length=255, verbose_name='заголовок')
    slug = models.SlugField(verbose_name='псевдоним', unique=True)
    collection = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='подборка материалов'
        )
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    content = models.TextField(verbose_name='содержимое')
    html_content = models.TextField()
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=3,
        verbose_name='статус'
        )
    content_type = models.IntegerField(
        choices=CONTENT_TYPE_CHOICES,
        default=1,
        verbose_name='тип содержимого'
        )
    category_type = models.IntegerField(
        choices=CATEGORY_CHOICES,
        default=0,
        verbose_name='категория'
        )
    show_for_users = models.CharField(
        'показывать пользователям',
        max_length=255,
        null=True,
        blank=True
        )
    created = models.DateTimeField(
        'дата создания',
        default=datetime.datetime.now
        )
    modified = models.DateTimeField(
        'дата изменения',
        default=datetime.datetime.now
        )

    def __url_prefix(self):
        prefixes = ['page', 'article', 'news']
        return f'/{prefixes[self.category_type]}/'

    def url(self):
        return self.__url_prefix()+self.slug

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'страница'
        verbose_name = 'страницы'


class MenuItem(models.Model):
    order = models.IntegerField('порядок', default=10)
    title = models.TextField('название', max_length=50)
    slug = models.SlugField('псевдоним', max_length=50)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='родительский элемент'
        )
    url = models.TextField('адрес', max_length=100, blank=True, null=True)
    active = models.BooleanField('активен', default=True)

    def childs(self):
        __childs = MenuItem.objects.filter(parent=self).order_by('order')
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

    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'пункты меню'
