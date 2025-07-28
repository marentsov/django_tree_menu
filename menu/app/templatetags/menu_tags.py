from django import template
from app.models import Menu
from django.utils.safestring import mark_safe

register = template.Library()

def get_menu(menus):
    html = '<ul>'
    for menu in menus:
        html += '<li>'
        if menu.url:
            html += f'<a href="{menu.url}">{menu.name}</a>'
        elif menu.named_url:
            html += f'<a href="{menu.named_url}">{menu.name}</a>'
        else:
            html += menu.name
        if menu.children.exists():
            html += get_menu(menu.children.all())
        html += '</li>'
    html += '</ul>'
    return html


@register.simple_tag
def draw_menu(menu_name):
    menus = Menu.objects.filter(name=menu_name).select_related('parent')
    return mark_safe(get_menu(menus)) # mark_safe отключает экранирование


