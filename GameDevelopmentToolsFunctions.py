import os
import platform
import time


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")


def TimerSleep():
    time.sleep(2)


