import keyboard
import pyautogui

# Website: http://www.donttap.com/

import win32api, win32con, time
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# squares: 
# Row 1: Y: 271 X: 165, 277, 390, 495
# Row 2: Y: 386
# Row 3: Y: 489
# Row 4: 589


# Change values of x_coords and y_coords. 
# I recommend using pyautogui.displayMousePosition() to see the co-ordinates on your screen.
# These co-ordinates are the areas around the centre of the 9 holes. The x co-ordinates are taken from the top most row, going across, and the y co-ordinates are taken from the left most column going down. 
# The bot can then find the rest of the holes using those 6 values.
y_coords = [271, 386, 489, 589]
x_coords = [165, 277, 390, 495]

# This was made more for my laptop which has a meh screen... So feel free to change the values as you desire.
input(": ")
while keyboard.is_pressed("q") == False:

    for value_y in y_coords:
        for value_x in x_coords:
            if pyautogui.pixel(value_x, value_y)[0] == 0:
                click(value_x, value_y)
