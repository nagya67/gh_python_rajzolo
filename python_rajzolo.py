import time
from tkinter import *
from random import randrange, random
import math
abl1=Tk()
label_font=('Comic Sans Ms', 12)
colors=['white','black','grey','brown','red','salmon','sienna','coral','orange','gold','olive','yellow','lightgreen',
        'green','lime','teal','cyan','navy','blue','indigo','violet','purple','magenta','pink']
all_figure=[]
polygons=['point','radius','line','endless_line','circle','triangle','square','polygon', 'stripe']
alakzatok=['pont','sugár','szakasz','egyenes','kör','háromszög','négyzet','sokszög','sáv']
myColor=StringVar
myDataX=IntVar
myDataY=IntVar
polygon_var=[]
selected_polygons=[]

# y a vászon magassága, szélessége
y=700
# size az alakzat 'mérete'
size_standard=100
size=IntVar

color_var=[]
color_buttons=[]

Label(abl1,text='alakzat színe:',font=label_font).grid(row=0,column=15)
for x in range(len(colors)):
    color_var.append(IntVar())
    color_buttons.append('cb_'+colors[x])
    color_buttons[x]=Checkbutton(abl1,text=colors[x],variable=color_var[x],bg=colors[x])
    color_buttons[x].grid(row=x+1,column=15)
    color_buttons[x].select()
none=IntVar()
all=IntVar()

def all_function():
    for x in range(len(color_buttons)):
        color_buttons[x].select()
def none_function():
    for x in range(len(color_buttons)):
        color_buttons[x].deselect()
Button(abl1,text='EGYIK SE', command=none_function).grid(row=len(colors)+1, column=15)
Button(abl1,text='ÖSSZES',command=all_function).grid(row=len(colors)+2,column=15)

def change_bg():
    canv1['background']=bg_var.get()

Label(abl1,text='háttér színe:',font=label_font).grid(row=0,column=16)
bg_buttons=[]
bg_var=StringVar()
for x in range(len(colors)):
    bg_buttons.append('bg_'+colors[x])
    bg_buttons[x]=Radiobutton(abl1,text=colors[x],bg=colors[x],variable=bg_var,value=colors[x], command=change_bg)
    bg_buttons[x].grid(row=x+1,column=16)
bg_buttons[0].select()

canv1=Canvas(abl1,height=y,width=y,bg='black')
canv1.grid(row=0,rowspan=len(colors)+3,column=0,columnspan=14)

Label(abl1, text='ennyiszer:',font=label_font).grid(row=0,column=17)
how_many=['1','10','100','200','500','1000','2000','5000', '10000']

how_many_buttons=[]
hmb_var=StringVar()

for x in range(len(how_many)):
    how_many_buttons.append('hmb_'+ str(how_many[x]))
    how_many_buttons[x]=Radiobutton(abl1,text=how_many[x],variable=hmb_var,value=how_many[x])
    how_many_buttons[x].grid(row=x+1,column=17)
how_many_buttons[5].select()

selected_colors=[]
def check_colors():
    global selected_colors
    selected_colors=[]
    for x in range(len(color_var)):
        if color_var[x].get()==1:
            selected_colors.append(colors[x])

polygon_buttons=[]

Label(abl1,text='alakzat:',font=label_font).grid(row=len(how_many)+2,column=17)
for x in range(len(polygons)):
    polygon_var.append(StringVar())
    polygon_buttons.append('pg_'+polygons[x])
    polygon_buttons[x]=Checkbutton(abl1,text=alakzatok[x],variable=polygon_var[x])
    polygon_buttons[x].grid(row=len(how_many)+3+x,column=17)
    polygon_buttons[x].deselect()
polygon_buttons[1].select()

counter=0

def distance_from_centre(do_it):
    global myDataX, myDataY, y
    while do_it==True:
        myDataX=randrange(y)
        myDataY=randrange(y)
        myDistance=int(math.sqrt((myDataX-y/2)**2+(myDataY-y/2)**2))
        myRandom=random()
        percentage=0.8
        if (myDistance<100 and myRandom>0.3) \
        or (myDistance>=100 and myDistance<200 and myRandom>0.85) \
        or (myDistance>=200 and myRandom>0.95):
            do_it= False


