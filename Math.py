import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def DisplayImage():
       display_label1.place(x = 0, y = 375)
       display_label2.place(x = 775, y = 275)
       display_label3.place(x = 0, y = 0)
       display_label4.place(x = 775, y = 25)
       text_label.place(x = 375, y = 330)
       
Canvas = tk.Canvas(root, height ='400', width='540')
Canvas.pack()

display_image1 = tk.PhotoImage(file='Mollweide.png')
display_label1 = tk.Label(root, image = display_image1)
display_image2 = tk.PhotoImage(file='Calculus.png')
display_label2 = tk.Label(root, image = display_image2)
display_image3 = tk.PhotoImage(file='BinomialTheorem.png')
display_label3 = tk.Label(root, image = display_image3)
display_image4 = tk.PhotoImage(file='Mandelbrot.png')
display_label4 = tk.Label(root, image = display_image4)

text_label = tk.Label(root,text = "These are some things that interest me.....")
        
Btn = tk.Button(root, text ="Some of the things I like! ", command = DisplayImage)
Btn.pack()
Btn.place(relx=0.4, rely=0.85, height=55, width=150)
tk.mainloop()