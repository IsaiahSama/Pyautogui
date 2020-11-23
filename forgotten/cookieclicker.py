import click, keyboard, pyautogui, time

time.sleep(2)
while not keyboard.is_pressed("q"):

    click.click(205, 394)
    if keyboard.is_pressed("e"): time.sleep(15)