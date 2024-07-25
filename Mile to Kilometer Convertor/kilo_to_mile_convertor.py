from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.minsize(width=300, height=150)
window.title("Mile to Kilometer Converter")
window.config(padx=15, pady=15)

miles_input = Entry(width=13)
miles_input.grid(row=0, column=2)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=3)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=2)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=1, column=3)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=3, column=2)

window.mainloop()
