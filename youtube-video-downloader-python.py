from tkinter import *
from pytube import YouTube
import webbrowser

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataSciPy-YouTube")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack(pady=15)

link = StringVar()

link_enter = Entry(root, width=50, font='18', textvariable=link)
link_enter.insert(0, 'Remove these text and paste your link here')
link_enter.place(x=32, y=90)


def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=250)

def callback():
    webbrowser.open(r"https://www.datascipy.com/")


Button(root, text='Download', font='verdana 15', bg='lime', command=Downloader).place(x=150, y=150)
Button(root, text='Exit', font='verdana 15' ,bg='red', command=quit).place(x=300, y=150)
Button(root, text='View Source Code', font='verdana 15', bg='blue', fg='white', command=callback).place(x=152, y=200)

root.mainloop()
