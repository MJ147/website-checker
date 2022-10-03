from urllib.request import urlopen;
import threading
import subprocess
import datetime
# import winsound

# import ctypes
# import Tkinter as tk
# import tkMessageBox

# root = tk.Tk()
# root.withdraw()
# tkMessageBox.showwarning('alert title', 'Bad things happened!') 

url = "https://hittheball.pl//get_events.php?date=2022-10-29"
searchedFragmentStart = '6 października'
searchedFragmentEnd = '7 października'
searchedPhrase = 'AKTYWNY WARSZAWIAK'


def findOnWebsite():
    page = urlopen(url)
    html = page.read().decode("utf-8")
    start = html.find(searchedFragmentStart)
    end = html.find(searchedFragmentEnd)
    fragment = html[start:end]
    training = fragment.find(searchedPhrase)

    if training == -1:
        print('not found at', datetime.datetime.now())
        threading.Timer(900.0, findOnWebsite).start()   
    else:
        print('-----------========> found at', datetime.datetime.now(), '<=========-----------')
        # Set frequency to 2000 Hertz
        frequency = 2000
        # Set duration to 1500 milliseconds (1.5 seconds)
        duration = 1500
        # Make beep sound on Windows
        # winsound.Beep(frequency, duration)
        subprocess.run(["/usr/bin/notify-send", "--icon=face-monkey", "Training is available in calendar"])
        threading.Timer(10.0, findOnWebsite).start()   


findOnWebsite()

# def Mbox(title, text, style):
    # return ctypes.windll.user32.MessageBoxW(0, text, title, style

# Mbox('Your title', 'Your text', 1)