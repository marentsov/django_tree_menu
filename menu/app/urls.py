from django.urls import path
from app import views



urlpatterns = [
    path('<str:menu_name>/', views.draw_menu, name='draw_menu'),
    path('<str:menu_name>/<path:submenu_path>/', views.draw_menu, name='draw_submenu'),
]
