# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Tiendita
from django.contrib import admin

# Register your models here.

#admin.site.register(Tiendita)
@admin.register(Tiendita)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'category','description', 'price')
    list_filter = ('category',)