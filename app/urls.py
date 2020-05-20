# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from app import views
from django.urls import path, re_path


urlpatterns = [
    # Matches any html file 
    #re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('idcard_form.html', views.idcard_form, name='idcard_form'),
    path('certificate_form.html', views.certificate_form, name='certificate_form'),
    path('reportform.html', views.reportform, name='reportform'),
    path('printreport.html', views.printreport, name='printreport'),
    path('certificate-verification.html', views.certificate_verification, name='printreport'),
    path('idcard-print.html', views.printreport, name='printreport'),
    path('idcard-print.html', views.printreport, name='printreport'),

]
