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
        
        im = Image.open(e.files[0].path)
        width, height = im.size
        self.controls[0].content.controls[1].content.controls.pop(2)
        self.controls[0].content.controls[1].content.controls.pop(1)
        self.controls[0].content.controls[1].content.controls[2].content = ft.Container(
            ft.Column(controls=[
                ft.Container(width=364,height=1,bgcolor=WHITE),
                ft.Container(ft.Row(controls=[
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Размер',size=14,color=WHITE,text_align='center'),width=100),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Пиксель',size=14,color=WHITE,text_align='center'),width=100),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Тайл',size=14,color=WHITE,text_align='center'),width=100),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                ]),margin=ft.margin.only(bottom=-8,top=-8)),
                ft.Container(width=364,height=1,bgcolor=WHITE),
                ft.Container(ft.Row(controls=[
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Ширина',size=14,color=WHITE,text_align='center'),width=100),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text(height,size=14,color=WHITE,text_align='center'),width=100),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text(round(height/TILESIZE),size=14,color=WHITE,text_align='center'),width=100),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                ]),margin=ft.margin.only(bottom=-8,top=-8)),
                ft.Container(width=364,height=1,bgcolor=WHITE),
                ft.Container(ft.Row(controls=[
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Высота',size=14,color=WHITE,text_align='center'),width=100),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text(width,size=14,color=WHITE,text_align='center'),width=100),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text(round(width/TILESIZE),size=14,color=WHITE,text_align='center'),width=100),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                ]),margin=ft.margin.only(bottom=-8,top=-8)),
                ft.Container(width=364,height=1,bgcolor=WHITE),
            ]),margin=ft.margin.only(left=10)
        )
        self.controls[0].content.controls[0].content.controls[1].content.content = ft.InteractiveViewer(
            min_scale=0.01,
            max_scale=200,
            boundary_margin=ft.margin.all(20),
            # on_interaction_start=lambda e: print(e),
            # on_interaction_end=lambda e: print(e),
            # on_interaction_update=lambda e: print(e),
            content=ft.Image(
                src=e.files[0].path,
            ),
        )
        # self.controls[0].content.controls[0].content.controls[1].content.content = ft.Image(
        #     src=e.files[0].path,
        #     # width=100,
        #     # height=100,
        #     fit=ft.ImageFit.CONTAIN,
        # )
        print(e.files[0].path)
        self.update()


    def build(self):
        
        pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.selected_files = ft.Text(text_align='center',color=WHITE)

        self.page.overlay.append(pick_files_dialog)
        
        self.size_file = ft.Container()

        self.main_page = ft.Container(
            ft.Row(controls=[
                ft.Container(
                    ft.Row(controls=[
                            ft.Container(width=100,height=900,border=ft.border.all(1,YELLOW)),
                            ft.Container(ft.Container(
                                    
                                ),width=1100,height=900,padding=10),
                        ]),
                    width=1200,height=900,bgcolor=BLUE,margin=ft.margin.only(right=-10)),
                ft.Container(
                    ft.Column(controls=[
                        ft.Container(ft.Text('Редактор карт',size=24,color=BLUE,text_align='center'),height=50,padding=ft.padding.only(top=8),bgcolor=YELLOW,width=400),
                        ft.Container(ft.Text('Выберите изображения на фон сетки, по которому будет рисоваться карта',color=WHITE,text_align='center'),width=400,padding=10),
                        ft.Container(ft.Text('Загрузить изображение',size=16,color=BLUE,text_align='center'),on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True ),height=40,padding=ft.padding.only(top=5),bgcolor=YELLOW,width=280,margin=ft.margin.only(left=60)),
                        ft.Container(self.selected_files,width=400),
                        ft.Container(),
                    ]),
                    width=400,height=900,bgcolor=BLUE,border=ft.border.all(1,YELLOW),margin=0),
            ]),margin=-1
        )
        return self.main_page
    
    
    
    