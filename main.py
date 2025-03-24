from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow



class Bill_App:
     def __init__(self,root) -> None:
      self.root=root
      self.root.geometry("1440x900+0+0")
      self.root.title("Billing Software") 






if __name__ == '__main__':
    root=Tk()
    object=Bill_App(root)
    root.mainloop()