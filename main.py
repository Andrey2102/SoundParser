from __future__ import unicode_literals
import youtube_dl
import os
from tkinter import*
from tkinter import filedialog as fd


# Window settings

root = Tk()
root.geometry("500x170")
root.title("Sound Parser")
root.resizable(width=True, height=False)

# Download data and config

def parse():
    try:
        os.chdir(PATH.get())
        try:
            with youtube_dl.YoutubeDL(download_options) as dl:
                dl.download([URL.get()])
        except:
            STATUS.set("Status: Operation failed. Something wrong with the URL.")
        STATUS.set("Status: Operation successful.")
    except:
        STATUS.set("Status: Operation failed. No such derictory or limited access.")






download_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
lab1 = Label(text="URL address: ").place(x=20, y=10)
URL = StringVar()
URL.set("default")
Entry(width=60, textvariable=URL).place(x=120, y=10)

lab2 = Label(text="PATH: ").place(x=40, y=40)
PATH = StringVar()
PATH.set("C:\\Users\Public\Music")
Entry(width=60, textvariable=PATH).place(x=120, y=40)

STATUS = StringVar()
STATUS.set("Status: Awaiting the start of work.")
lab3 = Label(textvariable=STATUS).place(x=0.5, y=150)

but = Button(text="Get Sound", command=parse).place(x=25, y=70)

root.mainloop()