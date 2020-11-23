import keyboard
import pyautogui
from click import click

# Website: http://www.donttap.com/

# Requires click.py to be in same folder. Or just uncomment out the below code
# import win32api, win32con, time
# def click(x, y):
#     win32api.SetCursorPos((x, y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
#     time.sleep(0.01)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# squares: 
# Row 1: Y: 271 X: 165, 277, 390, 495
# Row 2: Y: 386
# Row 3: Y: 489
# Row 4: 589

y_values = [271, 386, 489, 589]
x_values = [165, 277, 390, 495]

# This was made more for my laptop which has a meh screen... So feel free to change the values as you desire.
input(": ")
while keyboard.is_pressed("q") == False:

    for value_y in y_values:
        for value_x in x_values:
            if pyautogui.pixel(value_x, value_y)[0] == 0:
                click(value_x, value_y)
