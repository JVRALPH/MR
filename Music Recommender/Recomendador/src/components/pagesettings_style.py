import flet as ft
from flet import *

def page_settings(page):
    page.window_prevent_close = True
    page.window_width=1920
    page.window_height=1080
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.padding=10
    page.title = "Music Record"