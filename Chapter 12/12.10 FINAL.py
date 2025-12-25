from tkinter import *
import random 

class Car(Canvas):
    def __init__(self, window, colour):
        super().__init__(window, width=700, height=50, bg='white')
        self.car_tag = 'car' + colour
        self.create_rectangle(0, 20, 50, 30, fill=colour, tags=self.car_tag)
        self.create_polygon(10, 20, 20, 10, 30, 10, 40, 20, fill='black', outline='black', tags=self.car_tag)
        self.create_oval(10, 30, 20, 40, fill='black', outline='black', tags=self.car_tag)
        self.create_oval(30, 30, 40, 40, fill='black', outline='black', tags=self.car_tag)
        self.pack(pady=5)

    def move_car(self):
        dx = random.randint(1, 20)
        self.move(self.car_tag, dx, 0)
        bbox = self.bbox(self.car_tag)
        if bbox[2] < 700:
            self.after(50, self.move_car)

def start_race():
    car1.move_car()
    car2.move_car()
    car3.move_car()
    car4.move_car()

window = Tk()
window.title("4 Racing Cars")
window.geometry('720x350')

car1 = Car(window, 'gray')
car2 = Car(window, 'blue')
car3 = Car(window, 'red')
car4 = Car(window, 'green')

Button(window, text="Start Race", command=start_race).pack(pady=10)

window.mainloop()