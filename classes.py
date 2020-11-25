import pyautogui, keyboard, os, time, json, re

# Changes directory in the gmeetclass folder which must be in the same directory
os.chdir("gmeetclass")
# Creates folder for JSON files
if not os.path.exists("jsondata"): os.mkdir("jsondata")
# Creates folder for Screenshots
if not os.path.exists("screenshots"): os.mkdir("screenshots")


class MyClass:
    def __init__(self, schedule, subjects, days, periods, timing):
        self.schedule = schedule
        self.subjects = subjects
        self.days = days
        self.periods = periods
        self.timing = timing    
    
    def main(self):
        # Calls the get schedule function.
        my_schedule = self.get_schedule()
        # Should only fail if done on a weekend
        if not my_schedule:
            print("Sorry, I don't do work on a weekend")
            return  
        # Gets current time in minutes
        minutes = self.get_time()
        # 510 is 8:30 am.
        while minutes < 510:
            # You'll be seeing this usage of time.ctime() a bit.
            print(f"Today is {time.ctime()}. Waiting until 8:30 to begin Registration.")
            time.sleep(40)
        
        os.system("CLS")

        print("Beginning classes")
        # Loops through the 9 periods of the day.
        for period in self.periods:
            # Gets the time when the current period should end
            end_time = self.timing.get(period).split(":")
            # Turns the received time into integers.
            # Multiplies the hour by 60 to turn them into minutes then adds them to the minutes. Since working with only minutes was easier and more logical.
            end_minutes = (int(end_time[0]) * 60) + int(end_time[1])
            # Gets the current class based on your schedule and the period for today
            current_class = self.get_class(my_schedule, period)
            os.system("CLS")
            print(f"Period {period}: Initiating {current_class} phase")
            time.sleep(1)
            minutes = self.get_time()
            # As it goes thru one period to the next, skips those periods whose ending times have already passed.
            if minutes > end_minutes: continue

            is_class = self.navbar(current_class)
            
            if is_class:
                time.sleep(5)
                print(f"Joined {current_class}")
                self.send_msg(f"Period {period}: {current_class}")
                time.sleep(2)
                
            else:
                print("No class I guess")

            minutes = self.get_time()
            while not minutes == end_minutes:
                # timer += 1
                if is_class:
                    self.screen_check(current_class)

                time.sleep(40)
                minutes = self.get_time()
            
            if is_class:
                self.send_msg("Thank you for the class. Have a good day")

        os.system("CLS")
        print("Congratulations, your classes are now complete. Have good evening now.")

    def get_schedule(self):
        cur_sched = self.schedule.get(time.ctime().split(" ")[0])
        return cur_sched

    def get_class(self, schedule, period):
        return schedule.get(period)

    def navbar(self, subject):
        coords = pyautogui.locateOnScreen("images/r_icon.png", confidence=0.8, grayscale=True)
        time.sleep(4)
        if not coords:
            print("SOMETHING WENT WRONG")
            raise SystemExit

        left = coords.left + 100
        top = coords.top + 5
        pyautogui.click(left, top)
        try:
            pyautogui.typewrite(f"{subjects[subject]}?authuser=0&hs=179")
            # pyautogui.typewrite("meet.google.com/kop-qotc-hsz")
            time.sleep(0.5)
            pyautogui.press("enter")
            is_class = self.attemptjoin()
            return is_class
        except KeyError:
            return None

    def send_msg(self, msg):
        chat = pyautogui.locateOnScreen("images/chat.png", confidence=0.7)
        if chat:
            pyautogui.click(chat)
        time.sleep(3)
        text_area = pyautogui.locateOnScreen("images/msg.png", confidence=0.6, grayscale=True)
        if text_area:
            pyautogui.click(text_area)
            time.sleep(2)
            pyautogui.typewrite(msg)
            time.sleep(1)
            pyautogui.press("enter")
        # pass


    def attemptjoin(self):
        for _ in range(100):
            try:
                img = pyautogui.locateOnScreen("../reloadmeet/reload.png", confidence=0.8)
                if not img:
                    time.sleep(1)
                    dismiss = pyautogui.locateOnScreen("images/dismiss.png", confidence=0.8)
                    if dismiss:
                        pyautogui.click(dismiss)
                        time.sleep(1)
                    time.sleep(10)
                    camera = pyautogui.locateOnScreen("images/camera.png", confidence=0.8)
                    if camera:
                        pyautogui.click(camera)
                    join = pyautogui.locateOnScreen("images/join.png", confidence=0.8)
                    if join:
                        time.sleep(2)
                        pyautogui.click(join)
                        return True
                    else:
                        return False
                else:
                    pyautogui.click(img)
                time.sleep(3)
            except KeyboardInterrupt:
                return False
        return False
       

    def get_time(self):
        cur_time = time.ctime().split(" ")[3].split(":")
        minutes = (int(cur_time[0]) * 60) + int(cur_time[1])
        return minutes

    def get_last(self, itera):
        # An empty list of numbers
        numbers = []
        for img in itera:
            # Loops through the list of images in the screenshots folder looking for the numbers.
            # In the format "physics32.png", splits name by the . and returns the 0 index, which in this case is "physics32"
            numbers.append(int(re.findall(r"([0-9]+)", img.split(".")[0])[-1]))
        # Sorts the numbers then sends the highest one.
        return sorted(numbers)[-1]

    def screen_check(self, current_class):
        # Checks if someone is presenting by looking for the "presenting" image
        sharing = pyautogui.locateOnScreen("images/presenting.png", confidence=0.8)
        if sharing:
            if not os.path.exists(f"screenshots/{current_class}"):os.mkdir(f"screenshots/{current_class}")
            # Searches the screenshots folder for all images starting with the same name as the current subject
            screenshots = [screenshot for screenshot in os.listdir(f"screenshots/{current_class}") if screenshot.endswith(".png")]
            if screenshots:
                # Calles the get_last Function. All images will be saved with a number at the end of the subject's name
                highest = self.get_last(screenshots) + 1
            else:
                # If no other screenshots with the same name as current subject exists, sets highest to 1 and names the new screenshot that.
                highest = 1
            pyautogui.screenshot(imageFilename=f"screenshots/{current_class}/{current_class}{highest}.png")
            print("Screenshot taken")  

