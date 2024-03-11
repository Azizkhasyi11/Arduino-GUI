import tkinter as tk
from tkinter import messagebox
import pyfirmata
from time import sleep


# TODO: Before playing with this. Change the code in pyfirmata on line 185, to be 'len_args = len(inspect.getfullargspec(func)[0])'

# Function
def LedON():
    '''Turn on the LED on pin 13'''
    board.digital[13].write(1)
    
def LedOFF():
    '''Turn off the LED on pin 13'''
    board.digital[13].write(0)
    
def LedBlink():
    '''Blink the LED on pin 13 for a number of times given by the user. The default is 5 times.'''
    count = 0 if blinkCount.get() == '' else int(blinkCount.get())
    
    if count == 0:
        messagebox.showerror("Error", "Please enter a valid number")
        return
    elif count >= 30:
        messagebox.showinfo("Warning", "The number is too high, it may damage the LED")
        return
    elif count > 10:
        messagebox.askyesno("Warning", "The number is more than 10, it may take a long time. Do you want to continue?")
        
    for i in range(count):
            board.digital[13].write(1)
            sleep(0.5)
            board.digital[13].write(0)
            sleep(0.5)
    
#TODO Change the port to your port
board = pyfirmata.Arduino('COM8') # Mine at COM8, change it to your port


# Make the GUI
win = tk.Tk()
win.title("LED Control")
win.minsize(400,60)

# Label
label = tk.Label(win, text="Click to turn ON/OFF")
label.grid(column=1, row=1)

# Blink time
blinkCount = tk.Entry(win, bd=2, width=8)
blinkCount.grid(column=1, row=5)
tk.Label(win, text="Blink time").grid(column=2, row=5)

# Button
ONbtn = tk.Button(win, bd=2, text="ON", command=LedON)
ONbtn.grid(column=1, row=3)
OFFbtn = tk.Button(win, bd=2, text="OFF", command=LedOFF)
OFFbtn.grid(column=2, row=3)
BLbtn = tk.Button(win, bd=2, text="Blink", command=LedBlink)
BLbtn.grid(column=1, row=6)
BLbtn = tk.Button(win, bd=2, text="Stop Blink", command=LedBlink)
BLbtn.grid(column=2, row=6)

win.mainloop()