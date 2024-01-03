import flet as ft
from flet import *

def page_settings(page):
    page.window_prevent_close = True
    page.window_width=1920
    page.window_height=1080
    page.window_min_width=680
    page.window_min_height=800
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.padding=0
    page.window_resizable = True
    page.window_center()
    page.window_to_front()
