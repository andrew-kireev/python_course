from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def simple_route(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    if request.method == 'POST':
        return HttpResponse(status=405)


@require_http_methods('GET')
def slug_route(request):
    try:
        uri = str(request.get_raw_uri())
        return HttpResponse(content=uri.split('/')[-2])
    except:
        return HttpResponse(status=404)

@require_http_methods('GET')
def sum_route(request, a, b):
    try:
        # arg = str(request.url).split('/')
        # a = int(arg[-2])
        # b = int(arg[-3])
        # return HttpResponse(str(a + b))
        return HttpResponse(str(int(a) + int(b)))
    except:
        HttpResponse(status=404)


@require_http_methods('GET')
def sum_get_method(request):
    # print('zahli')
    try:
        a = request.GET['a']
        b = request.GET['b']
        return HttpResponse(str(int(a) + int(b)))
    except:
        return HttpResponse(status=400)

@require_POST
def sum_post_method(request):
    try:
        return HttpResponse(content=int(request.POST.get('a')) + int(request.POST.get('b')), status=200)
    except:
        # print('op')
        return HttpResponse(status=200)


