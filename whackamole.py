import pyautogui
import keyboard
import click

# Requires click.py to be in same folder. Or just uncomment out the below code
# import win32api, win32con, time
# def click(x, y):
#     win32api.SetCursorPos((x, y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
#     time.sleep(0.01)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Website https://www.memory-improvement-tips.com/whack-a-mole-game-window.html

# Y: 368 X: 227 338 444
# X: 227 Y: 368 432 498

x_coords = [230, 334, 441]
y_coords = [383, 472, 562]

# This was made more for my laptop which has a meh screen... So feel free to change the values as you desire.
input(": ")
while not keyboard.is_pressed("q"):
    
    for x in x_coords:
        for y in y_coords:
            pixel = pyautogui.pixel(x, y)
            if pixel[0] > 180 and pixel[1] > 180 and pixel[2] < 240:
                click.click(x, y)

