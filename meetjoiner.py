# Just your average everyday google meet joiner
import pyautogui, time

class meetjoin:
    def __init__(self, link, msgs):
        self.link = link
        self.msgs = msgs

    def setup(self):
        time.sleep(2)
        reload_icon = pyautogui.locateOnScreen("gmeetclass/r_icon.png", confidence=0.8) or pyautogui.locateOnScreen("gmeetclass/r_icon2.png", confidence=0.8)
        if not reload_icon:
            raise SystemExit
        
        left = reload_icon.left + 120
        top = reload_icon.top + 10
        pyautogui.click(left, top)
        time.sleep(0.5)
        pyautogui.typewrite(self.link)
        time.sleep(0.5)
        pyautogui.press("enter")

    def locate(self):
        time.sleep(5)
        reloadimg = pyautogui.locateOnScreen("gmeetclass/reload.png", confidence=0.8)
        while reloadimg: pyautogui.click(reloadimg); time.sleep(4); reloadimg = pyautogui.locateOnScreen("gmeetclass/reload.png", confidence=0.8)
        time.sleep(6)
        join_button = pyautogui.locateOnScreen("gmeetclass/join.png", confidence=0.8) or pyautogui.locateOnScreen("gmeetclass/join2.png", confidence=0.8)
        if not join_button: print("Tuff..."); return None
        pyautogui.click(join_button)
        time.sleep(1)
        return True

    def trouble(self):
        chat = pyautogui.locateOnScreen("gmeetclass/chat.png", confidence=0.8)
        while not chat:
            time.sleep(2)
            chat = pyautogui.locateOnScreen("gmeetclass/chat.png", confidence=0.8)

        pyautogui.click(chat)

        msg_thing = pyautogui.locateOnScreen("gmeetclass/msg.png", confidence=0.8)
        while not msg_thing:
            time.sleep(2)
            msg_thing = pyautogui.locateOnScreen("gmeetclass/chat.png", confidence=0.8)

        pyautogui.click(msg_thing)

    def goooo(self):
        for msg in self.msgs:
            pyautogui.typewrite(msg)
            time.sleep(0.4)
            pyautogui.press("enter")


def setup():
    print("Enter the link to the meeting you'd like to join")
    link = input(": ")
    print("What messages should I send? I will send in 10 second intervals. Terminate with blank")
    msgs = input(": ")
    msglist = []
    while msgs:
        msgs = input(": ")
        msglist.append(msgs)

    if not msglist:
        msglist.append("I am here")
    print("Completed... Aite... Let's goo")
    x = meetjoin(link, msglist)
    x.setup()
    success = x.locate()
    if not success: print("Couldn't seem to be able to join. Try again later"); raise SystemExit
    x.trouble()
    x.goooo()
    

setup()
        
