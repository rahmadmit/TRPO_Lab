import math as math
from tkinter import *
from tkinter import messagebox

#Основные функции
def distance(x0,y0,x,y):
    return math.sqrt((x - x0) ** 2 + (y-y0) ** 2)

def IsInRectangle(x0, y0, a, b, x, y):
    return (x >= x0 and x <= x0 + a and y >= y0 and y <= y0 + b)

def IsInCircle(x0, y0, r, x, y):
    return (distance(x0,y0,x,y) <= r)

#Сигналы
def clicked_on_distance():
    x = float(x_txt.get())
    y = float(y_txt.get())
    x0 = float(x0_dist_txt.get())
    y0 = float(y0_dist_txt.get())
    
    dist_window = Toplevel()
    dist_window.geometry('600x620+100+100')
    dist_window.title('Расстояние')
    
    c = Canvas(dist_window, width = 500, height = 500)
    c.grid(row = 0, column = 0)
    
    max_x_coord = max(1.1*x, 1.1*x0, 10)
    min_x_coord = min(1.1*x, 1.1*x0, -10)
    max_y_coord = max(1.1*y, 1.1*y0, 10)
    min_y_coord = min(1.1*y, 1.1*y0, -10)

    x_coord = (x - min_x_coord) * 500 / (max_x_coord - min_x_coord)
    x0_coord = (x0 - min_x_coord) * 500 / (max_x_coord - min_x_coord)
    y_coord = 500 - (y - min_y_coord) * 500 / (max_y_coord - min_y_coord)
    y0_coord = 500 - (y0 - min_y_coord) * 500 / (max_y_coord - min_y_coord)

    c.create_line(0, 500 + min_y_coord * 500 / (max_y_coord - min_y_coord), 500, 500 + min_y_coord * 500 / (max_y_coord - min_y_coord), arrow = LAST)
    c.create_line(- min_x_coord * 500 / (max_x_coord - min_x_coord), 500, - min_x_coord * 500 / (max_x_coord - min_x_coord), 0, arrow = LAST)
    
    c.create_line(x0_coord, y0_coord, x_coord, y_coord, width = 3, arrow = LAST)
    
    l_dist = Label(dist_window, text = "Расстояние между точками равно: " + str(distance(x0, y0, x, y)), font = ('Times New Roman', 18))
    l_dist.grid(row = 1, column = 0)

    dist_window.mainloop()

def clicked_on_rectangle():
    x = float(x_txt.get())
    y = float(y_txt.get())
    x0 = float(x0_rect_txt.get())
    y0 = float(y0_rect_txt.get())
    a = float(a_txt.get())
    b = float(b_txt.get())

    dist_window = Toplevel()
    dist_window.geometry('500x550+100+100')
    dist_window.title('Расстояние')
    
    c = Canvas(dist_window, width = 500, height = 500)
    c.grid(row = 0, column = 0)
    
    max_x_coord = max(1.1*x, 1.1*(x0+a), 10)
    min_x_coord = min(1.1*x, 1.1*x0, -10)
    max_y_coord = max(1.1*y, 1.1*(y0+b), 10)
    min_y_coord = min(1.1*y, 1.1*y0, -10)

    x_coord = (x - min_x_coord) * 500 / (max_x_coord - min_x_coord)
    x0_coord = (x0 - min_x_coord) * 500 / (max_x_coord - min_x_coord)
    y_coord = 500 - (y - min_y_coord) * 500 / (max_y_coord - min_y_coord)
    y0_coord = 500 - (y0 - min_y_coord) * 500 / (max_y_coord - min_y_coord)

    c.create_line(0, 500 + min_y_coord * 500 / (max_y_coord - min_y_coord), 500, 500 + min_y_coord * 500 / (max_y_coord - min_y_coord), arrow = LAST)
    c.create_line(- min_x_coord * 500 / (max_x_coord - min_x_coord), 500, - min_x_coord * 500 / (max_x_coord - min_x_coord), 0, arrow = LAST)
    
    c.create_rectangle(x0_coord, y0_coord - b * 500 / (max_y_coord - min_y_coord), x0_coord + a * 500 / (max_x_coord - min_x_coord), y0_coord)

    c.create_oval(x_coord - 3, y_coord - 3, x_coord + 3, y_coord + 3, fill = 'red')

    if (IsInRectangle(x0, y0, a, b, x, y)):
        mes = 'Точка лежит в прямоугольнике'
    else:
        mes = 'Точка не лежит в прямоугольнике'
    
    l_dist = Label(dist_window, text = mes, font = ('Times New Roman', 18))
    l_dist.grid(row = 1, column = 0)

    dist_window.mainloop()
    

