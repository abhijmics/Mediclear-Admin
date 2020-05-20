# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from app.models import idcard,Certificate,Report
from import_export.admin import ImportExportModelAdmin
# Register your models here.
#admin.site.register(idcard)
@admin.register(idcard)

class idc(ImportExportModelAdmin):
    pass

@admin.register(Certificate)

class cert(ImportExportModelAdmin):
    pass

@admin.register(Report)

class reg(ImportExportModelAdmin):
    pass