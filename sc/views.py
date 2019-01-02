# -*- coding: utf-8 -*-


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from models import *


def index(request):
    return render_to_response('index.html', locals())


def settings(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        key = request.GET.get('key', '')
        s = get_object_or_404(SettingScript, name=name)
        if s.key_list and key not in s.key_list:
            return HttpResponseBadRequest('Invalid key! Check SETTINGS_CLOUD_KEY in environment!')
        return HttpResponse(s.content)

    else:

        name = request.POST.get('name', '')
        key = request.POST.get('key', '')
        language = request.POST.get('language', '')
        content = request.POST.get('content', '')

        if not name:
            return HttpResponseBadRequest('miss name')

        if not content:
            return HttpResponseBadRequest('miss content')

        s, created = SettingScript.objects.get_or_create(name=name)

        if created:
            s.keys = key
        else:
            if s.key_list and key not in s.key_list:
                return HttpResponseBadRequest('invalid key')

        s.language = language
        s.content = content
        s.save()

        return HttpResponse('saved')







