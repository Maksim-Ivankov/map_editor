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
        self.changed_color = []
        self.flag_hover = False
        self.flag_hover_back = False
        self.mas_hover = []
    
    
    # кнопка - загрузить изображение
    def pick_files_result(self,e: ft.FilePickerResultEvent):
        if self.status_palitra: self.controls[0].content.controls[1].content.controls[4].content = ft.Container()
        self.selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Не выбрано!"
        )
        # делаем сетку
        self.path_img_celka = e.files[0].path
        self.e_files_0 = e.files[0]
        self.print_step_2()
        
    # отрисовка загруженной картинки
    def print_step_2(self):
        self.number_img_celka = self.e_files_0.name[:-4]
        image = Image.open(self.e_files_0.path)
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
                    ft.Image(src=self.path_img_celka,height=HEIGHT_CANVA,width=WIDTH_CANVA,fit=ft.ImageFit.COVER),
                    ft.Column(controls=line_y_mas)
                ]),
        )
        self.update()

    # выбор чанка в общей картинке
    def get_chank(self,e):
        self.controls[0].content.controls[1].content.controls[3].content = ft.Container()
        # self.controls[0].content.controls[1].content.controls.append(ft.Container())
        number = (int(self.number_img_celka)-1)*9 + (e.control.data[0]-1)*3 + (e.control.data[1]+1)
        self.status_palitra = True
        self.number_chank = number
        self.print_chank()
        

    # отрисовка чанка
    def print_chank(self):
        # получили файл с картой чанка
        with open(f'src/map/chank/{self.number_chank}.txt') as f:
            mas_map = ast.literal_eval(f.readline())
        # рисуем сетку
        line_x_mas = []
        line_y_mas = []
        for i in range(1,COUNT_CHANK+1):
            line_x_mas.clear()
            for j in range(1,COUNT_CHANK+1):
                if mas_map[i-1][j-1] == 0: line_x_mas.append(ft.Container(data=[i,j],on_hover=self.hover_tile,on_click=self.click_end_tile,on_tap_down=self.click_start_tile,height=TILESIZE,width=TILESIZE,border=ft.border.all(0.1,BLUE)))
                else: line_x_mas.append(ft.Container(ft.Image(src=f'src/tilemap/all/{mas_map[i-1][j-1]}.png',width=32,height=32),data=[i,j],on_hover=self.hover_tile,on_click=self.click_end_tile,on_tap_down=self.click_start_tile,height=TILESIZE,width=TILESIZE,border=ft.border.all(0.1,BLUE)))
            if i==1:line_y_mas.append(ft.Container(ft.Row(controls=line_x_mas,spacing=0,run_spacing=0,)))
            else:line_y_mas.append(ft.Container(ft.Row(controls=line_x_mas,spacing=0,run_spacing=0,)))
        self.controls[0].content.controls[0].content.controls[1].content.content = ft.Container(ft.Stack([
            ft.Image(src=f'src/img/map_grid/Tile_png/{self.number_chank}.png',height=HEIGHT_CANVA,width=WIDTH_CANVA,fit=ft.ImageFit.FILL),
            ft.Column(controls=line_y_mas,spacing=0,run_spacing=0,)
        ]),height=HEIGHT_CANVA,width=WIDTH_CANVA)
        self.controls[0].content.controls[1].content.controls[4].content = self.palitra()
        self.update()

    # клик начало по тайлу
    def click_start_tile(self,e):
        if self.changed_color: 
            if e.control.content: 
                now_img = e.control.content
                e.control.content = ft.Stack([
                    now_img,
                    ft.Image(src=self.changed_color[0],width=32,height=32)
                ])
            else: e.control.content = ft.Image(src=self.changed_color[0],width=32,height=32)
            # сохраняем в карту
            with open(f'src/map/chank/{self.number_chank}.txt') as f:
                mas_map = ast.literal_eval(f.readline())
            mas_map[e.control.data[0]-1][e.control.data[1]-1] = int(self.changed_color[1][:-4])
            my_file = open(f'src/map/chank/{self.number_chank}.txt', "w+")
            my_file.write(f'{str(mas_map)}')
            my_file.close()
        self.update()
        self.flag_hover = True
        if self.flag_hover_back:
            with open(f'src/map/chank/{self.number_chank}.txt') as f:
                mas_map = ast.literal_eval(f.readline())
            for i in self.mas_hover:
                # # сохраняем в карту
                mas_map[i[0]-1][i[1]-1] = int(i[2])
            mas_map[e.control.data[0]-1][e.control.data[1]-1] = int(self.changed_color[1][:-4])
            my_file = open(f'src/map/chank/{self.number_chank}.txt', "w+")
            my_file.write(f'{str(mas_map)}')
            my_file.close()
            self.mas_hover[:] = []
            self.flag_hover_back = False
            
        
        
    # клик окончание по тайлу
    def click_end_tile(self,e):
        self.flag_hover = False
    
    # наведение на тайл
    def hover_tile(self,e):
        if self.flag_hover: 
            self.flag_hover_back = True
            if e.control.content: 
                now_img = e.control.content
                e.control.content = ft.Stack([
                    now_img,
                    ft.Image(src=self.changed_color[0],width=32,height=32)
                ])
            else: e.control.content = ft.Image(src=self.changed_color[0],width=32,height=32)
            # Сохраняем в массив, что построили в режиме ховера
            self.mas_hover.append([e.control.data[0],e.control.data[1],self.changed_color[1][:-4]])
            self.update()
    
    # залить все нули выделенным цветом
    def fill_zero(self,e):
        if self.changed_color: 
            with open(f'src/map/chank/{self.number_chank}.txt') as f:
                mas_map = ast.literal_eval(f.readline())
            for i in range(0,COUNT_CHANK):
                for j in range(0,COUNT_CHANK):
                    if mas_map[i][j] == 0:
                        mas_map[i][j] = int(self.changed_color[1][:-4])
            my_file = open(f'src/map/chank/{self.number_chank}.txt', "w+")
            my_file.write(f'{str(mas_map)}')
            my_file.close()
            # print(f'Заливка цветом {int(self.changed_color[1][:-4])} выполнена')
            self.print_chank()
            self.update()
        # else: print('Сначала выберите чем залить нули')

    # выбираем вкладку в меню палитры
    def change_menu_palitra(self,e):
        for i in self.menu_palitra_sp:
            if i == e.control.data: self.menu_palitra_sp[i] = True
            else: self.menu_palitra_sp[i] = False
        self.controls[0].content.controls[1].content.controls[4].content = self.palitra()
        self.update()

    # рисуем сами краски
    def dev_color(self,dev_color):
        colors_mas = []
        for i in os.listdir(f'src/tilemap/palitra/{dev_color}'):
            colors_mas.append(ft.Container(ft.Image(src=f'src/tilemap/palitra/{dev_color}/{i}',width=32,height=32),on_click=self.change_dev_color,data=[f'src/tilemap/palitra/{dev_color}/{i}',i],width=32,height=32,bgcolor=BLUE))
        return ft.Container(ft.Row(controls=colors_mas,wrap=True,spacing=5,run_spacing=5,),width=350,padding=10)

    def change_dev_color(self,e):
        # print(e.control.data)
        self.changed_color = e.control.data
        self.controls[0].content.controls[0].content.controls[0].content.controls[0].content = ft.Image(src=e.control.data[0],width=32,height=32)
        self.update()

    # Кнопка назад
    def btn_back(self,e):
        self.print_step_2()

    # рисуем палитру
    def palitra(self):
        # добавляем кнопку назад
        self.controls[0].content.controls[1].content.controls[2] = ft.Container(ft.Row(controls=[
            ft.Container(ft.Text('Назад',size=16,color=BLUE,text_align='center'),on_click=self.btn_back,height=40,padding=ft.padding.only(top=5),bgcolor=YELLOW,width=100,margin=ft.margin.only(left=0)),
            ft.Container(ft.Text('Загрузить изображение',size=16,color=BLUE,text_align='center'),on_click=lambda _: self.pick_files_dialog.pick_files(allow_multiple=True ),height=40,padding=ft.padding.only(top=5),bgcolor=YELLOW,width=220,margin=ft.margin.only(left=0)),
        ]),margin=ft.margin.only(left=28))
        self.update()
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
        
        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.selected_files = ft.Text(text_align='center',color=WHITE)
        self.page.overlay.append(self.pick_files_dialog)

        self.main_page = ft.Container(
            ft.Row(controls=[
                ft.Container(
                    ft.Row(controls=[
                            ft.Container(ft.Column(controls=[
                                    ft.Container(width=32,height=32,border=ft.border.all(1,YELLOW),margin=ft.margin.only(left=34,top=34)), # что сейчас выбрано
                                    ft.Container(ft.Image(src='src/img/img/1.png',height=32,width=32,fit=ft.ImageFit.COVER),on_click=self.fill_zero,width=32,height=32,margin=ft.margin.only(left=34,top=20))# залить все нули в выбранный цвет
                                ]),width=100,height=height_window_platforma,border=ft.border.all(1,YELLOW)),
                            ft.Container(ft.Container(
                                    
                                ),width=WIDTH_CANVA,height=HEIGHT_CANVA,padding=0,margin=ft.margin.only(left=100)),
                        ]),
                    width=1200,height=height_window_platforma,bgcolor=BLUE),
                ft.Container(
                    ft.Column(controls=[
                        ft.Container(ft.Text('Редактор карт',size=24,color=BLUE,text_align='center'),height=50,padding=ft.padding.only(top=8),bgcolor=YELLOW,width=400),
                        ft.Container(ft.Text('Выберите изображения на фон сетки, по которому будет рисоваться карта',color=WHITE,text_align='center'),width=400,padding=10),
                        ft.Container(ft.Text('Загрузить изображение',size=16,color=BLUE,text_align='center'),on_click=lambda _: self.pick_files_dialog.pick_files(allow_multiple=True ),height=40,padding=ft.padding.only(top=5),bgcolor=YELLOW,width=280,margin=ft.margin.only(left=60)),
                        ft.Container(self.selected_files,width=400),
                        ft.Container(),
                    ]),
                    width=400,height=height_window_platforma,bgcolor=BLUE,border=ft.border.all(1,YELLOW),margin=ft.margin.only(left=-10)),
            ]),margin=-1
        )
        return self.main_page
    
    
    
    