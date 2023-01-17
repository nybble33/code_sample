from django.db import models

# Create your models here.


class Card(models.Model):
    en_word = models.CharField('english word', max_length=255)
    rus_word = models.CharField('russian word', max_length=255)
    en_description = models.TextField('english description', blank=True, null=True)
    rus_description = models.TextField('russian description', blank=True, null=True)
    active = models.BooleanField('active', default=True)

    class Meta:
        ordering = ['en_word']
        verbose_name = 'word'
        verbose_name_plural = 'words'

    def __str__(self):
        return f'{self.en_word}-{self.rus_word}'
