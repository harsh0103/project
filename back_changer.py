import os
import random
import ctypes
import time
from win10toast import ToastNotifier

for_notification = ToastNotifier()
for_notification.show_toast(
    "Wallpaper Automate","The script has been executed successfully..!", duration=10
)

"""_ _ _ Main Code _ _ _"""
def wallomator(path):
    try:
        list_wall = os.listdir(path)

        for i in range(len(list_wall)):
            random_wallpaper = random.choice(list_wall)
            random_wallpaper = os.path.join(path, random_wallpaper)
            final_wallpaper = bytes(random_wallpaper, "utf-8")
            ctypes.windll.user32.SystemParametersInfoA(20, 0, final_wallpaper, 3)
            t = 5
            time.sleep(t)
        return "Script Executed occured...!"
    except:
        print("Some error occured...!")

path = r"D:\wallpapers"
wallomator(path)
