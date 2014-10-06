from django.template import Library
import json
register = Library()


@register.filter
def location(point, arg=None):
    if point:
        if arg == 'x':
            return json.loads(point)['coordinates'][0]
        elif arg == 'y':
            return json.loads(point)['coordinates'][1]
    else:
        return ''