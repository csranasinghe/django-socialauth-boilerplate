from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    if request.method == 'POST':
        return render(request, "riyoapp/index.html", {})
    elif request.method == 'GET':
        return render(request, "userauth/login.html", {})

