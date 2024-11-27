from variable import *
from imports import *


class Platforma(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.menu_palitra_sp = {}
        for i in os.listdir('src/tilemap/palitra'):
            self.menu_palitra_sp[i] = False
        self.menu_palitra_sp[os.listdir('src/tilemap/palitra')[0]] = True
        self.status_palitra=False
    
    
    # кнопка - загрузить изображение
    def pick_files_result(self,e: ft.FilePickerResultEvent):
        # if self.status_palitra: self.controls[0].content.controls[1].content.controls.pop()
        self.selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Не выбрано!"
        )
        # делаем сетку
        self.path_img_celka = e.files[0].path
        self.number_img_celka = e.files[0].name[:-4]
        image = Image.open(e.files[0].path)
        width, height = image.size

        step_x = width/(TILESIZE*COUNT_CHANK)# количество чанков по иксу
        step_y = height/(TILESIZE*COUNT_CHANK)# количество чанков по иксу
        with_chank_UI = WIDTH_CANVA/step_x
        height_chank_UI = (HEIGHT_CANVA)/step_y
        line_x_mas = []
        line_y_mas = []
        for i in range(1,round(step_y)+2):
            line_x_mas.clear()
            for j in range(0,round(step_x)+2):
                line_x_mas.append(ft.Container(data=[i,j],on_click=self.get_chank,height=height_chank_UI-1,width=with_chank_UI,border=ft.border.all(0.1,BLUE),margin=ft.margin.only(left=0,top=0,bottom=-10,right=-10)))
            line_y_mas.append(ft.Row(controls=line_x_mas,))
        
        # self.controls[0].content.controls[1].content.controls.pop(2)
        # self.controls[0].content.controls[1].content.controls.pop(1)
        self.controls[0].content.controls[1].content.controls[3].content = ft.Container(
            ft.Column(controls=[
                ft.Container(width=364,height=1,bgcolor=WHITE),
                ft.Container(ft.Row(controls=[
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Размер',size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Пиксель',size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Тайл',size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Чанк',size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                ]),margin=ft.margin.only(bottom=-8,top=-8)),
                ft.Container(width=364,height=1,bgcolor=WHITE),
                ft.Container(ft.Row(controls=[
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Ширина',size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text(height,size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text(round(width/TILESIZE),size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text(round(step_x),size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                ]),margin=ft.margin.only(bottom=-8,top=-8)),
                ft.Container(width=364,height=1,bgcolor=WHITE),
                ft.Container(ft.Row(controls=[
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text('Высота',size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text(width,size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text(round(height/TILESIZE),size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                    ft.Container(ft.Text(round(step_y),size=14,color=WHITE,text_align='center'),width=70),
                    ft.Container(width=1,height=20,bgcolor=WHITE),
                ]),margin=ft.margin.only(bottom=-8,top=-8)),
                ft.Container(width=364,height=1,bgcolor=WHITE),
            ]),margin=ft.margin.only(left=10)
        )
        self.controls[0].content.controls[0].content.controls[1].content.content = ft.InteractiveViewer(
            min_scale=0.01,
            max_scale=500,
            boundary_margin=ft.margin.all(20),
            content=ft.Stack([
                    ft.Image(src=e.files[0].path,height=HEIGHT_CANVA,width=WIDTH_CANVA,fit=ft.ImageFit.COVER),
                    ft.Column(controls=line_y_mas)
                ]),
        )
        self.update()

    def get_chank(self,e):
        self.controls[0].content.controls[1].content.controls.pop(3)
        # self.controls[0].content.controls[1].content.controls.append(ft.Container())
        number = (int(self.number_img_celka)-1)*9 + (e.control.data[0]-1)*3 + (e.control.data[1]+1)
        self.status_palitra = True
        # рисуем сетку
        line_x_mas = []
        line_y_mas = []
        for i in range(1,COUNT_CHANK+1):
            line_x_mas.clear()
            for j in range(1,COUNT_CHANK+1):
                line_x_mas.append(ft.Container(data=[i,j],on_click=self.click_tile,height=TILESIZE,width=TILESIZE,border=ft.border.all(0.1,BLUE),margin=ft.margin.only(left=0,top=0,bottom=0,right=-10)))
            if i==1:line_y_mas.append(ft.Container(ft.Row(controls=line_x_mas)))
            else:line_y_mas.append(ft.Container(ft.Row(controls=line_x_mas),margin=ft.margin.only(top=-11.2)))

        self.controls[0].content.controls[0].content.controls[1].content.content = ft.Container(ft.Stack([
            ft.Image(src=f'src/img/map_grid/Tile_png/{number}.png',height=HEIGHT_CANVA,width=WIDTH_CANVA,fit=ft.ImageFit.FILL),
            ft.Column(controls=line_y_mas)
        ]),height=HEIGHT_CANVA,width=WIDTH_CANVA)
        self.controls[0].content.controls[1].content.controls.append(self.palitra())
        self.update()

    def click_tile(self,e):
        print(e.control.data)

    # выбираем вкладку в меню палитры
    def change_menu_palitra(self,e):
        for i in self.menu_palitra_sp:
            if i == e.control.data: self.menu_palitra_sp[i] = True
            else: self.menu_palitra_sp[i] = False
        # print(self.controls[0].content.controls[1].content.controls)
        len_mas = len(self.controls[0].content.controls[1].content.controls)
        self.controls[0].content.controls[1].content.controls[len_mas-1] = self.palitra()
        self.update()

    # рисуем сами краски
    def dev_color(self,dev_color):
        colors_mas = []
        for i in os.listdir(f'src/tilemap/palitra/{dev_color}'):
            colors_mas.append(ft.Container(ft.Image(src=f'src/tilemap/palitra/{dev_color}/{i}',width=32,height=32),on_click=self.change_dev_color,data=[f'src/tilemap/palitra/{dev_color}/{i}',i],width=32,height=32,bgcolor=BLUE))
        
        return ft.Container(ft.Row(controls=colors_mas,wrap=True,spacing=5,run_spacing=5,),width=350,padding=10)

    def change_dev_color(self,e):
        print(e.control.data)

    # рисуем палитру
    def palitra(self):
        menu_palitra_mas = []
        for i in self.menu_palitra_sp:
            if self.menu_palitra_sp[i]:
                color_change = i
                menu_palitra_mas.append(ft.Container(ft.Text(i,size=14,color=BLUE),bgcolor=YELLOW,padding=10,margin=0))
            else:menu_palitra_mas.append(ft.Container(ft.Text(i,size=14,color=YELLOW),data=i,on_click=self.change_menu_palitra,bgcolor=BLUE,padding=10,margin=0))
        palitra = ft.Container(ft.Column(controls=[
                ft.Container(ft.Row(controls=menu_palitra_mas,wrap=True,spacing=5,run_spacing=5,),bgcolor=BLUE,width=350),
                self.dev_color(color_change)
            ]),width=350,height=620,bgcolor=WHITE,margin=ft.margin.only(left=20))
        return palitra

    def build(self):
        
        pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.selected_files = ft.Text(text_align='center',color=WHITE)

        self.page.overlay.append(pick_files_dialog)
        
        self.size_file = ft.Container()

        self.main_page = ft.Container(
            ft.Row(controls=[
                ft.Container(
                    ft.Row(controls=[
                            ft.Container(width=100,height=height_window_platforma,border=ft.border.all(1,YELLOW)),
                            ft.Container(ft.Container(
                                    
                                ),width=WIDTH_CANVA,height=HEIGHT_CANVA,padding=0,margin=ft.margin.only(left=100)),
                        ]),
                    width=1200,height=height_window_platforma,bgcolor=BLUE),
                ft.Container(
                    ft.Column(controls=[
                        ft.Container(ft.Text('Редактор карт',size=24,color=BLUE,text_align='center'),height=50,padding=ft.padding.only(top=8),bgcolor=YELLOW,width=400),
                        ft.Container(ft.Text('Выберите изображения на фон сетки, по которому будет рисоваться карта',color=WHITE,text_align='center'),width=400,padding=10),
                        ft.Container(ft.Text('Загрузить изображение',size=16,color=BLUE,text_align='center'),on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True ),height=40,padding=ft.padding.only(top=5),bgcolor=YELLOW,width=280,margin=ft.margin.only(left=60)),
                        ft.Container(self.selected_files,width=400),
                        ft.Container(),
                    ]),
                    width=400,height=height_window_platforma,bgcolor=BLUE,border=ft.border.all(1,YELLOW),margin=ft.margin.only(left=-10)),
            ]),margin=-1
        )
        return self.main_page
    
    
    
    