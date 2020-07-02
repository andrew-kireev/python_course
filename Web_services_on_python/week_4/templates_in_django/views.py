from django.shortcuts import render
from django import template
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.

register = template.Library()


def echo(request):

    if 'HTTP_X_PRINT_STATEMENT' in request.META:
        head = request.META['HTTP_X_PRINT_STATEMENT']
    else:
        head = 'empty'

    return render(request, 'echo.html', context={
        'a' : request.GET.get('a', None),
        'b': request.GET.get('b', None),
        'c': request.GET.get('c', None),
        'd': request.GET.get('d', None),
        'method_name' : request.method,
        'head' : head
    })


@register.filter
def lower(value):
    return value.lower()



def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
