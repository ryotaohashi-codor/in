from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

import requests
import json


from . import forms


def logout_user(request):
    logout(request)
    return redirect('login')

@csrf_exempt
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        user = authenticate(
                username=request.POST['username'],
                password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse('ログインしました')
    return render(request, 'registration/login.html', context={'form': form, 'message': 'ログインしていません'})

def abc(request):
    return HttpResponse('ログインに成功しました')

def hook(request):
    SLACK_WEBHOOK = "https://hooks.slack.com/services/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"

    payload_dic = {
        "text": "新しいメールが届きました",
        "username": "sample",
        "channel": "#general",
    }

    r = requests.post(SLACK_WEBHOOK, data=json.dumps(payload_dic))
    return HttpResponse(r)

def hook2(request):
    SLACK_WEBHOOK = "https://hooks.slack.com/services/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"

    payload_dic = {
        "text": "新しいメールが届きました",
        "username": "same",
        "channel": "#general",
    }

    r = requests.post(SLACK_WEBHOOK, data=json.dumps(payload_dic))
    return HttpResponse(r)

@csrf_exempt
def inv(request):
    if request.method == 'POST':
        print('aaaaa')
        return HttpResponse('a')
    else:
        return HttpResponse('b')