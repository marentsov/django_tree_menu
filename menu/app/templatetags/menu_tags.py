from django import template
from app.models import Menu
from django.utils.safestring import mark_safe

register = template.Library()

def get_menu(menus, current_path=None):
    html = '<ul>'
    for menu in menus:
        # проверка активен ли текущий пункт меню
        is_active = False
        if current_path:
            menu_url = menu.url.strip('/')
            current = current_path.strip('/')
            is_active = menu_url == current

        active_class = ' class="active' if is_active else ''

        html += f'<li{active_class}>'
        if menu.url:
            html += f'<a href="{menu.url}">{menu.name}</a>'
        elif menu.named_url:
            html += f'<a href="{menu.named_url}">{menu.name}</a>'
        else:
            html += menu.name
        if menu.children.exists():
            html += get_menu(menu.children.all(), current_path)
        html += '</li>'
    html += '</ul>'
    return html

@register.simple_tag
def draw_menu(menu_name, current_path=None):
    menus = Menu.objects.filter(name=menu_name).select_related('parent').prefetch_related('children')
    return mark_safe(get_menu(menus, current_path)) # mark_safe отключает экранирование



