import tkinter as tk
from tkinter import Label, Button
import speedtest

# Function to check the internet speed
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10**6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10**6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

# Create the main window
sp = tk.Tk()
sp.title("Internet Speed Test")
sp.geometry("500x400")
sp.config(bg="black")

# Create and place labels and buttons
title_label = Label(sp, text="Internet Speed Test", font=("Arial", 20, "bold"), bg="black", fg="white")
title_label.place(x=100, y=10)

download_label = Label(sp, text="Download Speed", font=("Arial", 20, "bold"), bg="black", fg="white")
download_label.place(x=100, y=60)

lab_down = Label(sp, text="00", font=("Arial", 20, "bold"), bg="black", fg="white")
lab_down.place(x=100, y=100)

upload_label = Label(sp, text="Upload Speed", font=("Arial", 20, "bold"), bg="black", fg="white")
upload_label.place(x=100, y=150)

lab_up = Label(sp, text="00", font=("Arial", 20, "bold"), bg="black", fg="white")
lab_up.place(x=100, y=190)

check_button = Button(sp, text="Check Speed", font=("Arial", 20, "bold"), bg="black", fg="white", relief=tk.RAISED, command=speedcheck)
check_button.place(x=100, y=250)

# Start the main event loop
sp.mainloop()
