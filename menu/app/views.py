from django.shortcuts import render
from app.models import Menu


def draw_menu(request, menu_name):
    menus = Menu.objects.filter(name=menu_name).select_related('parent')
    return render(
        request,
        'base.html',
        {'menus': menus}
    )
# Create your views here.
