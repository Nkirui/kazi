# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Employee, Employer

admin.site.register(Employee)
admin.site.register(Employer)
