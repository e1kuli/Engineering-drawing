# задан список вершин
# он проходит обработку проекцией и присваивается буферному списку
# буферный список передается на вывод


from Linked_List import *
from Gr_Module import *
from tkinter import *
from math import *
import numpy as np

root = Tk()
root.geometry('1024x620')
bg_color='blue'
canvas = Canvas(root, width=824, height=620, bg=bg_color)
canvas.pack(side="right")
line_color = 'black'

# смещение при рисовании линии, что бы не уходило в "-"
shift_x = 200
shift_y = 400
angle = 0.261799
linear_transformation = 1
###
figures = []
fig_num=0
figures.append(LinkedList())
figures[fig_num].add_node([0, 0, 0,1], 1)
figures[fig_num].add_link(1, [100, 0, 0,1])
figures[fig_num].add_link(1, [0, 100, 0,1])
figures[fig_num].add_link(1, [0, 0, 100,1])

ind = 2

figures.append(LinkedList())

figures[fig_num+1].add_node([10 * ind, 10 * ind, 100 * ind,1], 1)#A
figures[fig_num+1].add_link(1, [100 * ind, 10 * ind, 100 * ind,1])#A1, C1, E1


figures[fig_num+1].add_node([10 * ind, 10 * ind, 10 * ind,1], 2)#B
#figures[fig_num+1].add_link(2, [10 * ind, 100 * ind, 10 * ind,1])#B1, D1, F1

figures[fig_num+1].add_node([100 * ind, 10 * ind, 10 * ind,1], 3)#C
figures[fig_num+1].add_link(3, [100 * ind, 10 * ind, 100 * ind,1])#A1, C1, E1

figures[fig_num+1].add_node([100 * ind, 100 * ind, 10 * ind,1], 4)#D
figures[fig_num+1].add_link(4, [10 * ind, 100 * ind, 10 * ind,1])#B1, D1, F1

figures[fig_num+1].add_node([100 * ind, 100 * ind, 100 * ind,1], 5)#E
figures[fig_num+1].add_link(5, [100 * ind, 10 * ind, 100 * ind,1])#A1, C1, E1

figures[fig_num+1].add_node([10 * ind, 100 * ind, 100 * ind,1], 6)#F
figures[fig_num+1].add_link(6, [10 * ind, 100 * ind, 10 * ind,1])#B1, D1, F1

figures[fig_num+1].add_node([-20 * ind, 55 * ind, 100 * ind,1], 7)#Q
figures[fig_num+1].add_link(7, [10 * ind, 10 * ind, 100 * ind,1])#A

figures[fig_num+1].add_node([-20 * ind, 55 * ind, 10 * ind,1], 8)#W
figures[fig_num+1].add_link(8, [10 * ind, 10 * ind, 10 * ind,1])#B
figures[fig_num+1].add_link(8, [10 * ind, 100 * ind, 10 * ind,1])#B1, D1, F1
#
# figures[fig_num+1].add_node([10 * ind, 100 * ind, 100 * ind,1],7)
#
# figures[fig_num+1].add_node([55 * ind, -30 * ind, 100 * ind,1],8)
# figures[fig_num+1].add_link(8, [100 * ind, 10 * ind, 100 * ind,1])
#
# figures[fig_num+1].add_node([55 * ind, -30 * ind, 10 * ind,1],9)
# figures[fig_num+1].add_link(9, [100 * ind, 10 * ind, 100 * ind,1])
# figures[fig_num+1].add_link(9, [100 * ind, 10 * ind, 10 * ind,1])

