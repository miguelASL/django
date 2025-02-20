from django.shortcuts import render


def simple(request):
    return render(request, 'simple.html', {})


def dinamico(request, name):
    categories = ['Python', 'Django', 'Flask', 'HTML', 'CSS', 'JavaScript']
    context = {'nombre': name, 'categorias': categories}
    return render(request, 'dinamico.html', context)
