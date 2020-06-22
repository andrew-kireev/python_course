from django.conf.urls import url
from routing.views import simple_route
from routing.views import slug_route

urlpatterns = [
    url('^simple_route/$', simple_route),
    url('^simple_route/blabla$', simple_route),
    url('^slug_route/[0-9a-z_-]{,16}/$', slug_route)
]
