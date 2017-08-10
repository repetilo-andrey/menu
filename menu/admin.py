# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from menu.models import MenuGroup, Menu


class MenuAdminInline(admin.TabularInline):
    model = Menu
    extra = 1


class MenuGroupAdmin(admin.ModelAdmin):
    inlines = [MenuAdminInline]


admin.site.register(MenuGroup, MenuGroupAdmin)
