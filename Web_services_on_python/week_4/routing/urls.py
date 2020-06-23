from django.conf.urls import url
from routing.views import simple_route
from routing.views import slug_route
from routing.views import sum_route
from routing.views import sum_get_method
from routing.views import sum_post_method



urlpatterns = [
    url('^simple_route/$', simple_route),
    url('^slug_route/[0-9a-z_-]{,16}/$', slug_route),
    url('^sum_route/([-\d])+/([-\d]+)/$', sum_route),
    url(r'^sum_get_method/$', sum_get_method),
    url(r'^sum_post_method/$', sum_post_method)
]
