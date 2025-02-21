from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def porfolio(request):
    return render(request, 'portfolio.html', {})