def clicked_on_circle():
    x = float(x_txt.get())
    y = float(y_txt.get())
    x0 = float(x0_circ_txt.get())
    y0 = float(y0_circ_txt.get())
    r = float(r_txt.get())
    
    dist_window = Toplevel()
    dist_window.geometry('500x550+100+100')
    dist_window.title('Расстояние')
    
    c = Canvas(dist_window, width = 500, height = 500)
    c.grid(row = 0, column = 0)
    
    max_x_coord = max(1.1*x, 1.1*(x0+r), 10)
    min_x_coord = min(1.1*x, 1.1*x0, -10)
    max_y_coord = max(1.1*y, 1.1*(y0+r), 10)
    min_y_coord = min(1.1*y, 1.1*y0, -10)

    x_coord = (x - min_x_coord) * 500 / (max_x_coord - min_x_coord)
    x0_coord = (x0 - min_x_coord) * 500 / (max_x_coord - min_x_coord)
    y_coord = 500 - (y - min_y_coord) * 500 / (max_y_coord - min_y_coord)
    y0_coord = 500 - (y0 - min_y_coord) * 500 / (max_y_coord - min_y_coord)

    c.create_line(0, 500 + min_y_coord * 500 / (max_y_coord - min_y_coord), 500, 500 + min_y_coord * 500 / (max_y_coord - min_y_coord), arrow = LAST)
    c.create_line(- min_x_coord * 500 / (max_x_coord - min_x_coord), 500, - min_x_coord * 500 / (max_x_coord - min_x_coord), 0, arrow = LAST)
    
    c.create_oval(x0_coord - r * 500 / (max_y_coord - min_y_coord), y0_coord - r * 500 / (max_y_coord - min_y_coord), x0_coord + r * 500 / (max_x_coord - min_x_coord), y0_coord + r * 500 / (max_y_coord - min_y_coord))

    c.create_oval(x_coord - 3, y_coord - 3, x_coord + 3, y_coord + 3, fill = 'red')

    if (IsInCircle(x0, y0, r, x, y)):
        mes = 'Точка лежит в окружности'
    else:
        mes = 'Точка не лежит в окружности'
    
    l_dist = Label(dist_window, text = mes, font = ('Times New Roman', 18))
    l_dist.grid(row = 1, column = 0)

    dist_window.mainloop()


window = Tk()
window.geometry('750x400+200+200')
window.title('лаба 1')

        
#Верхняя часть
prog_name = Label(window, text = 'Welcome to the academ!', font = ('Times New Roman', 26))
prog_name.grid(column = 0, columnspan = 6, row = 0)

x_lbl = Label(window, text = 'X:', font = ('Times New Roman', 18))
x_lbl.grid(column = 0, columnspan = 3, row = 1, sticky = E)
x_txt = Entry(window)
x_txt.grid(column = 3, columnspan = 3, row = 1, sticky = W)

y_lbl = Label(window, text = 'Y:', font = ('Times New Roman', 18))
y_lbl.grid(column = 0, columnspan = 3, row = 2, sticky = E)
y_txt = Entry(window)
y_txt.grid(column = 3, columnspan = 3, row = 2, sticky = W)

#Лейблы функций

dist_lbl = Label(window, text = 'Расстояние', font = ('Times New Roman', 14))
dist_lbl.grid(column = 0, columnspan = 2, row = 3, ipady = 20)

rect_lbl = Label(window, text = 'Лежит ли точка в прямоугольнике?', font = ('Times New Roman', 14))
rect_lbl.grid(column = 2, columnspan = 2, row = 3, ipadx = 30)

circ_lbl = Label(window, text = 'Лежит ли точка в окружности?', font = ('Times New Roman', 14))
circ_lbl.grid(column = 4, columnspan = 2, row = 3)

#Для дистанции

x0_dist_lbl = Label(window, text = 'X0:', font = ('Times New Roman', 14))
x0_dist_lbl.grid(column = 0, row = 4, sticky = E)
x0_dist_txt = Entry(window, width = 5)
x0_dist_txt.grid(column = 1, row = 4, sticky = W)

y0_dist_lbl = Label(window, text = 'Y0:', font = ('Times New Roman', 14))
y0_dist_lbl.grid(column = 0, row = 5, sticky = E)
y0_dist_txt = Entry(window, width = 5)
y0_dist_txt.grid(column = 1, row = 5, sticky = W)

#Для прямоугольника

x0_rect_lbl = Label(window, text = 'X0:', font = ('Times New Roman', 14))
x0_rect_lbl.grid(column = 2, row = 4, sticky = E)
x0_rect_txt = Entry(window, width = 5)
x0_rect_txt.grid(column = 3, row = 4, sticky = W)

y0_rect_lbl = Label(window, text = 'Y0:', font = ('Times New Roman', 14))
y0_rect_lbl.grid(column = 2, row = 5, sticky = E)
y0_rect_txt = Entry(window, width = 5)
y0_rect_txt.grid(column = 3, row = 5, sticky = W)

a_lbl = Label(window, text = 'a:', font = ('Times New Roman', 14))
a_lbl.grid(column = 2, row = 6, sticky = E)
a_txt = Entry(window, width = 5)
a_txt.grid(column = 3, row = 6, sticky = W)

b_lbl = Label(window, text = 'b:', font = ('Times New Roman', 14))
b_lbl.grid(column = 2, row = 7, sticky = E)
b_txt = Entry(window, width = 5)
b_txt.grid(column = 3, row = 7, sticky = W)

#Для окружности

x0_circ_lbl = Label(window, text = 'X0:', font = ('Times New Roman', 14))
x0_circ_lbl.grid(column = 4, row = 4, sticky = E)
x0_circ_txt = Entry(window, width = 5)
x0_circ_txt.grid(column = 5, row = 4, sticky = W)

y0_circ_lbl = Label(window, text = 'Y0:', font = ('Times New Roman', 14))
y0_circ_lbl.grid(column = 4, row = 5, sticky = E)
y0_circ_txt = Entry(window, width = 5)
y0_circ_txt.grid(column = 5, row = 5, sticky = W)

r_lbl = Label(window, text = 'r:', font = ('Times New Roman', 14))
r_lbl.grid(column = 4, row = 6, sticky = E)
r_txt = Entry(window, width = 5)
r_txt.grid(column = 5, row = 6, sticky = W)

#Кнопки
btn_dist = Button(window, text = 'Вычислить', command = clicked_on_distance)
btn_dist.grid(column = 0, columnspan = 2, row = 8, pady = 20)

btn_rect = Button(window, text = 'Проверить', command = clicked_on_rectangle)
btn_rect.grid(column = 2, columnspan = 2, row = 8)

btn_circ = Button(window, text = 'Проверить', command = clicked_on_circle)
btn_circ.grid(column = 4, columnspan = 2, row = 8)


window.mainloop()

