from django import template

register = template.Library()


def perfect_view(value):
    result = value.__dict__
    del result['_state']
    return result


register.filter('perfect_view', perfect_view)
