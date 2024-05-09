import tkinter as tk
from class_basket import Basket
from class_person import Person



root = tk.Tk(className= "golfsim")

title_label = tk.Label(root, text="DISK GOLF SIMULATOR")
prompt_label= tk.Label(root, text="Enter your name in the textbox and press enter to see nothing happen! Wow!")

person = Person()
basket = Basket()

entry_box = tk.Entry(root)
enter_button = tk.Button(root, text="Enter")
name_label = tk.Label(root, text=f"Your character's name is {person.name}.")
basket_num_label = tk.Label(root, text=f"The basket number is {basket.basket_num}.")
basket.coordinate_set()
basket_coord_label = tk.Label(root, text=f"The basket coordinates are {basket.coordinates}.")


title_label.pack()
prompt_label.pack()
entry_box.pack()
enter_button.pack()
name_label.pack()
basket_num_label.pack()
basket_coord_label.pack()

root.mainloop()

