import tkinter as tk

root = tk.Tk()

root.title("My First GUI")

label = tk.Label(root, text ="My First Design", font =("Calibri", 18))
label.pack(padx=28, pady=28)
textbox = tk.Text(root, height=1.5, font = ("Arial", 12))
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text ="1", font =("Arial", 12))
btn1.grid(row= 0, column=0, sticky= tk.W+ tk.E)

btn2 = tk.Button(buttonframe, text ="2", font =("Arial", 12))
btn2.grid(row= 0, column=1, sticky= tk.W+ tk.E)

btn3 = tk.Button(buttonframe, text ="3", font =("Arial", 12))
btn3.grid(row= 0, column=2, sticky= tk.W+ tk.E)

btn4 = tk.Button(buttonframe, text ="4", font =("Arial", 12))
btn4.grid(row= 1, column=0, sticky= tk.W+ tk.E)

btn5 = tk.Button(buttonframe, text ="5", font =("Arial", 12))
btn5.grid(row= 1, column=1, sticky= tk.W+ tk.E)

btn6 = tk.Button(buttonframe, text ="6", font =("Arial", 12))
btn6.grid(row= 1, column=2, sticky= tk.W+ tk.E)

buttonframe.pack(fill="x")

root.mainloop()
