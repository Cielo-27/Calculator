from tkinter  import *

class Calculator():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.entry1 = Entry(master)
        self.entry1.pack()
        self.entry2 = Entry(master)
        self.entry2.pack()
        self.label = Label(master).pack()
        self.button1 = Button(master, text="Adding", command=None).pack(side=TOP)
root = Tk()
calc = Calculator(root)
root.mainloop()
        
