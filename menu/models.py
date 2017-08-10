# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property


class MenuGroup(models.Model):
    name = models.CharField('Название меню', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __unicode__(self):
        return self.name


class Menu(models.Model):
    menu_group = models.ForeignKey(MenuGroup)
    title = models.CharField('Название пункта меню', max_length=255)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', verbose_name='Родительский пункт', null=True, blank=True)

    class Meta:
        verbose_name = 'Пункт Меню'
        verbose_name_plural = 'Пункты Меню'

    def __unicode__(self):
        return self.url

    @cached_property
    def get_url(self):
        try:
            return reverse(self.url)
        except:
            return self.url
