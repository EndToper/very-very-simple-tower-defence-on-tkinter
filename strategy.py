import tkinter as tk
import random as r
from tkinter import messagebox as mb
count = 10
money = 250
t_c = 50
health = 5
speed = 1
window= tk.Tk()
evil_army = []
evil_army_2 = []
window.geometry("1000x500")
pixelVirtual = tk.PhotoImage(width=1, height=1)
clear_l = tk.Label(text=" "*100)
clear_l.place(x = 900, y = 0)
label_count = tk.Label(text=f"Money: {money}")
label_count.place(x = 900, y = 0)
towers_mass=[]
qavb =  True
class towers():
    def __init__(self,number,idificator):
        self.num = number
        self.power = 1
        self.id = idificator
    def hit(self):
        for i in range(len(evil_army)):
            if evil_army[i].pos+1 == self.num:
                evil_army[i].health -= self.power



class enemy():
    def __init__(self,h,s,r,a):
        self.health = h
        self.speed = s
        self.pos = r
        self.x = 950
        self.alive = a
        self.vie = tk.Button(window, text=" ", height = 25, width = 25,  compound="c", image=pixelVirtual)
        self.vie.png = tk.PhotoImage(file="enemy.png")
        self.vie['image'] = self.vie.png
        self.vie.place(x = self.x,y = 25+100*self.pos)
    def go(self):
        global health,money, evil_army, qavb
        if self.alive == True:
            self.x -= 10
            self.vie.place(x = self.x,y = 25+100*self.pos)
            if self.health <= 0:
                self.vie.place(x = 10000,y = 10000)
                health += 1
                money += 5
                self.alive = False
                clear_l = tk.Label(text=" "*100)
                clear_l.place(x = 900, y = 0)
                label_count = tk.Label(text=f"Money: {money}")
                label_count.place(x = 900, y = 0)
            if self.x == 250:
                exit()
def gl(e):
    print(e.keysym)
    global qavb
    if e.keysym == "g" and qavb == True:
        rand = r.randint(1,5)
        for i in range(rand):
            ran = r.randint(0,4)
            en = enemy(health, speed, ran, True)
            evil_army.append(en)
            qavb = False
    if e.keysym == "q":
        for i in range(len(towers_mass)):
            towers_mass[i].hit()
        for i in range(len(evil_army)):
            evil_army[i].go()
        wqawe = 0
        for i in range(len(evil_army)):
            wqawe += evil_army[i].health

        if wqawe < 1:
            qavb = True
        print(health)
def buy_tower(e):
    global towers_mass, money, label_count, t
    if money >= t_c * e.widget.tower:
        for i in range(len(towers_mass)):
            if towers_mass[i].id == e.widget.num:
                towers_mass[i].power += 1
                money = money - t_c * e.widget.tower
    if money >= t_c and e.widget.tower == 1:
        e.widget['image'] = e.widget.image_png
        e.widget['text'] = "1"
        tower = towers(e.widget.number,e.widget.num)
        towers_mass.append(tower)
        money = money - 50
        e.widget.tower += 1
    clear_l = tk.Label(text=" "*100)
    clear_l.place(x = 900, y = 0)
    label_count = tk.Label(text=f"Money: {money}")
    label_count.place(x = 900, y = 0)


x1,y1 = 0,0
btns = []
for i in range(1,count+1):
    btn = tk.Button(window, text="Buy Tower", height = 100, width = 100,  compound="c", image=pixelVirtual)
    btn.num = i
    btn.tower = 1
    btn.image_png = tk.PhotoImage(file="tower.png")
    #btn['image'] = btn.image_png
    btns.append(btn)

for btn in btns:
        btn.place(x = x1, y = y1)
        btn.number = int(y1 // 100) + 1
        if btn.num % 2 == 0:
            y1 = y1 + 100
            x1 = 0
        else:
            x1 = x1 + 100



window.bind('<KeyPress>', gl)
window.bind("<Button-1>", buy_tower)
window.mainloop()