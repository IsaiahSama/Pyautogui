import pyautogui
import keyboard
import webbrowser
from time import sleep
from threading import Thread
from win10toast import ToastNotifier

# WASD!!!
x_coords = [1285, 1011, 1143, 1423]
letters = ["w", "a", "s", "d"]

y_coord = 306

color = (135, 163, 173)

webbrowser.open("https://www.newgrounds.com/portal/view/770371")
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
        ToastNotifier().show_toast(title="Friday Night Funkin Bot", msg="Bot has Started")
        setup.get_arrow("down", 1143)
        setup.get_arrow("left", 1011)
        setup.get_arrow("right", 1423)
        setup.get_arrow("up", 1285)
        print("Done and ready to play")
        ToastNotifier().show_toast(title="Friday Night Funkin Bot", msg="Done and ready to play")


    def main(self):
        thread_list = [Thread(target=self.handle_up, daemon=True), Thread(target=self.handle_left, daemon=True), Thread(target=self.handle_down, daemon=True), Thread(target=self.handle_right, daemon=True)]


        for thread in thread_list:
            thread.start()

        input()


    def handle_up(self):
        green = (18, 249, 7)

        print("Handling up arrow has begun.")
        
        while not keyboard.is_pressed("q"):
            # thread = Thread(target=self.press, args=("w",))
            try:
                x = pyautogui.pixel(x_coords[0], y_coord)

                if x[1] > 245:
                    # thread.start()
                    self.press("w")
                    print("Up arrow pressed")

                    x = pyautogui.pixel(x_coords[0], y_coord)
                    if x[1] > 245:
                        keyboard.press("w")
                        print("Up arrow held")
                        while x[1] > 245:
                            sleep(0.01)
                            x = pyautogui.pixel(x_coords[0], y_coord)

                        keyboard.release("w")
            
            except WindowsError:
                continue                
            

        print("Function has been terminated")

        ToastNotifier().show_toast(title="Friday Night Funkin Bot", msg="Bot has been stopped")

    def handle_left(self):
        purple = (195, 75, 154)

        print("Handling left arrow has begun")

        while not keyboard.is_pressed("q"):
            
            # thread = Thread(target=self.press, args=("a",))

            try:
                x = pyautogui.pixel(x_coords[1], y_coord)

                if x[0] > 160 and x[2] > 150:
                    self.press("a")
                    print("Left arrow pressed")

                    x = pyautogui.pixel(x_coords[1], y_coord)
                    if x[0] > 160 and x[2] > 150:
                        keyboard.press("a")
                        print("left arrow held")
                        while x[0] > 160 and x[2] > 150:
                            sleep(0.01)
                            x = pyautogui.pixel(x_coords[1], y_coord)

                        keyboard.release("a")                   
            
            except WindowsError:
                continue

        print("Function has been terminated")


    def handle_down(self):
        blue = (0, 204, 205)

        print("Handling down arrow has begun")

        while not keyboard.is_pressed("q"):
            # thread = Thread(target=self.press, args=("s",))

            try:
                x = pyautogui.pixel(x_coords[2], y_coord)
                
                if x[1] > 200 and x[2] > 200:
                    self.press("s")

                    print("Down arrow pressed")

                    x = pyautogui.pixel(x_coords[2], y_coord)
                    if x[1] > 200 and x[2] > 200:
                        keyboard.press("s")
                        print("Right arrow held")
                        while x[1] > 200 and x[2] > 200:
                            sleep(0.01)
                            x = pyautogui.pixel(x_coords[2], y_coord)

                        keyboard.release("s")
            
            except WindowsError:
                continue

        print("Function has been terminated")


    def handle_right(self):
        red = (249, 57, 63)

        print("Handling right arrow has begun")

        while not keyboard.is_pressed("q"):
            #thread = Thread(target=self.press, args=("d",))


            try:
                x = pyautogui.pixel(x_coords[3], y_coord)
            
                if x[0] > 245:
                    
                    self.press("d")
                    print("Right arrow pressed")

                    x = pyautogui.pixel(x_coords[3], y_coord)
                    if x[0] > 245:
                        keyboard.press("d")
                        print("Right arrow held")
                        while x[0] > 245:
                            sleep(0.01)
                            x = pyautogui.pixel(x_coords[3], y_coord)

                        keyboard.release("d")

            
            except WindowsError:
                continue

        print("Function has been terminated")

    def press(self, key):
        
        keyboard.press(key)
        sleep(0.1)
        keyboard.release(key)
        sleep(0.03)



main = Main()

main.main()