# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Gato

# Create your views here.

def gato(request):
    gatos = Gato.objects.order_by('id')
    template = loader.get_template('gato.html')
    title = 'Los gatos son cool'
    context = {
        'gatos': gatos,
        'title': title
    }
    return HttpResponse(template.render(context, request))

def saludo(request):
    template = loader.get_template('saludo.html')
    big_title = 'Encabezado de la página'
    title = 'Aquí no hay gatos'
    hola = {
        'big_title' : big_title,
        'title' : title
    }
    return HttpResponse(template.render(hola, request))