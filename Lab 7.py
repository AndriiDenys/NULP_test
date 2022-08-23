from tkinter import*
from random import*
import time



tk = Tk()
tk.title("Lab 7")
tk.resizable(False, False)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

tk.bind('<Button-1>', motion)



class Ball:
    def __init__(self, canvas, paddle, paddle1, color):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle1 = paddle1
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height() #поточна висота полотна
        self.canvas_width = self.canvas.winfo_width() #поточна ширина полотна
        #self.canvas.bind_all('<KeyPress-A>', self.turn_left)
        #self.canvas.bind_all('<KeyPress-D>', self.turn_right)
        self.hit_bottom = False

    def hit_paddle(self, pos):  #pos --> поточні координати м'яча
        paddle_pos = self.canvas.coords(self.paddle.id) #визначаємо координати ракетки і зберігаємо їх у змінну
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def hit_paddle1(self, pos):  #pos --> поточні координати м'яча
        paddle1_pos = self.canvas.coords(self.paddle1.id1) #визначаємо координати ракетки і зберігаємо їх у змінну
        if pos[2] >= paddle1_pos[0] and pos[0] <= paddle1_pos[2]:
            if pos[3] >= paddle1_pos[1] and pos[3] <= paddle1_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) #поточні координати х і у, за умови якщо є ідентифікатор
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def draw1(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) #поточні координати х і у, за умови якщо є ідентифікатор
        if pos[1] <=0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle1(pos) == True:
            self.y = -3
        if pos[0] <=0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<Button-1>', self.draw)
        self.canvas.bind_all('<KeyPress-Up>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Down>', self.turn_right)


    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)  # поточні координати х і у, за умови якщо є ідентифікатор
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2

class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id1 = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id1, 151, 209)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<Button-1>', self.draw)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)


    def draw(self):
        self.canvas.move(self.id1, self.x, 0)
        pos = self.canvas.coords(self.id1)  # поточні координати х і у, за умови якщо є ідентифікатор
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2

paddle = Paddle(canvas, 'blue')
paddle1 = Paddle1(canvas, 'blue')
ball = Ball(canvas, paddle, paddle1, 'red')
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        paddle1.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

