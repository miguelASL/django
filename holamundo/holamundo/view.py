from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola Mundo")


def despedida(request):
    return HttpResponse("Hasta luego nen")


def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("Eres menor de edad")
