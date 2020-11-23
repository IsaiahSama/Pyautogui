import pyautogui, keyboard, time

pyautogui.displayMousePosition()
time.sleep(1)
print("GO!")

while True:
    for x in range(180, 260):
        if pyautogui.pixel(x, 485)[0] != pyautogui.pixel(382, 403)[0]:
            pyautogui.press(" ")

        
    if keyboard.is_pressed("q"):
        break

    if pyautogui.locateOnScreen("dino/gameover.png", confidence=0.8):
        print("Died")
        pyautogui.press(" ")


print("Bye....")