def draw_triangle():
    global myDataX,myDataY,myColor,size
    triangle_datas=[]

    for x in range(6):
        if x%2==0:
            triangle_datas.append(myDataX+randrange(size))
        else:
            triangle_datas.append(myDataY+randrange(size))
            
    canv1.create_polygon(triangle_datas,fill=myColor,outline=myColor)
    triangle_datas+=[myColor,'triangle']
    all_figure.append(triangle_datas)
    print("YYYYYYYYYYYYYYYYy")
    print(triangle_datas)
    print(all_figure)


def draw_circle():
    global myDataX,myDataY,myColor,size
    circle_datas=[]
    circle_datas.append(myDataX)
    circle_datas.append(myDataY)
    circle_datas.append(myDataX+size/2)
    circle_datas.append(myDataY+size/2)
    canv1.create_oval(circle_datas, fill=myColor,outline=myColor)
    circle_datas+=[myColor,'circle']
    all_figure.append(circle_datas)

def draw_line():
    global myDataX,myDataY,myColor
    line_datas=[myDataX,myDataY,myDataX+size,myDataY+size]
    canv1.create_line(line_datas, fill=myColor)
    line_datas+=[myColor,'line']
    all_figure.append(line_datas)

def draw_point():
    global myDataX,myDataY,myColor
    line_datas=[]
    x1=randrange(700)
    y1=randrange(700)
    line_datas+=[x1,y1,x1+5,y1+5]
    canv1.create_oval(line_datas, fill=myColor, outline=myColor)
    line_datas+=[myColor,'point']
    all_figure.append(line_datas)

def draw_endless_line():
    global myDataX,myDataY,myColor
    line_datas=[]
    control=-10
    my_rnd=-10
    for x in range(2):
        while control==my_rnd:
            my_rnd=int(randrange(4))
        if my_rnd==0:
            line_datas.append(0)
            line_datas.append(randrange(y))
        if my_rnd==1:
            line_datas.append(randrange(y))
            line_datas.append(0)
        if my_rnd==2:
            line_datas.append(700)
            line_datas.append(randrange(y))
        if my_rnd==3:
            line_datas.append(randrange(y))
            line_datas.append(700)
        control=my_rnd

    canv1.create_line(line_datas, fill=myColor)
    line_datas+=[myColor,"no","endless_line"]

def draw_radius():
    global myDataX,myDataY,myColor
    line_datas=[0,0,myDataX,myDataY]
    canv1.create_line(line_datas, fill=myColor)
    line_datas+=[myColor,'radius']
    all_figure.append(line_datas)

def draw_square():
    global myDataX,myDataY,myColor,size
    c=math.sqrt(2)*size
    alpha=math.radians(randrange(90))
    X=c*math.cos(alpha)
    Y=c*math.sin(alpha)
    X2=myDataX+X
    Y2=myDataY+Y
    X3=X2-Y
    Y3=Y2+X
    X4=X3-X
    Y4=Y3-Y
    line_datas=[myDataX,myDataY,X2,Y2,X3,Y3,X4,Y4]
    canv1.create_polygon(line_datas,fill=myColor)
    line_datas+=[myColor,'square']
    all_figure.append(line_datas)

def draw_polygon():
    global myDataX,myDataY,myColor,size, centre, mySlide
    polygon_counter=randrange(4,9)
    line_datas=[]
    for z in range(polygon_counter):    
        X1=randrange(size)
        Y1=randrange(size)
        line_datas+=line_datas+[myDataX+X1,myDataY+Y1]
    canv1.create_polygon(line_datas, fill=myColor)
    line_datas+=[myColor,'polygon']
    all_figure.append(line_datas)

def draw_stripe():
    global myDataX, myDataY, size
    line_datas=[0,myDataX,700,myDataY,700,myDataY+size,0,myDataX+size]
    canv1.create_polygon(line_datas,fill=myColor)
    line_datas+=[myColor,'stripe']
    all_figure.append(line_datas)

def check_polygons():
    global polygons, selected_polygons, polygon_var
    selected_polygons=[]
    for x in range(len(polygon_var)):
        if int(polygon_var[x].get())==1:
            selected_polygons.append(polygons[x])

