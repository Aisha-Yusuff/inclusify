# import all components
# from the tkinter Library
from tkinter import *
from gestures import start_gestures, stop_gestures
from threading import Thread

# Create the root window
window = Tk()

# Set Window titLe
window.title('Inclusify')

# Set window size
window.geometry("1000x500")

#Set window background color
window.config(background = "white")

label_gesture_control = Label(window,
                            text = "Gesture Controller",
                            width = 100, height = 4,
                            fg = "blue")

label_movement_speed = Label(window,
                             text = "Set fine control precision, higher = more precise")

entry_movement_speed = Entry(window,
                             width=10
)
entry_movement_speed.insert(-1, "1")

gestureThread = None

def gesture_button_click():
    global gestureThread
    if gestureThread is not None:
        print("Stopping gestures")
        stop_gestures()
        gestureThread.join()
        gestureThread = None
        button_gestures.configure(text= "Start Gesture Control")
        return
    delay_str = entry_movement_speed.get()
    if delay_str == "" or delay_str == None:
        gestureThread = Thread(target = start_gestures)
    else:
        gestureThread = Thread(target = start_gestures, args=(10/int(delay_str),))
    gestureThread.start()
    button_gestures.configure(text= "Stop Gesture Control")

def exit_button_click():
    global gestureThread
    if gestureThread is not None:
        stop_gestures()
        gestureThread.join()
    exit()

button_gestures = Button(window,
                        text = "Start Gesture Control",
                        command = gesture_button_click)

button_exit = Button(window,
                    text = "Exit",
                    command = exit_button_click)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_gesture_control.grid(column = 0, row = 0)

label_movement_speed.grid(column = 0, row = 1)

entry_movement_speed.grid(column = 0, row = 2)

button_gestures.grid(column = 0, row = 3)

button_exit.grid(column = 0, row = 4)

# Let the windows wait for any events 
window.mainloop()
