# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def page(request):
    return render(request, 'page.html')


def sub1(request):
    return render(request, 'sub.html', {'sub': 'sub1'})


def sub2(request):
    return render(request, 'sub.html', {'sub': 'sub2'})


def sub2_1(request):
    return render(request, 'sub.html', {'sub': 'sub2_1'})


def sub2_2(request):
    return render(request, 'sub.html', {'sub': 'sub2_2'})
