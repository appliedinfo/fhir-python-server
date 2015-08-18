# -- encoding: utf-8 --

# Copyright 2014 Applied Informatics Inc.
# @author  Nickolas Whiting  <nickolas@trialx.com>

"""fhir_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from api.views import PatientView, PatientSearch

urlpatterns = [
    url('^Patient/(?P<id>[0-9]+)', PatientView.as_view(), name='patient'),
    url('^Patient', PatientSearch.as_view(), name='patient_search'),
]
