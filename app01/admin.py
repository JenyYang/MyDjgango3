# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
import models

admin.site.register(models.Author)
admin.site.register(models.Publish)
admin.site.register(models.Book)