from anahori import *
import tkinter
import tkinter.messagebox
import time
import random
key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

mx = 1
my = 1
yuka = 0
t1 = time.time()
def main_proc():
    global mx, my, yuka, yukamax
    canvas.delete("MYCHR")
    canvas.create_image(mx*40 + 20, my*40 + 20, image=img, tag="MYCHR")
    if mx == size_x - 2 and my == size_y - 2:
        tkinter.messagebox.showinfo("maze", "GOAL!")
        map()
        mx = 1
        my = 1
    if key == "Up" and m.maze[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and m.maze[my+1][mx] == 0:
        my = my + 1
    if key == "Left" and m.maze[my][mx-1] == 0:
        mx = mx - 1
    if key == "Right" and m.maze[my][mx+1] == 0:
        mx = mx + 1
    root.after(100, main_proc)
root = tkinter.Tk()
root.title("maze")
root.bind("<KeyPress>", key_down) 
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=1940, height=1040, bg="black")
canvas.pack()
def map():
    canvas.delete("way")
    anahori()
    for y in range(m.size_y):
        for x in range(m.size_x):
            if m.maze[y][x] == 0:
                if x == 1 and y == 1:
                    canvas.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill="lightgreen", tag="start")
                elif x == size_x - 2 and y == size_y - 2:
                    canvas.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill="pink", tag="goal")
                else:
                    canvas.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill="white", tag="way")
                    

map()

img = tkinter.PhotoImage(file="image small.png")
canvas.create_image(mx * 40  + 20, my * 40 + 20, image=img, tag="MYCHR")
main_proc()
root.mainloop()