#
# figures.append(LinkedList())
#
# figures[fig_num+2].add_node([200 * ind, 50 * ind, 50 * ind,1], 1) #вершина
# figures[fig_num+2].add_link(1, [300 * ind, 100 * ind, 10 * ind,1]) #C
# figures[fig_num+2].add_node([300 * ind, 100 * ind, 100 * ind,1], 2) #A
# figures[fig_num+2].add_link(2, [300 * ind, 100 * ind, 10 * ind,1]) #C
# figures[fig_num+2].add_node([300 * ind, 10 * ind, 100 * ind,1], 3) #B
# figures[fig_num+2].add_link(3, [300 * ind, 100 * ind, 10 * ind,1]) #C
# figures[fig_num+2].add_node([200 * ind, 50 * ind, 50 * ind,1], 4) #вершина
#
#
# #figures[fig_num+2].add_link(1, [300 * ind, 100 * ind, 100 * ind,1]) #A
# #figures[fig_num+2].add_link(1, [300 * ind, 10 * ind, 100 * ind,1]) #B
# #
#
# figures[fig_num+2].add_node([300 * ind, 100 * ind, 10 * ind,1],2) #C
# figures[fig_num+2].add_link(1, [300 * ind, 10 * ind, 100 * ind,1]) #B
#
#
# figures[fig_num+2].add_node([200 * ind, 50 * ind, 50 * ind,1], 1) #вершина
# # figures[fig_num+2].add_link(3, [300 * ind, 10 * ind, 100 * ind,1]) #B
#
# figures[fig_num+2].add_node([300 * ind, 100 * ind, 100 * ind,1], 3) #A
# figures[fig_num+2].add_node([300 * ind, 100 * ind, 10 * ind,1],2) #C
#
#

def line_draw(point1, point2, color='black'):
    x0 = point1[0] + shift_x
    y0 = point1[1] + shift_y

    x1 = point2[0] + shift_x
    y1 = point2[1] + shift_y

    canvas.create_line([x0, y0], [x1, y1], fill=color)
    #рисуем красивые линии методами питона
    if 3 == 2:
        point_size = 5
        x = x0
        y = y0
        step = 1
        t = 0
        canvas.create_oval(x0, y0, x0 + point_size, y0 + point_size, width=0.1, fill=color)

        if abs(x1 - x0) > abs(y1 - y0):
            if x < x1:
                while int(x) < int(x1):
                    t = float((x - x0) / (x1 - x0))
                    y = y0 * (1 - t) + y1 * t
                    x += step
                    canvas.create_oval(x, y, x + point_size, y + point_size, width=0.1, fill=color)
            elif x > x1:
                while int(x) > int(x1):
                    t = float((x - x0) / (x1 - x0))
                    y = y0 * (1 - t) + y1 * t
                    x -= step
                    canvas.create_oval(x, y, x + point_size, y + point_size, width=0.1, fill=color)
        else:
            if y < y1:
                while int(y) < int(y1):
                    t = float((y - y0) / (y1 - y0))
                    x = x0 * (1 - t) + x1 * t
                    y += step
                    canvas.create_oval(x, y, x + point_size, y + point_size, width=0.1, fill=color)
            elif y > y1:
                while int(y) > int(y1):
                    t = float((y - y0) / (y1 - y0))
                    x = x0 * (1 - t) + x1 * t
                    y -= step
                    canvas.create_oval(x, y, x + point_size, y + point_size, width=0.1, fill=color)


def line_draw_fill(point1, point2, color):
    x0 = point1[0]
    y0 = point1[1]

    x1 = point2[0]
    y1 = point2[1]

    point_size = 5

    x = x0
    y = y0
    step = 1
    t = 0
    canvas.create_oval(x0, y0, x0 + point_size, y0 + point_size, width=0.1, fill=color)

    if (x1 - x0) > (y1 - y0):
        while int(x) < int(x1):
            t = float((x - x0) / (x1 - x0))
            y = y0 * (1 - t) + y1 * t
            x += step
            canvas.create_oval(x, y, x + point_size, y + point_size, width=0.1, fill=color)
        if x == x0:
            while int(x) > int(x1):
                t = float((x - x0) / (x1 - x0))
                y = y0 * (1 - t) + y1 * t
                x -= step
                canvas.create_oval(x, y, x + point_size, y + point_size, width=0.1, fill=color)
    else:
        while int(y) < int(y1):
            t = float((y - y0) / (y1 - y0))
            x = x0 * (1 - t) + x1 * t
            y += step
            canvas.create_oval(x, y, x + point_size, y + point_size, width=0.1, fill=color)
        if y == y0:
            while int(y) > int(y1):
                t = float((x - x0) / (x1 - x0))
                y = y0 * (1 - t) + y1 * t
                x -= step
                canvas.create_oval(x, y, x + point_size, y + point_size, width=0.1, fill=color)


