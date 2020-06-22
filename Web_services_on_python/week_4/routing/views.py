from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
# Create your tests here.

def simple_route(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    if request.method == 'POST':
        return HttpResponse(status=405)


@require_http_methods('GET')
def slug_route(request, text):
    try:
        return HttpResponse(text)
    except:
        return HttpResponse(status=404)
