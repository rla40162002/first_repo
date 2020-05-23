from django import template
from lists import models as list_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, room):  # templatetag call 하는 역할
    user = context.request.user
    the_list = list_models.List.objects.get_or_none(
        user=user, name="My Favorite Houses"
    )
    # 이것 또한 리스트가 한 개 더 있다면 에러가 나옴

    return room in the_list.rooms.all()  # the_list안에 해당 room 있는지 없는지 확인
