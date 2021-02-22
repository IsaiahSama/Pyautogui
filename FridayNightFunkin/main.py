import pyautogui
import keyboard
from time import sleep
from threading import Thread
from win10toast import ToastNotifier

# WASD!!!
x_coords = [1392, 1056, 1228, 1565]
letters = ["w", "a", "s", "d"]

y_coord = 165

class Setup:

    def __init__(self) -> None:
        pass

    def setup(self):
        ToastNotifier().show_toast(title="Friday Night Funkin Bot", msg="Press the 'p' key when the mouse is near the middle of the left arrow.")
        while not keyboard.is_pressed("p"): sleep(0.05)
        while True:
            try:
                color = pyautogui.pixel(1056, 165)
                return color
            except WindowsError:
                continue
        
class Main:

    def __init__(self) -> None:
        self.color = None


    def pre_main(self):
        setup = Setup()
        pyautogui.moveTo(1056, 165)
        self.color = setup.setup()
        ToastNotifier().show_toast(title="Friday Night Funkin Bot", msg="Done. Press 'F' to start me and 'q' to stop me :)")
        while not keyboard.is_pressed('f'): sleep(0.02)
        self.main()


    def main(self):
        thread_list = [Thread(target=self.handle_up, daemon=True), Thread(target=self.handle_left, daemon=True), Thread(target=self.handle_down, daemon=True), Thread(target=self.handle_right, daemon=True)]


        for thread in thread_list:
            thread.start()

        while not keyboard.is_pressed("q"):sleep(0.1)

    def handle_up(self):
        green = (18, 249, 7)

        print("Handling up arrow has begun.")
        
        while not keyboard.is_pressed("q"):
            # thread = Thread(target=self.press, args=("w",))
            
            for y in range(x_coords[0]-2, x_coords[0]+2):
                try:
                    x = pyautogui.pixel(y, y_coord)

                    if x[1] > 245-20:
                        # thread.start()
                        self.press("w")
                        print("Up arrow pressed")
                
                        sleep(0.1)
                except WindowsError:
                    continue                

        print("Function has been terminated")

        ToastNotifier().show_toast(title="Friday Night Funkin Bot", msg="Bot has been stopped")

    def handle_left(self):
        purple = (195, 75, 154)

        print("Handling left arrow has begun")

        while not keyboard.is_pressed("q"):
            
            # thread = Thread(target=self.press, args=("a",))

            for y in range(x_coords[1]-2, x_coords[1]+2):
                try:
                    x = pyautogui.pixel(y, y_coord)

                    if x[0] > 160-20 and x[2] > 150-20:
                        self.press("a")
                        print("Left arrow pressed")
                        
                        sleep(0.1)
                except WindowsError:
                    continue

        print("Function has been terminated")


    def handle_down(self):
        blue = (0, 204, 205)
        print("Handling down arrow has begun")

        while not keyboard.is_pressed("q"):
            # thread = Thread(target=self.press, args=("s",))

            for y in range(x_coords[2]-2, x_coords[2]+2):
                try:
                    x = pyautogui.pixel(y, y_coord)
                    
                    if x[1] > 200-20 and x[2] > 200-20:
                        self.press("s")

                        print("Down arrow pressed")
                
                        sleep(0.1)
                except WindowsError:
                    continue

        print("Function has been terminated")


    def handle_right(self):
        red = (249, 57, 63)

        print("Handling right arrow has begun")

        while not keyboard.is_pressed("q"):
            #thread = Thread(target=self.press, args=("d",))

            for y in range(x_coords[3]-2, x_coords[3]+2):
                try:
                    x = pyautogui.pixel(y, y_coord)
                
                    if x[0] > 245-20:
                        
                        self.press("d")
                        print("Right arrow pressed")
                        sleep(0.1)
                except WindowsError:
                    continue

        print("Function has been terminated")

    def press(self, key):
        
        keyboard.press(key)
        sleep(0.05)
        keyboard.release(key)



main = Main()
ToastNotifier().show_toast(title="Friday Night Funkin Bot", msg="Bot has Started. DO NOT MOVE YOUR CURSOR")

while True: main.pre_main()