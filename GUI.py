import tkinter as tk

h = input("Enter the height ")
l = input("Enter the length ")

Method = tk.Tk()

canvas = tk.Canvas(Method, height=h, width=l)
canvas.pack()

frame = tk.Frame(Method, bg='#6108cd')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
#image attributes and tk description
background_image1 = tk.PhotoImage(file='SouthIndia.png')
background_label1 = tk.Label(Method, image=background_image1)
background_label1.place(relwidth=1.5, relheight=1.5)
background_image2 = tk.PhotoImage(file='NorthIndia.png')
background_label2 = tk.Label(Method, image=background_image2)
background_label2.place(relwidth=0.5, relheight=0.5)
Method.mainloop()
