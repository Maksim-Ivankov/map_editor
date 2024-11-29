from variable import *
from imports import *

from src.UI.input import Input

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
        self.number_chank = str(CHANK_START)
        for j in range(0,len(MAP_CHANK)):
                for i in range(0,len(MAP_CHANK[0])):
                    if CHANK_START == MAP_CHANK[j][i]:
                        # print(f'{j} - {i}')
                        pos_ugol_chank = [j,i]
                        break
        self.coords_1 = [MAP_CHANK[pos_ugol_chank[0]][pos_ugol_chank[1]],pos_ugol_chank[0],pos_ugol_chank[1]]
        self.coords_2 = [MAP_CHANK[pos_ugol_chank[0]][pos_ugol_chank[1]+1],pos_ugol_chank[0],(pos_ugol_chank[1]+1)]
        self.coords_3 = [MAP_CHANK[pos_ugol_chank[0]+1][pos_ugol_chank[1]],(pos_ugol_chank[0]+1),pos_ugol_chank[1]]
        self.coords_4 = [MAP_CHANK[pos_ugol_chank[0]+1][pos_ugol_chank[1]+1],(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)]
        print(f'{self.coords_1[0]}|{self.coords_2[0]}|{self.coords_3[0]}|{self.coords_4[0]}')
        

    # отрисовка чанка
    def print_chank(self,regime='defolt'):
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
        if regime == 'defolt':
            self.controls[0].content.controls[0].content.controls[1].content.content = ft.Container(ft.Stack([
                ft.Image(src=f'src/img/map_grid/Tile_png/{self.number_chank}.png',height=HEIGHT_CANVA,width=WIDTH_CANVA,fit=ft.ImageFit.FILL),
                ft.Column(controls=line_y_mas,spacing=0,run_spacing=0,)
            ]),height=HEIGHT_CANVA,width=WIDTH_CANVA)
            self.update()
        elif regime=='print':
            return ft.Container(ft.Stack([
                ft.Image(src=f'src/img/map_grid/Tile_png/{self.number_chank}.png',height=HEIGHT_CANVA,width=WIDTH_CANVA,fit=ft.ImageFit.FILL),
                ft.Column(controls=line_y_mas,spacing=0,run_spacing=0,)
            ]),height=HEIGHT_CANVA,width=WIDTH_CANVA)
            

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
    
    # # залить все нули выделенным цветом
    def fill_zero(self,e):
        print('Типа залили')
    #     if self.changed_color: 
    #         with open(f'src/map/chank/{self.number_chank}.txt') as f:
    #             mas_map = ast.literal_eval(f.readline())
    #         for i in range(0,COUNT_CHANK):
    #             for j in range(0,COUNT_CHANK):
    #                 if mas_map[i][j] == 0:
    #                     mas_map[i][j] = int(self.changed_color[1][:-4])
    #         my_file = open(f'src/map/chank/{self.number_chank}.txt', "w+")
    #         my_file.write(f'{str(mas_map)}')
    #         my_file.close()
    #         # print(f'Заливка цветом {int(self.changed_color[1][:-4])} выполнена')
    #         self.print_chank()
    #         self.update()
    #     # else: print('Сначала выберите чем залить нули')

    # выбираем вкладку в меню палитры
    def change_menu_palitra(self,e):
        for i in self.menu_palitra_sp:
            if i == e.control.data: self.menu_palitra_sp[i] = True
            else: self.menu_palitra_sp[i] = False
        self.controls[0].content.controls[1].content.controls[3].content = self.palitra()
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

    # обработчик инпута выбора чанка
    def input_num_chank(self,e):
        # print(e.control.value)
        if e.control.value:
            for j in range(0,len(MAP_CHANK)):
                for i in range(0,len(MAP_CHANK[0])):
                    if int(e.control.value) == MAP_CHANK[j][i]:
                        # print(f'{j} - {i}')
                        pos_ugol_chank = [j,i]
                        break
            self.coords_1 = [MAP_CHANK[pos_ugol_chank[0]][pos_ugol_chank[1]],pos_ugol_chank[0],pos_ugol_chank[1]]
            self.coords_2 = [MAP_CHANK[pos_ugol_chank[0]][pos_ugol_chank[1]+1],pos_ugol_chank[0],(pos_ugol_chank[1]+1)]
            self.coords_3 = [MAP_CHANK[pos_ugol_chank[0]+1][pos_ugol_chank[1]],(pos_ugol_chank[0]+1),pos_ugol_chank[1]]
            self.coords_4 = [MAP_CHANK[pos_ugol_chank[0]+1][pos_ugol_chank[1]+1],(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)]
            print(f'{self.coords_1[0]}|{self.coords_2[0]}|{self.coords_3[0]}|{self.coords_4[0]}')
            # если целая часть всех чисел равно, то это один и тот же чанк. Просто отрисуем его.
            if int(self.coords_1[0]) == int(self.coords_2[0]) and int(self.coords_1[0]) == int(self.coords_3[0]) and int(self.coords_1[0]) == int(self.coords_4[0]):
                self.number_chank = self.coords_1[0]
                self.print_chank()
       
       
    # отрисовка четвертинок чанка
    def print_chank_chetvert(self,cords):
            
        # # получили файл с картой чанка
        # with open(f'src/map/chank/{self.number_chank}.txt') as f:
        #     mas_map = ast.literal_eval(f.readline())
        # # рисуем сетку
        # line_x_mas = []
        # line_y_mas = []
        # for i in range(1,COUNT_CHANK+1):
        #     line_x_mas.clear()
        #     for j in range(1,COUNT_CHANK+1):
        #         if mas_map[i-1][j-1] == 0: line_x_mas.append(ft.Container(data=[i,j],on_hover=self.hover_tile,on_click=self.click_end_tile,on_tap_down=self.click_start_tile,height=TILESIZE,width=TILESIZE,border=ft.border.all(0.1,BLUE)))
        #         else: line_x_mas.append(ft.Container(ft.Image(src=f'src/tilemap/all/{mas_map[i-1][j-1]}.png',width=32,height=32),data=[i,j],on_hover=self.hover_tile,on_click=self.click_end_tile,on_tap_down=self.click_start_tile,height=TILESIZE,width=TILESIZE,border=ft.border.all(0.1,BLUE)))
        #     if i==1:line_y_mas.append(ft.Container(ft.Row(controls=line_x_mas,spacing=0,run_spacing=0,)))
        #     else:line_y_mas.append(ft.Container(ft.Row(controls=line_x_mas,spacing=0,run_spacing=0,)))
        self.controls[0].content.controls[0].content.controls[1].content.content = ft.Container(ft.Stack([
            ft.Container(ft.Row(controls=[
                ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[0]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[1]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[2]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[3]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
            ],wrap=True,spacing=0,run_spacing=0)),
            # ft.Container(ft.Row(controls=[
            #     ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[2]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
            #     ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[3]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
            # ])),
            # ft.Column(controls=line_y_mas,spacing=0,run_spacing=0,)
        ]),height=HEIGHT_CANVA,width=WIDTH_CANVA)
        self.update()
       
        
    def offset_btn(self,e):
        if e.control.data == 'right':
            a1 = MAP_CHANK[(self.coords_1[1])][(self.coords_1[2]+1)] # получили номер четвертины чанка
            a2 = MAP_CHANK[(self.coords_2[1])][(self.coords_2[2]+1)] # получили номер четвертины чанка
            a3 = MAP_CHANK[(self.coords_3[1])][(self.coords_3[2]+1)] # получили номер четвертины чанка
            a4 = MAP_CHANK[(self.coords_4[1])][(self.coords_4[2]+1)] # получили номер четвертины чанка
            for j in range(0,len(MAP_CHANK)):
                for i in range(0,len(MAP_CHANK[0])):
                    if a1 == MAP_CHANK[j][i]: # получили номер левого верхнего угла зоны просмотра, по нему дальше посчитали оординаты зоны просмотра
                        pos_ugol_chank = [j,i]
                        break
            self.coords_1 = [a1,pos_ugol_chank[0],pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
            self.coords_2 = [a2,pos_ugol_chank[0],(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
            self.coords_3 = [a3,(pos_ugol_chank[0]+1),pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
            self.coords_4 = [a4,(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
        if e.control.data == 'left':
            a1 = MAP_CHANK[(self.coords_1[1])][(self.coords_1[2]-1)] # получили номер четвертины чанка
            a2 = MAP_CHANK[(self.coords_2[1])][(self.coords_2[2]-1)] # получили номер четвертины чанка
            a3 = MAP_CHANK[(self.coords_3[1])][(self.coords_3[2]-1)] # получили номер четвертины чанка
            a4 = MAP_CHANK[(self.coords_4[1])][(self.coords_4[2]-1)] # получили номер четвертины чанка
            for j in range(0,len(MAP_CHANK)):
                for i in range(0,len(MAP_CHANK[0])):
                    if a1 == MAP_CHANK[j][i]: # получили номер левого верхнего угла зоны просмотра, по нему дальше посчитали оординаты зоны просмотра
                        pos_ugol_chank = [j,i]
                        break
            self.coords_1 = [a1,pos_ugol_chank[0],pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
            self.coords_2 = [a2,pos_ugol_chank[0],(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
            self.coords_3 = [a3,(pos_ugol_chank[0]+1),pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
            self.coords_4 = [a4,(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
            
            # print(f'Нажали вправо {a1}|{a2}|{a3}|{a4}') # 1.25|2|1.75|2.5
        self.print_chank_chetvert([a1,a2,a3,a4])


    def build(self):
        self.main_page = ft.Container(
            ft.Row(controls=[
                ft.Container(
                    ft.Row(controls=[
                            ft.Container(ft.Column(controls=[
                                    ft.Container(width=32,height=32,border=ft.border.all(1,YELLOW),margin=ft.margin.only(left=34,top=34)), # что сейчас выбрано
                                    ft.Container(ft.Image(src='src/img/img/1.png',height=32,width=32,fit=ft.ImageFit.COVER),on_click=self.fill_zero,width=32,height=32,margin=ft.margin.only(left=34,top=20))# залить все нули в выбранный цвет
                                ]),width=100,height=height_window_platforma,border=ft.border.all(1,YELLOW)),
                            ft.Container(ft.Container(
                                self.print_chank('print') # отрисовываем вначале дефолтный чанк
                            ),width=WIDTH_CANVA,height=HEIGHT_CANVA,padding=0,margin=ft.margin.only(left=100)),
                        ]),
                    width=1200,height=height_window_platforma,bgcolor=BLUE),
                ft.Container(
                    ft.Column(controls=[
                        ft.Container(ft.Text('Редактор карт',size=24,color=BLUE,text_align='center'),height=50,padding=ft.padding.only(top=8),bgcolor=YELLOW,width=400),
                        ft.Container(ft.Column(controls=[
                                ft.Container(ft.Image(src='src/img/img/4.png',width=50,height=50),margin=ft.margin.only(left=60)),
                                ft.Container(ft.Row(controls=[
                                    ft.Container(ft.Image(src='src/img/img/3.png',width=50,height=50),data='left',on_click=self.offset_btn),
                                    Input(self.input_num_chank,str(CHANK_START),50),
                                    ft.Container(ft.Image(src='src/img/img/2.png',width=50,height=50),data='right',on_click=self.offset_btn),
                                ])),
                                ft.Container(ft.Image(src='src/img/img/5.png',width=50,height=50),margin=ft.margin.only(left=60)),
                            ]),margin=ft.margin.only(left=20)),
                        ft.Container(width=360,height=1,bgcolor=WHITE,margin=ft.margin.only(left=20)),
                        ft.Container(self.palitra()),
                    ]),
                    width=400,height=height_window_platforma,bgcolor=BLUE,border=ft.border.all(1,YELLOW),margin=ft.margin.only(left=-10)),
            ]),margin=-1
        )
        return self.main_page
    
    
    
    