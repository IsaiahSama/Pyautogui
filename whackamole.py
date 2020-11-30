import pyautogui
import keyboard

import win32api, win32con, time
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Website https://www.memory-improvement-tips.com/whack-a-mole-game-window.html

# Change values of x_coords and y_coords. 
# I recommend using pyautogui.displayMousePosition() to see the co-ordinates on your screen.
# These co-ordinates are the areas around the centre of the 9 holes. The x co-ordinates are taken from the top most row, going across, and the y co-ordinates are taken from the left most column going down. 
# The bot can then find the rest of the holes using those 6 values.
x_coords = [230, 334, 441]
y_coords = [383, 472, 562]

# This was made more for my laptop which has a meh screen... So feel free to change the values as you desire.
input(": ")
while not keyboard.is_pressed("q"):
    
    for x in x_coords:
        for y in y_coords:
            pixel = pyautogui.pixel(x, y)
            if pixel[0] > 180 and pixel[1] > 180 and pixel[2] < 240:
                click(x, y)

