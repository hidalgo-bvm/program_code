import tkinter
import time

w = tkinter.Tk()

def change_red(x):
    if x == "red" :
        x = "grey"
    else :
        x = "red"
    p.create_oval(50, 50, 75, 75, fill = x)
    print(x)
    return x

def change_yellow(x):
    if x == "yellow" :
        x = "grey"
    else :
        x = "yellow"
    p.create_oval(50, 80, 75, 105, fill = x)
    print(x)
    return x
    
def change_green(x):
    if x == "green" :
        x = "grey"
    else :
        x = "green"
    p.create_oval(50, 110, 75, 135, fill = x)
    print(x)
    return x

p = tkinter.Canvas(master = w, width = 300, heigth = 200, bg = "white")
p.pack()
clr = "grey"

p.create_oval(50, 80, 75, 105, fill = clr)
p.create_oval(50, 110, 75, 135, fill = clr)
for n in range(5) :
    p.create_oval(50, 50, 75, 75, fill = "red")
    time.sleep(3)
    count = 0
    timing = time.time()
    clr = "grey"
    while count < 8:
        if time.time() - timing > 0.50:
            timing = time.time()
            clr = change_red(clr)
            print(f"Change color: {clr}")
            count += 1
    p.create_oval(50, 80, 75, 105, fill = "yellow")
    time.sleep(2)
    count = 0
    timing = time.time()
    clr = "grey"
    while count < 8:
        if time.time() - timing > 0.50:
            timing = time.time()
            clr = change_yellow(clr)
            print(f"Change color: {clr}")
            count += 1
    p.create_oval(50, 110, 75, 135, fill = "green")
    time.sleep(5)
    count = 0
    timing = time.time()
    clr = "grey"
    while count < 8:
        if time.time() - timing > 0.50:
            timing = time.time()
            clr = change_green(clr)
            print(f"Change color: {clr}")
            count += 1
w.destroy()
w.mainloop()