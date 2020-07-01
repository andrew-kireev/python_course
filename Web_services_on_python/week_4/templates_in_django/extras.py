from django import template

register = template.Library()

@register.filter
def inc(to_inc, how_inc):
    return str(int(to_inc) + int(how_inc))


@register.simple_tag
def division(to_del, on_what, to_int=False):
    if to_int == False:
        return str(float(to_del) / float(on_what))
    else:
        return str(int(int(to_del) / int(on_what)))




# print(division(10,3))