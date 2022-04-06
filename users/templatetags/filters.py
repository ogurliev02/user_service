from django import template

register = template.Library()


def user_to_json(user, add_fields=None):
    result = user.__dict__
    del result['_state']
    result.update(add_fields)
    return result


register.filter('user_to_json', user_to_json)