def draw_something():
    global myDataX, myDataY, counter, hmb_var, selected_polygons, myColor, sizing, mySlide, size_standard, size

    #alakzat középpontól való távolsága
    if centre.get()==1:
        myDataX,myDataY=randrange(y),randrange(y)
    else:
        do_it= True
        distance_from_centre(do_it)

    #alakzat színe
    myColor=selected_colors[randrange(len(selected_colors))]

    #az alakzat mérete
    if sizing.get()==0:
        size=randrange(size_standard)
    else:
        size=size_standard

    #milyen alakzat és az azt előállító függvény
    my_rnd=randrange(len(selected_polygons))
    eval('draw_'+selected_polygons[my_rnd])()

def drawing():
    global counter, hmb_var, selected_polygons, myColor, sizing, mySlide, size_standard, size
    check_colors()
    check_polygons()
    limit=int(hmb_var.get())
    counter=0
    size_standard=mySlide.get()

    while counter<limit:
        draw_something()
        counter+=1

line_datas=[]
color=StringVar()
def drawing_again():
    global all_figure,line_datas,color
    print("itt")
    print(all_figure)
    for x in range(len(all_figure)):
        line_datas=[]
        for y in range(len(all_figure[x])-2):
            line_datas.append(all_figure[x][y])
        if all_figure[x][len(all_figure[x])-1]=='triangle':
            color=all_figure[x][len(all_figure[x])-2]
        print("most")
        print(color)
        print(line_datas)
        canv1.create_polygon(line_datas,fill=color)

def clear_canvas():
    global all_figure
    canv1.delete('all')
    all_figure=[]

all_figure_2=[]

def rotation():
    global all_figure,all_figure_2
    all_figure_2=[]
    for x in range(len(all_figure)):
        line_datas=[]
        for y in range(len(all_figure[x])-2):
            line_datas.append(0)
        for y in range(len(line_datas)):
            if y%2==0:
                line_datas[y+1]=(700-all_figure[x][y])
                print("XXXXX")
                print(line_datas)
            else:
                line_datas[y-1]=(700-all_figure[x][y])
                print("XXXXX--------------")
                print(line_datas)
            
        line_datas.append(all_figure[x][len(all_figure[x])-2])
        line_datas.append(all_figure[x][len(all_figure[x])-1])
        all_figure_2.append(line_datas)
       
    clear_canvas()
    all_figure=all_figure_2.copy()
    print("WWWWWWWWWWWWWWWWWw")
    print(all_figure)
    drawing_again()


Label(abl1,text='alakzat mérete:',font=label_font).grid(row=0,column=18)
mySlide=Scale(abl1,from_=10,to=500,orient=HORIZONTAL)
mySlide.set(200)
mySlide.grid(row=1,column=18)

sizing=IntVar()
Radiobutton(abl1,text='ekkora és ennél kisebb',variable=sizing,value=0).grid(row=2,column=18)
Radiobutton(abl1,text='az összes ekkora',variable=sizing,value=1).grid(row=3,column=18)

Label(abl1,text='alakzatok eloszlása:',font=label_font).grid(row=5,column=18)
centre=IntVar()
Radiobutton(abl1,text='közép felé sűrűsödik',variable=centre,value=0).grid(row=6,column=18)
Radiobutton(abl1,text='egyenletes eloszlás',variable=centre,value=1).grid(row=7,column=18)

buttonFont=('Arial',16, 'bold')
button1=Button(abl1,text='(rá)rajzol',bg='#d3d3d3',font=buttonFont,command=drawing)
button1.grid(row=9, rowspan=3,column=18,columnspan=2,sticky=N+E+S+W)
button2=Button(abl1,text='töröl', bg='#d3d3d3',font=buttonFont, command=clear_canvas)
button2.grid(row=13,rowspan=3,column=18,columnspan=2,sticky=N+E+S+W)
button3=Button(abl1,text='elforgat', bg='#d3d3d3',font=buttonFont, command=rotation)
button3.grid(row=17,rowspan=3,column=18,columnspan=2,sticky=N+E+S+W)
#for x in range(50000):
    #draw_triangle()
    #time.sleep(0.5)


abl1.mainloop()
abl1.destroy()
