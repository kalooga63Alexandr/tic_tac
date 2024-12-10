import tkinter
import random
import time


window = tkinter.Tk()
listt = []

class TicTacToe(tkinter.Canvas):
 
    def __init__(self, window):
        super().__init__(window, height=300, width=300)
        self.bind('<Button-1>', self.click)
        self.state = [None, ] * 9
        self.list_move = [i for i in range(0, 9)]

    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill='grey')
        self.create_line(200, 0, 200, 300, fill='grey')
        self.create_line(0, 100, 300, 100, fill='grey')
        self.create_line(0, 200, 300, 200, fill='grey')

    def click(self, event):
        column = event.x // 100
        row = event.y // 100
        i = column + row * 3
        if self.state[i] is None:
            self.state[i] = 'x'
            self.add_x(column, row)
        else:
            print('Занято')   
        res = self.get_winner()
        if res == 'x_win':
            self.text(res)
            self.update()
        else:
            self.text(res)
            self.update()                
        self.bot_move(i) 
        res = self.get_winner()
        if res == 'o_win':
            self.text(res)
            self.update()
        else:
            self.text(res)
            self.update() 
        if res is not None:
            time.sleep(2)
            self.state = [None, ] * 9
            self.delete(*listt)
            self.list_move.clear()
            self.list_move = [i for i in range(0, 9)]    
    def add_x(self, column, row):
        x = column * 100
        y = row * 100
        li = self.create_line(10+x, 10+y, 90+x, 90+y, width=5, fill='green',  tags='li')
        lit = self.create_line(10+x, 90+y, 90+x, 10+y, width=5, fill='green', tags='li')
        listt.append(li)
        listt.append(lit)       

    def add_o(self, column, row):
        x = column * 100
        y = row * 100
        li = self.create_oval(10+x, 10+y, 90+x, 90+y, width=5, outline='red', tags='li') 
        listt.append(li)   

   
    def bot_move(self, i):
        state = self.state
        victory = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        s = [s for s, n in enumerate(state) if n == 'x']
                          
        if None in self.state: 
            while True:
                ran = random.randint(0, 8)
                if self.state[ran] is None:
                    break
            self.state[ran] = 'o'
            column = ran % 3
            row = ran // 3
            self.add_o(column, row)
        
    def get_winner(self):  
        state = self.state
        if (state[0] == 'x' and state[1] == 'x' and state[2] == 'x') or (state[3] == 'x' and state[4] == 'x' and state[5] == 'x') or (state[6] == 'x' and state[7] == 'x' and state[8] == 'x'):
            return 'x_win'       
        elif (state[0] == 'o' and state[1] == 'o' and state[2] == 'o') or (state[3] == 'o' and state[4] == 'o' and state[5] == 'o') or (state[6] == 'o' and state[7] == 'o' and state[8] == 'o'):
            return 'o_win'
        elif (state[0] == 'x' and state[3] == 'x' and state[6] == 'x') or (state[1] == 'x' and state[4] == 'x' and state[7] == 'x') or (state[2] == 'x' and state[5] == 'x' and state[8] == 'x'):
            return 'x_win'        
        elif (state[0] == 'o' and state[3] == 'o' and state[6] == 'o') or (state[1] == 'o' and state[4] == 'o' and state[7] == 'o') or (state[2] == 'o' and state[5] == 'o' and state[8] == 'o'):
            return 'o_win'
        elif (state[0] == 'x' and state[4] == 'x' and state[8] == 'x') or (state[2] == 'x' and state[4] == 'x' and state[6] == 'x'):
            return 'x_win'       
        elif (state[0] == 'o' and state[4] == 'o' and state[8] == 'o') or (state[2] == 'o' and state[4] == 'o' and state[6] == 'o'):
            return 'o_win'
        elif not None in state:
            return 'draw'
        else:
            return None
        
    def text(self, tr):
        li = self.create_text(150, 120, text=tr, fill='green1', font=("Arial", 60), tags='li')
        listt.append(li)
  
game = TicTacToe(window)
game.draw_lines()
game.pack()
window.mainloop()