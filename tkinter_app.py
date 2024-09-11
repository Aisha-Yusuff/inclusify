# import all components
# from the tkinter Library
from tkinter import *
from gestures import start_gestures

# Create the root window
window = Tk()

# Set Window titLe
window.title('Inclusify')

# Set window size
window.geometry("1000x500")

#Set window background color
window.config(background = "white")

gesture_control_label = Label(window,
                            text = "Gesture Controller",
                            width = 100, height = 4,
                            fg = "blue")

entry_movement_speed = Entry(window,
                             width=10
)

def gesture_button_click():
    delay_str = entry_movement_speed.get()
    if delay_str == "" or delay_str == None:
        start_gestures()
    else:
        start_gestures(int(delay_str))

button_gestures = Button(window,
                        text = "Start Gesture Control",
                        command = gesture_button_click)

button_exit = Button(window,
                    text = "Exit",
                    command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
gesture_control_label.grid(column = 0, row = 0)

entry_movement_speed.grid(column = 0, row = 1)

button_gestures.grid(column = 0, row = 2)

button_exit.grid(column = 0, row = 3)

# Let the windows wait for any events 
window.mainloop()
