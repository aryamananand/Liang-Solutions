from tkinter import *
import random

class PointGame24():
    def __init__(self):
        self.val1,self.val2,self.val3,self.val4 = 5,13,7,10
        self.real_numbers_list = [5,7,10,13]
        self.window = Tk()
        self.window.title('24-Point Game')
        self.window.geometry('400x160')
        self.frame1 = Frame(self.window)
        self.frame1.grid(row = 1, column = 1)
        self.frame2 = Frame(self.window)
        self.frame2.grid(row = 2, column = 1)
        self.frame3 = Frame(self.window)
        self.frame3.grid(row = 3, column = 1)

        # Buttons and label

        button_fns = Button(self.frame1, text = 'Find a Solution', command = self.find_solution)
        button_fns.grid(row=1,column=1)

        self.solution_string = StringVar()
        self.label = Entry(self.frame1, textvariable = self.solution_string, state = 'readonly').grid(row=1,column=2)
        self.solution_string.set("Solution to be displayed here.")
        
        button = Button(self.frame1, text = 'Refresh', command = self.refresh)
        button.grid(row=1,column=3)

        # Number display canvases

        self.canvas1 = Canvas(self.frame2, height = 60, width = 60, bg = 'white')
        self.canvas1.grid(row=1,column=1)
        self.canvas1.create_text(30,30,text=self.val1,fill='red')
        self.canvas2 = Canvas(self.frame2, height = 60, width = 60, bg = 'white')
        self.canvas2.grid(row=1,column=2)
        self.canvas2.create_text(30,30,text=self.val2,fill='red')
        self.canvas3 = Canvas(self.frame2, height = 60, width = 60, bg = 'white')
        self.canvas3.grid(row=1,column=3)
        self.canvas3.create_text(30,30,text=self.val3,fill='red')
        self.canvas4 = Canvas(self.frame2, height = 60, width = 60, bg = 'white')
        self.canvas4.grid(row=1,column=4)
        self.canvas4.create_text(30,30,text=self.val4,fill='red')

        # User input

        label = Label(self.frame3, text = 'Enter an expression:')
        label.grid(row=1,column=1,pady=5)
        
        self.eqnString = str()
        self.eqn = Entry(self.frame3, textvariable=self.eqnString)
        self.eqn.grid(row=1,column=2,pady=5) 

        button1 = Button(self.frame3, text = 'Verify', command = self.verify)
        button1.grid(row=1,column=3)

        self.window.mainloop()


    def find_solution(self):
        
        numbers =[self.val1, self.val2, self.val3, self.val4]

        operators = ['+','-','*','/']

        # 24 possibilities of number ordering
        permutations = [
            [numbers[0], numbers[1], numbers[2], numbers[3]],
            [numbers[0], numbers[1], numbers[3], numbers[2]],
            [numbers[0], numbers[2], numbers[1], numbers[3]],
            [numbers[0], numbers[2], numbers[3], numbers[1]],
            [numbers[0], numbers[3], numbers[1], numbers[2]],
            [numbers[0], numbers[3], numbers[2], numbers[1]],
            [numbers[1], numbers[0], numbers[2], numbers[3]],
            [numbers[1], numbers[0], numbers[3], numbers[2]],
            [numbers[1], numbers[2], numbers[0], numbers[3]],
            [numbers[1], numbers[2], numbers[3], numbers[0]],
            [numbers[1], numbers[3], numbers[0], numbers[2]],
            [numbers[1], numbers[3], numbers[2], numbers[0]],
            [numbers[2], numbers[0], numbers[1], numbers[3]],
            [numbers[2], numbers[0], numbers[3], numbers[1]],
            [numbers[2], numbers[1], numbers[0], numbers[3]],
            [numbers[2], numbers[1], numbers[3], numbers[0]],
            [numbers[2], numbers[3], numbers[0], numbers[1]],
            [numbers[2], numbers[3], numbers[1], numbers[0]],
            [numbers[3], numbers[0], numbers[1], numbers[2]],
            [numbers[3], numbers[0], numbers[2], numbers[1]],
            [numbers[3], numbers[1], numbers[0], numbers[2]],
            [numbers[3], numbers[1], numbers[2], numbers[0]],
            [numbers[3], numbers[2], numbers[0], numbers[1]],
            [numbers[3], numbers[2], numbers[1], numbers[0]]]

        found = False   # Initialise
        for nums in permutations:
            a, b, c, d = nums
            if eval(f"{a}+{b}+{c}+{d}") == 24:
                return f"{a}+{b}+{c}+{d}"
            elif eval(f"{a}*{b}*{c}*{d}") == 24:
                return f"{a}*{b}*{c}*{d}"
            else:
                for op1 in operators:   #loop of first operator
                    for op2 in operators:   # loop of second operator
                        for op3 in operators:   # loop of third operator
                            
                            expressions = [   # Concatenate the strings to form a single expression   
                                # 5 types of bracket arrangment
                                f"(({a}{op1}{b}){op2}{c}){op3}{d}",
                                f"({a}{op1}({b}{op2}{c})){op3}{d}",
                                f"{a}{op1}(({b}{op2}{c}){op3}{d})",
                                f"{a}{op1}({b}{op2}({c}{op3}{d}))",
                                f"({a}{op1}{b}){op2}({c}{op3}{d})"]
                            
                            for expr in expressions:
                                try:
                                    result = eval(expr)
                                except:
                                    continue
                                else:
                                    if result == 24:
                                        self.solution_string.set(expr)
                                        found = True
                                        self.solution_string.set(expr)
                                        return
        if not found:
            self.solution_string.set("No solution found.")


    def refresh(self):
        self.solution_string.set("Solution to be displayed here.")

        self.val1 = random.randint(1,13)
        self.canvas1.delete('all')
        self.canvas1.create_text(30,30,text=self.val1,fill='red')
        self.val2 = random.randint(1,13)
        self.canvas2.delete('all')
        self.canvas2.create_text(30,30,text=self.val2,fill='red')
        self.val3 = random.randint(1,13)
        self.canvas3.delete('all')
        self.canvas3.create_text(30,30,text=self.val3,fill='red')
        self.val4 = random.randint(1,13)
        self.canvas4.delete('all')
        self.canvas4.create_text(30,30,text=self.val4,fill='red')

        self.real_numbers_list = []
        self.real_numbers_list.append(self.val1)
        self.real_numbers_list.append(self.val2)
        self.real_numbers_list.append(self.val3)
        self.real_numbers_list.append(self.val4)
        self.real_numbers_list.sort()


    def verify(self):
        self.init_string = self.eqn.get()
        self.val = eval(self.init_string)
        
        if self.numbers_used() == self.real_numbers_list:
            if self.val == 24:
                self.correct()
            else:
                self.incorrect1()
        else:
            self.incorrect2()


    def correct(self):
        win2 = Toplevel(self.window)
        win2.title('Correct')
        win2.geometry('200x100')
        Label(win2).grid(row=1,column=1)
        Label(win2, text = 'You got it!', justify='center').grid(row=2,column=1)
        Label(win2).grid(row=3,column=1)
        Button(win2, text = 'Close', command = win2.destroy).grid(row=4,column=1)


    def incorrect1(self):
        win2 = Toplevel(self.window)
        win2.title('Incorrect')
        win2.geometry('160x100')
        Label(win2).grid(row=1,column=1)
        Label(win2, text = f'{self.init_string} = {self.val}, not 24.', justify='center').grid(row=2,column=1)
        Label(win2).grid(row=3,column=1)
        Button(win2, text = 'Close', command = win2.destroy).grid(row=4,column=1)


    def incorrect2(self):
        win2 = Toplevel(self.window)
        win2.title('Incorrect')
        win2.geometry('230x100')
        Label(win2).grid(row=1,column=1)
        Label(win2, text = 'You have to use the four cards shown.', justify='center').grid(row=2,column=1)
        Label(win2).grid(row=3,column=1)
        Button(win2, text = 'Close', command = win2.destroy).grid(row=4,column=1)

    def numbers_used(self):     # Returns list with ascending numbers (max 2 digit) used in equation with +,-,*,/
        init_string = self.eqn.get()
        print("init string: ", init_string)
        lst = list(init_string)
        lst = [x.strip() for x in lst if x.strip()] #remove trailing spaces
        print("list of items: ", lst)

        operators = ['+','-','*','/','(',')']
        number_list = []
        operator_list = []

        x = 0
        while x < len(lst):
            if lst[x] not in operators:     #if it is an integer
                if x != len(lst)-1 and lst[x+1] not in operators:    # if next digit is also integer
                    number_list.append(int(lst[x])*10+int(lst[x+1]))    #append 2 digit number
                    x += 2  # move on to the next next item of list
                    
                else:
                    number_list.append(int(lst[x]))
                    print("WORKING") 
                    x += 1
            else:
                operator_list.append(lst[x])
                x += 1
        number_list.sort()
        return number_list


PointGame24()