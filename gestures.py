from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui
import time

gestures_enabled = True

def stop_gestures():
    gestures_enabled = False

def start_gestures(delay = 2):
    gestures_enabled = True

    width, height = 1000, 800
    gesture_threshold = 300
    # Camera Setup
    cam = cv2.VideoCapture(0)

    #TODO: set the camera dimensions to match the monitor using tkinter
    # screen_width = win.winfo_screenwidth()
    # screen_height = win.winfo_screenheight()

    cam.set(3, width)
    cam.set(4, height) 
    # Hand Detector
    detector_hand = HandDetector(detectionCon=0.8, maxHands=1)
    # Variables
    button_pressed = False
    counter = 0

    print("starting gesture control")
    while gestures_enabled:
        # Get image frame
        success, img = cam.read()
        # Find the hand and its landmarks
        hands, img = detector_hand.findHands(img)  # with draw
        if hands and button_pressed is False:  # If hand is detected
            hand = hands[0]
            lmList = hand["lmList"]  # List of 21 Landmark points
            fin = detector_hand.fingersUp(hand)  
              
            current_mouse_x, current_mouse_y = pyautogui.position()

            if fin == [0, 1, 0, 0, 0]: 
                print("up")
                pyautogui.moveTo(current_mouse_x, current_mouse_y-10)
                button_pressed = True
            
            if fin == [0, 1, 1, 0, 0]: 
                print("down")
                pyautogui.moveTo(current_mouse_x, current_mouse_y+10)
                button_pressed = True

            if fin == [0, 0, 0, 0, 1]: 
                print("right")
                pyautogui.moveTo(current_mouse_x-10, current_mouse_y)
                button_pressed = True

            if fin == [1, 0, 0, 0, 0]: 
                print("left")
                pyautogui.moveTo(current_mouse_x+10, current_mouse_y)
                button_pressed = True       

            if fin == [1, 1, 0, 0, 0]: 
                print("left click")
                pyautogui.click()
                button_pressed = True       
                time.sleep(2)

            if fin == [0, 1, 1, 1, 1]: 
                print("right click")
                pyautogui.rightClick()
                button_pressed = True       
                time.sleep(2) 
            
            if fin == [1, 1, 1, 0, 0]:
                print("double click")
                pyautogui.doubleClick()
                button_pressed = True       
                time.sleep(2) 

            if fin == [1, 1, 1, 1, 1]: 
                cx, cy = hand["center"]
                print('following')
                pyautogui.moveTo(cx-50, cy+100)

        if button_pressed:
            counter += 1
            if counter > delay:
                counter = 0
                button_pressed = False
    
        cv2.imshow("GestureRecognition", img)
    
        key = cv2.waitKey(1)
        if key == ord('q'): # press q to quit
            cv2.destroyAllWindows()
            break