def triangle_draw(triangle):
    i = 0
    min_point = triangle[0]
    mid_point = triangle[0]
    max_point = triangle[0]

    while i < 3:
        if min_point[1] > triangle[i][1]:
            min_point = triangle[i]
        if max_point[1] < triangle[i][1]:
            max_point = triangle[i]
        i += 1
    i = 0
    while i < 3:
        if triangle[i][1] != min_point[1] and triangle[i][1] != max_point[1]:
            mid_point = triangle[i]
        i += 1

    line_draw(min_point, max_point, "red")
    line_draw(min_point, mid_point, "green")
    line_draw(max_point, mid_point, "green")


########
# преобразуют координаты 1й точки

def transofrmation(pt, tf_type):
    '''rectangular_isometry = 0
        rectangular_dimetry = 1
        horizontal_oblique_isometry = 2
        durer_method = 3'''
    if tf_type==0 or tf_type==1 or tf_type==2:
        if tf_type == 0:
            a11 = cos(pi / 6)
            a12 = -a11
            a13 = 0
            a21 = -sin(pi / 6)
            a22 = -sin(pi / 6)
            a23 = 1
        elif tf_type == 1:
            a11 = cos(0.13)
            a12 = -0.5 * cos(0.72)
            a13 = 0
            a21 = -sin(0.13)
            a22 = -0.5 * sin(0.72)
            a23 = 1
        elif tf_type == 2:
            a11 = cos(pi / 6)
            a12 = -sin(pi / 6)
            a13 = 0
            a21 = -sin(pi / 6)
            a22 = -cos(pi / 6)
            a23 = 1
        u = a11 * pt[0] + a12 * pt[1] + a13 * pt[2]
        v = a21 * pt[0] + a22 * pt[1] + a23 * pt[2]
        return [u, v]

    if tf_type == 3:
        # d - расстояние от наблюдателя до картины
        # h - высота наблюдения
        # u - x
        # v - y
        # x0, y0 - точки начала координат
        # xu, yu -
        # mx, my -
        # m_corr -
        # max_x, max_y - разрешение
        max_x = 500
        max_y = 500
        max_z = 100
        m_corr = (4 * max_x) / (3 * max_y)

        d = max_y*0.1
        h = max_z / 2
        u0 = max_x

        u = (d * pt[0]) / (d + pt[1])
        v = (d * (pt[2] - h)) / (d + pt[1]) + h

        return [u, v]




def rotate(pt, tf_type):
    '''left = 4
        right = 5
        up = 6
        down = 7'''
    if tf_type == 4:
        rx = np.array([[1, 0,          0,          0],
                       [0, cos(angle), sin(angle), 0],
                       [0, -sin(angle),cos(angle, ), 0],
                       [0, 0,           0, 1]], float)
        np.array(pt)
        return np.dot(pt, rx)
    if tf_type == 5:
        rx = np.array([[1, 0, 0, 0],
                       [0, cos(-angle), sin(-angle), 0],
                       [0, -sin(-angle), cos(-angle, ), 0],
                       [0, 0, 0, 1]], float)
        a = np.array(pt)
        # print('!',a)
        return np.dot(pt, rx)
    if tf_type == 6:
        rx = np.array([[cos(angle), sin(angle), 0, 0],
                       [-sin(angle), cos(angle), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]], float)
        a = np.array(pt)
        # print('!',a)
        return np.dot(pt, rx)
    if tf_type == 7:
        rx = np.array([[cos(-angle), sin(-angle), 0, 0],
                       [-sin(-angle), cos(-angle), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]], float)
        a = np.array(pt)
        # print('!',a)
        return np.dot(pt, rx)