dotw = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# List of the 9 periods of a day (Including Period 0 (Registration) and Period 5 (Lunch))
periods = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

def mainSetUp():
    if not os.path.exists("jsondata/schedule2.json"):
        # Code to set up time table. 
        def setup(filename):
            weekly_schedule = {}

            for day in dotw:
                weekly_schedule[day] = {}

                for period in periods:
                    print(f"Enter subject for period {period} on {day}")
                    
                    if period == '0':
                        print("Period 0 is registrationnnn")
                        weekly_schedule[day][period] = "Registration"
                        continue

                    if period == '5':
                        print("Period 5 is lunchhhh")
                        weekly_schedule[day][period] = "LUNCH"
                        continue
                    
                    subject = input(": ").capitalize()
                    
                    weekly_schedule[day][period] = subject   
                
                os.system("CLS")

            with open(filename, "w") as f:
                json.dump(weekly_schedule, f, indent=4)
        
        setup("jsondata/schedule1.json")
        setup("jsondata/schedule2.json")

    # Checks for subjects file
    if not os.path.exists("jsondata/subjects.json"):
        print("How many subjects do you do?")
        subject_count = int(input(": "))
        subjects = {}
        for _ in range(subject_count):
            print("Enter the name of your subject")
            subject_name = input(": ")
            print("Enter the link for the google meeting for this class")
            meetlink = input(": ")
            subjects[subject_name] = meetlink
            os.system("CLS")

        print("Subjects have been set up")
        with open("jsondata/subjects.json", "w") as f:
            json.dump(subjects, f, indent=4) 

mainSetUp()

# This is mainly for my school. Online classes are done weird so we have a different timetable for the first and second week.
print("Is this week 1 or week 2?")
week = input(": ")

with open(f"jsondata/schedule{week}.json") as f:
    schedule = json.load(f)

with open("jsondata/subjects.json") as f:
    subjects = json.load(f)

# Timing for my school day. Come and change the code yourself >:)
# It's just a dictionary BROOOOOOOO
# These keys will be referenced by the current period. The values are the time that period should end.
timing = {"0":"9:00", "1": "9:40", "2": "10:20", "3": "11:00", "4":"11:40", "5":"12:50", "6":"13:30", "7":"14:10", "8":"14:50"}

myclass = MyClass(schedule, subjects, dotw, periods, timing)
myclass.main()