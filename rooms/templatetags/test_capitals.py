from django import template

register = template.Library()


@register.filter
def test_capitals(value):
    print(value)
    return value.capitalize()
