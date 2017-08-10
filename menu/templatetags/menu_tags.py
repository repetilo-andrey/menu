from django import template

from menu.models import Menu


register = template.Library()


@register.inclusion_tag('inc/menu.html', takes_context=True)
def draw_menu(context, menu_group_name):
    request = context.get('request')
    items_all = Menu.objects.select_related('parent').filter(menu_group__name=menu_group_name)
    current_url = request.path
    items = []
    for item in items_all:
        children = []
        for i in items_all:
            if i.parent == item:
                children.append(i)
        setattr(item, 'children', children)
        if not item.parent:
            items.append(item)
    return {'items': items, 'current_url': current_url}
