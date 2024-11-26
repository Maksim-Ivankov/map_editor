from variable import *
from imports import *

from src.platforma import Platforma

class Main:
    def __init__(self):
        None

#111

    def run(self, page):
        self.page: ft.Page = page
        self.page.title = "Редактор карт"
        self.page.padding=0
        self.page.theme_mode = "light" 
            

        # self.page.window_full_screen = True # на весь экран
        self.page.window_height, self.page.window_width = height_window_platforma, width_window_platforma
        self.main_print = ft.Container( 
           content = Platforma(self),
           expand = True,
        #    padding=ft.padding.only(bottom=-10)
        )
        self.page.add(self.main_print)



main = Main()
ft.app(target=Main().run, assets_dir="assets")

























































