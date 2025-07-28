from django.shortcuts import render
from app.models import Menu


def draw_menu(request, menu_name, submenu_path=None):
    current_path = f'{menu_name}/{submenu_path}' if submenu_path else menu_name

    menus = Menu.objects.filter(name=menu_name).select_related('parent')
    return render(
        request,
        'base.html',
        {
            'menus': menus,
            'current_path': current_path
         }
    )
# Create your views here.
