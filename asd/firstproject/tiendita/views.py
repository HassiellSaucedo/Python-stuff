# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Tiendita
# Create your views here.



def hello_world(request):
    product = Tiendita.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'product': product
    }

    return HttpResponse(template.render(context, request))
   #return render(request, 'index.html')