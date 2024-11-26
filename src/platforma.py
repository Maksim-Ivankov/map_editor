from variable import *
from imports import *


class Platforma(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
    
    
    def pick_files_result(self,e: ft.FilePickerResultEvent):
        self.selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Не выбрано!"
        )
        self.selected_files.update()

    def build(self):
        
        pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.selected_files = ft.Text(text_align='center',color=WHITE)

        self.page.overlay.append(pick_files_dialog)

        self.main_page = ft.Container(
            ft.Row(controls=[
                ft.Container(width=1200,height=900,bgcolor=BLUE,margin=ft.margin.only(right=-10)),
                ft.Container(
                    ft.Column(controls=[
                        ft.Container(ft.Text('Редактор карт',size=24,color=BLUE,text_align='center'),height=50,padding=ft.padding.only(top=8),bgcolor=YELLOW,width=400),
                        ft.Container(ft.Text('Выберите изображения на фон сетки, по которому будет рисоваться карта',color=WHITE,text_align='center'),width=400,padding=10),
                        ft.Container(ft.Text('Загрузить изображение',size=16,color=BLUE,text_align='center'),on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True ),height=40,padding=ft.padding.only(top=5),bgcolor=YELLOW,width=280,margin=ft.margin.only(left=60)),
                        ft.Container(self.selected_files,width=400),
                    ]),
                    width=400,height=900,bgcolor=BLUE,border=ft.border.all(1,YELLOW),margin=0),
            ]),margin=-1
        )
        return self.main_page
    
    
    
    