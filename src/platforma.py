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
        # print(f'{self.coords_1[0]}|{self.coords_2[0]}|{self.coords_3[0]}|{self.coords_4[0]}')
        self.flag_zalifka_diapazon = False
        
    # движения по кнопкам
    def on_keyboard(self,e):
        # print(e.key)
        try:
            self.controls[0].content.controls[1].content.controls[1].content.controls[1].content.controls[1] = Input(self.input_num_chank,str(self.coords_1[0]),50)
            if e.key == 'W':
                if self.coords_1[1]-1>=0 and self.coords_2[1]-1>=0 and self.coords_3[1]-1>=0 and self.coords_4[1]-1>=0:
                    a1 = MAP_CHANK[(self.coords_1[1]-1)][(self.coords_1[2])] # получили номер четвертины чанка
                    a2 = MAP_CHANK[(self.coords_2[1]-1)][(self.coords_2[2])] # получили номер четвертины чанка
                    a3 = MAP_CHANK[(self.coords_3[1]-1)][(self.coords_3[2])] # получили номер четвертины чанка
                    a4 = MAP_CHANK[(self.coords_4[1]-1)][(self.coords_4[2])] # получили номер четвертины чанка
                    for j in range(0,len(MAP_CHANK)):
                        for i in range(0,len(MAP_CHANK[0])):
                            if a1 == MAP_CHANK[j][i]: # получили номер левого верхнего угла зоны просмотра, по нему дальше посчитали оординаты зоны просмотра
                                pos_ugol_chank = [j,i]
                                break
                    if pos_ugol_chank[0]==0 or pos_ugol_chank[1]==0: 
                        self.controls[0].content.controls[1].content.controls[1].content.controls[1].content.controls[1] = ft.Container(ft.Text('!',color=WHITE),width=50,height=50,bgcolor=RED)
                        self.update()
                    
                    self.coords_1 = [a1,pos_ugol_chank[0],pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                    self.coords_2 = [a2,pos_ugol_chank[0],(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                    self.coords_3 = [a3,(pos_ugol_chank[0]+1),pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                    self.coords_4 = [a4,(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
            if e.key == 'S':
                a1 = MAP_CHANK[(self.coords_1[1]+1)][(self.coords_1[2])] # получили номер четвертины чанка
                a2 = MAP_CHANK[(self.coords_2[1]+1)][(self.coords_2[2])] # получили номер четвертины чанка
                a3 = MAP_CHANK[(self.coords_3[1]+1)][(self.coords_3[2])] # получили номер четвертины чанка
                a4 = MAP_CHANK[(self.coords_4[1]+1)][(self.coords_4[2])] # получили номер четвертины чанка
                for j in range(0,len(MAP_CHANK)):
                    for i in range(0,len(MAP_CHANK[0])):
                        if a1 == MAP_CHANK[j][i]: # получили номер левого верхнего угла зоны просмотра, по нему дальше посчитали оординаты зоны просмотра
                            pos_ugol_chank = [j,i]
                            break
                if pos_ugol_chank[0]==0 or pos_ugol_chank[1]==0: 
                    self.controls[0].content.controls[1].content.controls[1].content.controls[1].content.controls[1] = ft.Container(ft.Text('!',color=WHITE),width=50,height=50,bgcolor=RED)
                    self.update()
                self.coords_1 = [a1,pos_ugol_chank[0],pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                self.coords_2 = [a2,pos_ugol_chank[0],(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                self.coords_3 = [a3,(pos_ugol_chank[0]+1),pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                self.coords_4 = [a4,(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
            if e.key == 'A':
                if self.coords_1[2]-1>=0 and self.coords_2[2]-1>=0 and self.coords_3[2]-1>=0 and self.coords_4[2]-1>=0:
                    a1 = MAP_CHANK[(self.coords_1[1])][(self.coords_1[2]-1)] # получили номер четвертины чанка
                    # print(f"==>> a1: {a1}")
                    a2 = MAP_CHANK[(self.coords_2[1])][(self.coords_2[2]-1)] # получили номер четвертины чанка
                    a3 = MAP_CHANK[(self.coords_3[1])][(self.coords_3[2]-1)] # получили номер четвертины чанка
                    a4 = MAP_CHANK[(self.coords_4[1])][(self.coords_4[2]-1)] # получили номер четвертины чанка
                    for j in range(0,len(MAP_CHANK)):
                        for i in range(0,len(MAP_CHANK[0])):
                            if a1 == MAP_CHANK[j][i]: # получили номер левого верхнего угла зоны просмотра, по нему дальше посчитали оординаты зоны просмотра
                                pos_ugol_chank = [j,i]
                                # print(f"==>> pos_ugol_chank: {pos_ugol_chank}")
                                break
                    
                    if pos_ugol_chank[1]==0 or pos_ugol_chank[0]==0: 
                        self.controls[0].content.controls[1].content.controls[1].content.controls[1].content.controls[1] = ft.Container(ft.Text('|<',color=WHITE),width=50,height=50,bgcolor=RED)
                        self.update()
                    self.coords_1 = [a1,pos_ugol_chank[0],pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                    self.coords_2 = [a2,pos_ugol_chank[0],(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                    self.coords_3 = [a3,(pos_ugol_chank[0]+1),pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                    self.coords_4 = [a4,(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
            if e.key == 'D':
                a1 = MAP_CHANK[(self.coords_1[1])][(self.coords_1[2]+1)] # получили номер четвертины чанка
                a2 = MAP_CHANK[(self.coords_2[1])][(self.coords_2[2]+1)] # получили номер четвертины чанка
                a3 = MAP_CHANK[(self.coords_3[1])][(self.coords_3[2]+1)] # получили номер четвертины чанка
                a4 = MAP_CHANK[(self.coords_4[1])][(self.coords_4[2]+1)] # получили номер четвертины чанка
                for j in range(0,len(MAP_CHANK)):
                    for i in range(0,len(MAP_CHANK[0])):
                        if a1 == MAP_CHANK[j][i]: # получили номер левого верхнего угла зоны просмотра, по нему дальше посчитали оординаты зоны просмотра
                            pos_ugol_chank = [j,i]
                            break
                if pos_ugol_chank[0]==0 or pos_ugol_chank[1]==0: 
                    self.controls[0].content.controls[1].content.controls[1].content.controls[1].content.controls[1] = ft.Container(ft.Text('!',color=WHITE),width=50,height=50,bgcolor=RED)
                    self.update()
                self.coords_1 = [a1,pos_ugol_chank[0],pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                self.coords_2 = [a2,pos_ugol_chank[0],(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                self.coords_3 = [a3,(pos_ugol_chank[0]+1),pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                self.coords_4 = [a4,(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
            self.print_chank_chetvert([a1,a2,a3,a4])
        except Exception as e:
            print(f'У границы или ошибка - {e}')
            
    # клик начало по тайлу
    def click_start_tile(self,e):
        if self.flag_zalifka_diapazon == False: # если не выбран режим заливки диапазона
            if self.changed_color: 
                if e.control.content: 
                    # print(self.changed_color[0])
                    if int(self.changed_color[0].split('/')[-1][:-4]) in COLOR_PNG:
                        print(int(self.changed_color[1][:-4]))
                        # now_img = e.control.content
                        # e.control.content = ft.Image(src=self.changed_color[0],width=COLOR_PNG_size[self.changed_color[0].split('/')[-1][:-4]][0],height=COLOR_PNG_size[self.changed_color[0].split('/')[-1][:-4]][1])
                        # e.control.content = ft.Stack([
                        #     now_img,
                        #     ft.Image(src=self.changed_color[0],width=COLOR_PNG_size[self.changed_color[0].split('/')[-1][:-4]][0],height=COLOR_PNG_size[self.changed_color[0].split('/')[-1][:-4]][1])
                        # ])
                        # print(e.control.content)
                        
                        with open(f'src/map/chamk_chetvert/{e.control.data[2]}.txt') as f:
                            mas_map = ast.literal_eval(f.readline())
                        for data in COLOR_PNG_size[str(self.changed_color[1][:-4])]:
                            mas_map[e.control.data[0]-1+data[0]][e.control.data[1]-1+data[1]] = int(data[2])
                        my_file = open(f'src/map/chamk_chetvert/{e.control.data[2]}.txt', "w+")
                        my_file.write(f'{str(mas_map)}')
                        my_file.close()
                        self.print_chank_chetvert([self.coords_1[0],self.coords_2[0],self.coords_3[0],self.coords_4[0]])    
                    else:
                        now_img = e.control.content
                        e.control.content = ft.Stack([
                            now_img,
                            ft.Image(src=self.changed_color[0],width=32,height=32)
                        ])
                        # сохраняем в карту
                        with open(f'src/map/chamk_chetvert/{e.control.data[2]}.txt') as f:
                            mas_map = ast.literal_eval(f.readline())
                        mas_map[e.control.data[0]-1][e.control.data[1]-1] = int(self.changed_color[1][:-4])
                        my_file = open(f'src/map/chamk_chetvert/{e.control.data[2]}.txt', "w+")
                        my_file.write(f'{str(mas_map)}')
                        my_file.close()
                        self.flag_hover = True
                else: 
                    e.control.content = ft.Image(src=self.changed_color[0],width=32,height=32)
                    # сохраняем в карту
                    with open(f'src/map/chamk_chetvert/{e.control.data[2]}.txt') as f:
                        mas_map = ast.literal_eval(f.readline())
                    mas_map[e.control.data[0]-1][e.control.data[1]-1] = int(self.changed_color[1][:-4])
                    my_file = open(f'src/map/chamk_chetvert/{e.control.data[2]}.txt', "w+")
                    my_file.write(f'{str(mas_map)}')
                    my_file.close()
                    self.flag_hover = True
            self.update()
            if self.flag_hover_back:
                # print(self.mas_hover)
                for i in self.mas_hover:
                    with open(f'src/map/chamk_chetvert/{i[3]}.txt') as f:
                        mas_map = ast.literal_eval(f.readline())
                    # # сохраняем в карту
                    mas_map[i[0]-1][i[1]-1] = int(i[2])
                    # mas_map[e.control.data[0]-1][e.control.data[1]-1] = int(self.changed_color[1][:-4])
                    my_file = open(f'src/map/chamk_chetvert/{i[3]}.txt', "w+")
                    my_file.write(f'{str(mas_map)}')
                    my_file.close()
                self.mas_hover[:] = []
                self.flag_hover_back = False
        else:
            with open(f'src/map/chamk_chetvert/{e.control.data[2]}.txt') as f:
                mas_map = ast.literal_eval(f.readline())
            # if mas_map[e.control.data[0]-1][e.control.data[1]-1] == 0:
            yze_zalito = mas_map[e.control.data[0]-1][e.control.data[1]-1]
            # вверх по рядам
            for j in range(e.control.data[0]-1,-1,-1):
                # двигаемся влево в одном ряду
                if mas_map[j][e.control.data[1]-1] == yze_zalito: 
                    for i in range((e.control.data[1]-1),-1,-1):
                        if mas_map[j][i] == yze_zalito: 
                            mas_map[j][i] = int(self.changed_color[1][:-4])
                        else: break
                    # двигаемся вправо в одном ряду
                    for i in range((e.control.data[1]),len(mas_map[0])):
                        if mas_map[j][i] == yze_zalito: 
                            mas_map[j][i] = int(self.changed_color[1][:-4])
                        else: break
                else: break
            # вниз по рядам
            for j in range(e.control.data[0],len(mas_map)):
                if mas_map[j][e.control.data[1]-1] == yze_zalito: 
                    for i in range((e.control.data[1]-1),-1,-1):
                        if mas_map[j][i] == yze_zalito: 
                            mas_map[j][i] = int(self.changed_color[1][:-4])
                        else: break
                    # двигаемся вправо в одном ряду
                    for i in range((e.control.data[1]),len(mas_map[0])):
                        if mas_map[j][i] == yze_zalito: 
                            mas_map[j][i] = int(self.changed_color[1][:-4])
                        else: break
                else: break
                # for i in range((e.control.data[1]-1),-1,-1):
                #     if mas_map[e.control.data[0]-1][i] == 0: 
                #         mas_map[e.control.data[0]-1][i] = int(self.changed_color[1][:-4])
                #     else: break
                # # двигаемся вправо в одном ряду
                # for i in range((e.control.data[1]),len(mas_map[0])):
                #     if mas_map[e.control.data[0]-1][i] == 0: 
                #         mas_map[e.control.data[0]-1][i] = int(self.changed_color[1][:-4])
                #     else: break
            my_file = open(f'src/map/chamk_chetvert/{e.control.data[2]}.txt', "w+")
            my_file.write(f'{str(mas_map)}')
            my_file.close()
            self.print_chank_chetvert([self.coords_1[0],self.coords_2[0],self.coords_3[0],self.coords_4[0]])
            self.update()
                              
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
            self.mas_hover.append([e.control.data[0],e.control.data[1],self.changed_color[1][:-4],e.control.data[2]])
            self.update()
    
    # # залить все нули выделенным цветом
    def fill_zero(self,e):
        # print('Типа залили')
        if self.changed_color: 
            for name_chetv_chank in [self.coords_1[0],self.coords_2[0],self.coords_3[0],self.coords_4[0]]:
                with open(f'src/map/chamk_chetvert/{name_chetv_chank}.txt') as f:
                    mas_map = ast.literal_eval(f.readline())
                for i in range(0,15):
                    for j in range(0,15):
                        if mas_map[i][j] == 0:
                            mas_map[i][j] = int(self.changed_color[1][:-4])
                my_file = open(f'src/map/chamk_chetvert/{name_chetv_chank}.txt', "w+")
                my_file.write(f'{str(mas_map)}')
                my_file.close()
                # print(f'Заливка цветом {int(self.changed_color[1][:-4])} выполнена')
                self.print_chank_chetvert([self.coords_1[0],self.coords_2[0],self.coords_3[0],self.coords_4[0]])
                self.update()
        else: print('Сначала выберите чем залить нули')

    # удалить все тексутры в активном чанке
    def delete_chanks(self,e):
         # print('Типа залили')
            for name_chetv_chank in [self.coords_1[0],self.coords_2[0],self.coords_3[0],self.coords_4[0]]:
                with open(f'src/map/chamk_chetvert/{name_chetv_chank}.txt') as f:
                    mas_map = ast.literal_eval(f.readline())
                for i in range(0,15):
                    for j in range(0,15):
                        mas_map[i][j] = 0
                my_file = open(f'src/map/chamk_chetvert/{name_chetv_chank}.txt', "w+")
                my_file.write(f'{str(mas_map)}')
                my_file.close()
                # print(f'Заливка цветом {int(self.changed_color[1][:-4])} выполнена')
                self.print_chank_chetvert([self.coords_1[0],self.coords_2[0],self.coords_3[0],self.coords_4[0]])
                self.update()

    # залить нули по границам
    def fill_zero_diapazon(self,e):
        if self.changed_color: 
            if self.flag_zalifka_diapazon == False:
                self.controls[0].content.controls[0].content.controls[0].content.controls[2].border = ft.border.all(2,YELLOW)
                self.update()
                self.flag_zalifka_diapazon = True
            else:
                self.controls[0].content.controls[0].content.controls[0].content.controls[2].border = ft.border.all(1,BLUE)
                self.update()
                self.flag_zalifka_diapazon = False
                
            
        else: print('Сначала выберите чем залить')

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
            if i!='main.png':
                colors_mas.append(ft.Container(ft.Image(src=f'src/tilemap/palitra/{dev_color}/{i}',width=32,height=32),on_click=self.change_dev_color,data=[f'src/tilemap/palitra/{dev_color}/{i}',i],width=32,height=32,bgcolor=BLUE))
        if os.path.isfile(f'src/tilemap/palitra/{dev_color}/main.png'):
            return ft.Container(ft.Column(controls=[
                ft.Container(ft.Row(controls=colors_mas,wrap=True,spacing=5,run_spacing=5,),width=350,padding=10),
                ft.Container(ft.Image(src=f'src/tilemap/palitra/{dev_color}/main.png',width=350),width=350,padding=10),
            ]))
        else:
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
                self.print_chank_chetvert([self.coords_1[0],self.coords_2[0],self.coords_3[0],self.coords_4[0]])
       
       
    # отрисовка четвертинок чанка
    def print_chank_chetvert(self,cords,regime='default'):
        mas_fore_pol_chanks = []
        mas_fore_pol_chanks.clear()
        count_l = 0
        for cords_i in cords: # итерируемся по 4 названием текущих чанков
            # получили файл с картой чанка
            # print(f'src/map/chamk_chetvert/{cords_i}.txt')
            with open(f'src/map/chamk_chetvert/{cords_i}.txt') as f:
                mas_map = ast.literal_eval(f.readline())
            # рисуем сетку
            line_x_mas = []
            line_y_mas = []
            line_y_mas.clear()
            for i in range(1,16):
                line_x_mas.clear()
                for j in range(1,16):
                    if mas_map[i-1][j-1] == 0: line_x_mas.append(ft.Container(data=[i,j,cords_i],on_hover=self.hover_tile,on_click=self.click_end_tile,on_tap_down=self.click_start_tile,height=TILESIZE,width=TILESIZE,border=ft.border.all(0.1,BLUE)))
                    else: line_x_mas.append(ft.Container(ft.Image(src=f'src/tilemap/all/{mas_map[i-1][j-1]}.png',width=32,height=32),data=[i,j,cords_i],on_hover=self.hover_tile,on_click=self.click_end_tile,on_tap_down=self.click_start_tile,height=TILESIZE,width=TILESIZE,border=ft.border.all(0.1,BLUE)))
                line_y_mas.append(ft.Container(ft.Row(controls=line_x_mas,spacing=0,run_spacing=0,)))
            mas_fore_pol_chanks.append(line_y_mas)
        if regime == 'default':
            self.controls[0].content.controls[0].content.controls[1].content.content = ft.Container(ft.Stack([
                ft.Container(ft.Row(controls=[
                    ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[0]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                    ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[1]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                    ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[2]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                    ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[3]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                ],wrap=True,spacing=0,run_spacing=0)),
                ft.Container(ft.Row(controls=[
                    ft.Container(ft.Column(controls=mas_fore_pol_chanks[0],spacing=0,run_spacing=0,),width=WIDTH_CANVA/2,height=HEIGHT_CANVA/2),
                    ft.Container(ft.Column(controls=mas_fore_pol_chanks[1],spacing=0,run_spacing=0,),width=WIDTH_CANVA/2,height=HEIGHT_CANVA/2),
                    ft.Container(ft.Column(controls=mas_fore_pol_chanks[2],spacing=0,run_spacing=0,),width=WIDTH_CANVA/2,height=HEIGHT_CANVA/2),
                    ft.Container(ft.Column(controls=mas_fore_pol_chanks[3],spacing=0,run_spacing=0,),width=WIDTH_CANVA/2,height=HEIGHT_CANVA/2),
                    
                ],wrap=True,spacing=0,run_spacing=0)),
                # ft.Column(controls=line_y_mas,spacing=0,run_spacing=0,)
            ]),height=HEIGHT_CANVA,width=WIDTH_CANVA)
            self.update()
        else: # для отрисовки 1 раз при старте
            return ft.Container(ft.Stack([
                ft.Container(ft.Row(controls=[
                    ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[0]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                    ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[1]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                    ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[2]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                    ft.Image(src=f'src/img/map_grid/Tile_png_chetwert/{cords[3]}.png',height=HEIGHT_CANVA/2,width=WIDTH_CANVA/2,fit=ft.ImageFit.FILL),
                ],wrap=True,spacing=0,run_spacing=0)),
                ft.Container(ft.Row(controls=[
                    ft.Container(ft.Column(controls=mas_fore_pol_chanks[0],spacing=0,run_spacing=0,),width=WIDTH_CANVA/2,height=HEIGHT_CANVA/2),
                    ft.Container(ft.Column(controls=mas_fore_pol_chanks[1],spacing=0,run_spacing=0,),width=WIDTH_CANVA/2,height=HEIGHT_CANVA/2),
                    ft.Container(ft.Column(controls=mas_fore_pol_chanks[2],spacing=0,run_spacing=0,),width=WIDTH_CANVA/2,height=HEIGHT_CANVA/2),
                    ft.Container(ft.Column(controls=mas_fore_pol_chanks[3],spacing=0,run_spacing=0,),width=WIDTH_CANVA/2,height=HEIGHT_CANVA/2),
                    
                ],wrap=True,spacing=0,run_spacing=0)),
                # ft.Column(controls=line_y_mas,spacing=0,run_spacing=0,)
            ]),height=HEIGHT_CANVA,width=WIDTH_CANVA)
       
    # нажатие на стрелки пермещение по карте
    def offset_btn(self,e):
        try:
            # print()
            self.controls[0].content.controls[1].content.controls[1].content.controls[1].content.controls[1] = Input(self.input_num_chank,str(self.coords_1[0]),50)
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
                if pos_ugol_chank[0]==0 or pos_ugol_chank[1]==0: 
                    self.controls[0].content.controls[1].content.controls[1].content.controls[1].content.controls[1] = ft.Container(ft.Text('!',color=WHITE),width=50,height=50,bgcolor=RED)
                    self.update()
                self.coords_1 = [a1,pos_ugol_chank[0],pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                self.coords_2 = [a2,pos_ugol_chank[0],(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                self.coords_3 = [a3,(pos_ugol_chank[0]+1),pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                self.coords_4 = [a4,(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                # self.print_chank_chetvert([a1,a2,a3,a4])
            if e.control.data == 'left':
                if self.coords_1[2]-1>=0 and self.coords_2[2]-1>=0 and self.coords_3[2]-1>=0 and self.coords_4[2]-1>=0:
                    a1 = MAP_CHANK[(self.coords_1[1])][(self.coords_1[2]-1)] # получили номер четвертины чанка
                    # print(f"==>> a1: {a1}")
                    a2 = MAP_CHANK[(self.coords_2[1])][(self.coords_2[2]-1)] # получили номер четвертины чанка
                    a3 = MAP_CHANK[(self.coords_3[1])][(self.coords_3[2]-1)] # получили номер четвертины чанка
                    a4 = MAP_CHANK[(self.coords_4[1])][(self.coords_4[2]-1)] # получили номер четвертины чанка
                    for j in range(0,len(MAP_CHANK)):
                        for i in range(0,len(MAP_CHANK[0])):
                            if a1 == MAP_CHANK[j][i]: # получили номер левого верхнего угла зоны просмотра, по нему дальше посчитали оординаты зоны просмотра
                                pos_ugol_chank = [j,i]
                                # print(f"==>> pos_ugol_chank: {pos_ugol_chank}")
                                break
                    
                    if pos_ugol_chank[1]==0 or pos_ugol_chank[0]==0: 
                        self.controls[0].content.controls[1].content.controls[1].content.controls[1].content.controls[1] = ft.Container(ft.Text('|<',color=WHITE),width=50,height=50,bgcolor=RED)
                        self.update()

                    self.coords_1 = [a1,pos_ugol_chank[0],pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                    self.coords_2 = [a2,pos_ugol_chank[0],(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                    self.coords_3 = [a3,(pos_ugol_chank[0]+1),pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                    self.coords_4 = [a4,(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                        # self.print_chank_chetvert([a1,a2,a3,a4])
            if e.control.data == 'up':
                if self.coords_1[1]-1>=0 and self.coords_2[1]-1>=0 and self.coords_3[1]-1>=0 and self.coords_4[1]-1>=0:
                    a1 = MAP_CHANK[(self.coords_1[1]-1)][(self.coords_1[2])] # получили номер четвертины чанка
                    a2 = MAP_CHANK[(self.coords_2[1]-1)][(self.coords_2[2])] # получили номер четвертины чанка
                    a3 = MAP_CHANK[(self.coords_3[1]-1)][(self.coords_3[2])] # получили номер четвертины чанка
                    a4 = MAP_CHANK[(self.coords_4[1]-1)][(self.coords_4[2])] # получили номер четвертины чанка
                    for j in range(0,len(MAP_CHANK)):
                        for i in range(0,len(MAP_CHANK[0])):
                            if a1 == MAP_CHANK[j][i]: # получили номер левого верхнего угла зоны просмотра, по нему дальше посчитали оординаты зоны просмотра
                                pos_ugol_chank = [j,i]
                                break
                    if pos_ugol_chank[0]==0 or pos_ugol_chank[1]==0: 
                        self.controls[0].content.controls[1].content.controls[1].content.controls[1].content.controls[1] = ft.Container(ft.Text('!',color=WHITE),width=50,height=50,bgcolor=RED)
                        self.update()
                    
                    self.coords_1 = [a1,pos_ugol_chank[0],pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                    self.coords_2 = [a2,pos_ugol_chank[0],(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                    self.coords_3 = [a3,(pos_ugol_chank[0]+1),pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                    self.coords_4 = [a4,(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                        # self.print_chank_chetvert([a1,a2,a3,a4])
            if e.control.data == 'down':
                a1 = MAP_CHANK[(self.coords_1[1]+1)][(self.coords_1[2])] # получили номер четвертины чанка
                a2 = MAP_CHANK[(self.coords_2[1]+1)][(self.coords_2[2])] # получили номер четвертины чанка
                a3 = MAP_CHANK[(self.coords_3[1]+1)][(self.coords_3[2])] # получили номер четвертины чанка
                a4 = MAP_CHANK[(self.coords_4[1]+1)][(self.coords_4[2])] # получили номер четвертины чанка
                for j in range(0,len(MAP_CHANK)):
                    for i in range(0,len(MAP_CHANK[0])):
                        if a1 == MAP_CHANK[j][i]: # получили номер левого верхнего угла зоны просмотра, по нему дальше посчитали оординаты зоны просмотра
                            pos_ugol_chank = [j,i]
                            break
                if pos_ugol_chank[0]==0 or pos_ugol_chank[1]==0: 
                    self.controls[0].content.controls[1].content.controls[1].content.controls[1].content.controls[1] = ft.Container(ft.Text('!',color=WHITE),width=50,height=50,bgcolor=RED)
                    self.update()
                self.coords_1 = [a1,pos_ugol_chank[0],pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                self.coords_2 = [a2,pos_ugol_chank[0],(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                self.coords_3 = [a3,(pos_ugol_chank[0]+1),pos_ugol_chank[1]] # перезаписываем массив со значением и координатами этих значений
                self.coords_4 = [a4,(pos_ugol_chank[0]+1),(pos_ugol_chank[1]+1)] # перезаписываем массив со значением и координатами этих значений
                # self.print_chank_chetvert([a1,a2,a3,a4])
            self.print_chank_chetvert([a1,a2,a3,a4])
            # print(f'{a1}|{a2}|{a3}|{a4}') # 1.25|2|1.75|2.5
            # self.print_chank_chetvert([a1,a2,a3,a4])
            # print(f'{a1} - {a2} - {a3} - {a4}')
        except Exception as e:
            # print(f'{a1} - {a2} - {a3} - {a4}')
            print(f'У границы или ошибка - {e}')


    def build(self):
        # self.page.on_keyboard_event = self.on_keyboard
        self.main_page = ft.Container(
            ft.Row(controls=[
                ft.Container(
                    ft.Row(controls=[
                            ft.Container(ft.Column(controls=[
                                    ft.Container(width=32,height=32,border=ft.border.all(1,YELLOW),margin=ft.margin.only(left=34,top=34)), # что сейчас выбрано
                                    ft.Container(ft.Image(src='src/img/img/1.png',height=32,width=32,fit=ft.ImageFit.COVER),on_click=self.fill_zero,width=32,height=32,margin=ft.margin.only(left=34,top=20)),# залить все нули в выбранный цвет
                                    ft.Container(ft.Image(src='src/img/img/7.png',height=32,width=32,fit=ft.ImageFit.COVER),on_click=self.fill_zero_diapazon,width=32,height=32,margin=ft.margin.only(left=34,top=20)),# залить все нули в выбранный цвет
                                    ft.Container(ft.Image(src='src/img/img/6.png',height=32,width=32,fit=ft.ImageFit.COVER),on_click=self.delete_chanks,width=32,height=32,margin=ft.margin.only(left=34,top=20)),# 
                                ]),width=100,height=height_window_platforma,border=ft.border.all(1,YELLOW)),
                            ft.Container(ft.Container(
                                self.print_chank_chetvert([self.coords_1[0],self.coords_2[0],self.coords_3[0],self.coords_4[0]],'print') # отрисовываем вначале дефолтный чанк
                            ),width=WIDTH_CANVA,height=HEIGHT_CANVA,padding=0,margin=ft.margin.only(left=100)),
                        ]),
                    width=1200,height=height_window_platforma,bgcolor=BLUE),
                ft.Container(
                    ft.Column(controls=[
                        ft.Container(ft.Text('Редактор карт',size=24,color=BLUE,text_align='center'),height=50,padding=ft.padding.only(top=8),bgcolor=YELLOW,width=400),
                        ft.Container(ft.Column(controls=[
                                ft.Container(ft.Image(src='src/img/img/4.png',width=50,height=50),margin=ft.margin.only(left=60),data='up',on_click=self.offset_btn),
                                ft.Container(ft.Row(controls=[
                                    ft.Container(ft.Image(src='src/img/img/3.png',width=50,height=50),data='left',on_click=self.offset_btn),
                                    Input(self.input_num_chank,str(CHANK_START),50),
                                    ft.Container(ft.Image(src='src/img/img/2.png',width=50,height=50),data='right',on_click=self.offset_btn),
                                ])),
                                ft.Container(ft.Image(src='src/img/img/5.png',width=50,height=50),margin=ft.margin.only(left=60),data='down',on_click=self.offset_btn),
                            ]),margin=ft.margin.only(left=20)),
                        ft.Container(width=360,height=1,bgcolor=WHITE,margin=ft.margin.only(left=20)),
                        ft.Container(self.palitra()),
                    ]),
                    width=400,height=height_window_platforma,bgcolor=BLUE,border=ft.border.all(1,YELLOW),margin=ft.margin.only(left=-10)),
            ]),margin=-1
        )
        return self.main_page
    
    
    
    