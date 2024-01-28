from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=3, row=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=4, row=0)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=5, row=0)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=3, row=2)

window.mainloop()
