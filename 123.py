import tkinter as tk
import tkinter.ttk

class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.count = 0
        self.pack()
        self.create_widgets()


    def create_widgets(self):

        self.myscrollbar = tk.Scrollbar (self)
        self.myscrollbar.pack(side = "right")
        
        self.toplable = tk.Label(self,text = "\n/*******testing*******/\n\n", fg = "green")
        self.toplable.pack(side = "top")
        
        self.start = tk.Button(self)
        self.start["text"] = "Hello World\n(click me)"
        self.start["command"] = self.topclicked
    
        self.start.pack(side="top")
        
        self.middlelable = tk.Label(self,text = "\n")
        self.middlelable.pack()
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

        self.bottomlable = tk.Label(self,text = "By Leo", fg = "gray")
        self.bottomlable.pack(side = "bottom")

    def topclicked(self):
        self.count = self.count +1
        if self.count ==1:
            print("hi there, everyone!")
            self.start["text"] = str(self.count)+" times clicked"
            self.start["command"] = self.topclicked
        elif self.count <5:
            self.start["text"] = str(self.count)+" times clicked"
            self.start["command"] = self.topclicked
        elif self.count >=5:
            self.start["text"] = "done and exit"
            self.start["fg"] = "blue"
            self.start["command"] = root.destroy
        

root = tk.Tk()
root.title("GUI Test")
root.minsize(width = 250, height = 125)
app = App(master = root)
app.mainloop()

