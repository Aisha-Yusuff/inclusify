
import win32com.client as win32
import time

# import all components
# from the tkinter Library
from tkinter import *

# import filedialog module
from tkinter import filedialog

from app import hand_gestures

#  Function for opening the file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                        title = "Select a File",
                                        filetypes = (("Powerpoint files", "*.pptx*"),("All files", "*.*")))

# Change Label contents
    label_file_explorer.configure(text="Presentation opened: "+filename)

    app = win32. Dispatch("PowerPoint.Application")

    objCOM = app. Presentations. Open(FiLeName=filename, WithWindow=1)

    objCOM.SLideShowSettings.Run()
    # time.sleep(10)
    objCOM.SLideShowSettings.View.Next()

# Create the root window
window = Tk()

# Set Window titLe
window.title('File Explorer')

# Set window size
window. geometry ("700x500")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
Label_file_explorer = Label(window,
                            text = "Gesture Controlled PowerPoint",
                            width = 100, height = 4,
                            fg = "blue")

button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)

button_hand_gesture = Button(window,
                        text = "Activate Hands",
                        command = hand_gestures)

button_exit = Button(window,
                    text = "Exit",
                    command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
Label_file_explorer.grid(column = 0, row = 1)

button_hand_gesture.grid(column = 0, row =2)

button_explore.grid(column = 0, row =2)

button_exit.grid(column = 0, row = 3)

# Let the windows wait for any events 
window.mainloop()