#для вращения
# rx = np.array([[cos(-angle), 0, -sin(-angle), 0],
#                        [0, 1, 0, 0],
#                        [sin(-angle), 0, cos(-angle, ), 0],
#                        [0, 0, 0, 1]], float)

def done_rotate (figure, tf_type):
    next_node = figure.head
    if next_node!= None:
        next_node.t_value = rotate(next_node.t_value, tf_type)
        temp_links = []
        for link in next_node.links:
            temp_links.append (rotate(link, tf_type))
        next_node.links = temp_links
    while next_node.next:
        next_node = next_node.next
        next_node.t_value = rotate(next_node.t_value, tf_type)
        temp_links = []
        for link in next_node.links:
            temp_links.append (rotate(link, tf_type))
        next_node.links = temp_links



    # for link in next_node.links:
    #     link = rotate(link, tf_type)


def done_transofrmation(figure, tf_type, color):
    ''' если tf_type < 4 - это вывод на экран
        если больше - это вращение'''
    next_node = figure.head

    while next_node.next:
        next_node_1 = next_node.next
        line_draw(transofrmation(next_node.t_value, tf_type), transofrmation(next_node_1.t_value, tf_type), color)

        # для маркировки точек
        # label_x = transofrmation(next_node.value, tf_type)[0] + shift_x + 20
        # label_y = transofrmation(next_node.value, tf_type)[1] + shift_y + 20
        # canvas.create_text(label_x, label_y, text=next_node.name, fill='white')
        #
        # label_x = transofrmation(next_node_1.value, tf_type)[0] + shift_x + 20
        # label_y = transofrmation(next_node_1.value, tf_type)[1] + shift_y + 20
        # canvas.create_text(label_x, label_y, text=next_node_1.name, fill='grey')

        for link in next_node.links:
            line_draw(transofrmation(next_node.t_value, tf_type), transofrmation(link, tf_type),color)
        next_node = next_node.next

    for link in next_node.links:
         line_draw(transofrmation(next_node.t_value, tf_type), transofrmation(link, tf_type), color)


def draw(linear_transformation):

    for fig in figures:
        if fig == None:
            break
        done_transofrmation(fig, linear_transformation, line_color)

def rotate_left():
    canvas.create_rectangle(0, 0, 824, 620, fill=bg_color)
    for fig in figures:
        if fig == None:
            break
        done_rotate(fig, 4)
        done_transofrmation(fig, linear_transformation, line_color)


def rotate_right():
    canvas.create_rectangle(0, 0, 824, 620, fill=bg_color)
    for fig in figures:
        if fig == None:
            break
        done_rotate(fig, 5)
        done_transofrmation(fig, linear_transformation, line_color)


def rotate_up():
    canvas.create_rectangle(0, 0, 824, 620, fill=bg_color)
    for fig in figures:
        if fig == None:
            break
        done_rotate(fig, 6)
        done_transofrmation(fig, linear_transformation, line_color)

def rotate_down():
    canvas.create_rectangle(0, 0, 824, 620, fill=bg_color)
    for fig in figures:
        if fig == None:
            break
        done_rotate(fig, 7)
        done_transofrmation(fig, linear_transformation, line_color)

draw(linear_transformation)

# line_draw(transofrmation([10,100,100], linear_transformation), transofrmation([10,100,10], linear_transformation), 'green')
# line_draw([10, 10, 100],  [10, 10, 10], 'red')


btn_left = Button(root, text='Rotate left',  command=rotate_left)
btn_left.pack(side="left")
btn_right = Button(root, text='Rotate right', command=rotate_right)
btn_right.pack(side="right")
btn_up = Button(root, text='Rotate up', command=rotate_up)
btn_up.pack(side="top")
btn_down = Button(root, text='Rotate down', command=rotate_down)
btn_down.pack(side="bottom")



root.mainloop()
