from django import template
from lists import models as list_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, room):  # templatetag call 하는 역할
    user = context.request.user
    if user.is_anonymous:
        print("어나니머스")
        return False

    the_list = list_models.List.objects.get_or_none(
        user=user, name="My Favorite Houses"
    )
    if the_list is None:
        print("좋아요없음")
        return False

    return room in the_list.rooms.all()
