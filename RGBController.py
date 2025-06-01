import serial
import time
import tkinter as tk

# The Port and the Serial Init Num
# Port = input("Enter Port: ")
# Buad = int(input("Enter Baud: "))

# arduino = serial.Serial(Port, Buad)
# arduino = serial.Serial("COM4", 9600)

# # Not Understood but wait for arduino to reset
# time.sleep(2)

# RedVal = 0
# GreenVal = 0
# BlueVal = 0

# def Update():
#     global RedVal
#     global GreenVal
#     global BlueVal

#     print(RedVal)
#     print(GreenVal)
#     print(BlueVal)

#     parsestring = f"R{RedVal}G{GreenVal}B{BlueVal}\n"
#     arduino.write(parsestring.encode())

# def red_slider_changed(value):
#     global RedVal
#     RedVal = value

# def green_slider_changed(value):
#     global GreenVal
#     GreenVal = value

# def blue_slider_changed(value):
#     global BlueVal
#     BlueVal = value

# def on_button_click():
#     Update()
#     print("Sleeping for 2 Seconds!!...")
#     time.sleep(2)
#     print("Online!!")

# root = tk.Tk()
# root.title("Tkinter Slider Example")

# tk.Label(root, text="Red", font=("Arial", 12)).pack()
# Redslider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, command=red_slider_changed)
# Redslider.pack()

# tk.Label(root, text="Blue", font=("Arial", 12)).pack()
# Blueslider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, command=blue_slider_changed)
# Blueslider.pack()

# tk.Label(root, text="Green", font=("Arial", 12)).pack()
# Greenslider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, command=green_slider_changed)
# Greenslider.pack()

# # Create a button and bind it to the function
# button = tk.Button(root, text="Click Me", command=on_button_click)
# button.pack(padx=20, pady=20)

# print("Update Check")

# root.mainloop()

# arduino.close()

print(serial.__version__)
# print(tk)
