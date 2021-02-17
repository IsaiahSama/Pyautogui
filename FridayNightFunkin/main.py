import pyautogui
import keyboard
from time import sleep
from threading import Thread

# Left, down, up, right
x_coords = [1011, 1143, 1285, 1423]
letters = ["a", "s", "w", "d"]

y_coord = 300

color = (135, 163, 173)

class Setup:

    def __init__(self) -> None:
        pass

    def get_arrow(self, looking_for, to_find):

        print(f"Checking for color of {looking_for}")

        while True:
            try:
                while pyautogui.pixel(to_find, y_coord) != color:
                    pass

                break

            except WindowsError:
                continue  

        print(f"{looking_for} is correct.")
        

class Main:

    def __init__(self) -> None:
        setup = Setup()
        setup.get_arrow("down", 1143)
        setup.get_arrow("left", 1011)
        setup.get_arrow("right", 1423)
        setup.get_arrow("up", 1285)
        print("Done and ready to play")

    def main(self):
        for num, x_value in enumerate(x_coords):
            thread = Thread(target=self.play, args=(x_value, letters[num]), daemon=True)
            thread.start()       

        input()        

    def play(self, coord, letter):
        print(f"For coordinate {coord} we got the letter {letter}")      

        while True:
            
            try:
                x = pyautogui.pixel(coord, y_coord)
                if x[0] != color[0] or x[1] != color[1] or x[2] != color[2]:
                    keyboard.press(letter)
                    sleep(0.005)
                    keyboard.release(letter)
                    print(f"{letter} was pressed")
                    sleep(0.3)
            
            except WindowsError: continue

            if keyboard.is_pressed("q"):
                sleep(0.5)
                while not keyboard.is_pressed("z"):
                    sleep(0.1)

            if keyboard.is_pressed("f"): break

        print("Loop ended")


main = Main()

main.main()