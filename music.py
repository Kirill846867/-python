import os
import tkinter as tk
from tinytag import TinyTag
from pygame import mixer
from tkinter import *
import easygui
from PIL import Image, ImageTk
from mutagen import File

locate = os.path.dirname(os.path.abspath(__file__))
locate1 = locate+"/im.png"
playi = locate+"/play.png"
ico = locate+"/icon.png"

mixer.init()
root=Tk()
root.geometry("450x600")
root.title("player")
root.iconphoto(False, tk.PhotoImage(file=locate+"/icon.jpg"))
root.resizable(False, False)

if os.path.exists(locate+"/dir.txt")==False:
   direct = easygui.diropenbox()
   my_file = open(locate+"/dir.txt", "w+")
   my_file.write(direct)
   my_file.close()
else:
   my_file = open(locate+"/dir.txt", "r")
   direct = my_file.read()

#цвет
root["bg"] = "gray11"

#картинка
canvas = tk.Canvas(heigh=250, width=250)
canvas.place(x=225, y=100, anchor="n")
image = Image.open(locate1)
image.thumbnail((250, 250))
photo = ImageTk.PhotoImage(image)
canvas.create_image(127, 127, image=photo)

#названия
name1 = Label(text="Неизвестный" , background="gray11" , foreground="white")
name1.place(x=220, y=50, anchor="n")

name2 = Label(text="Неизвестный" , background="gray11" , foreground="white")
name2.place(x=220, y=25, anchor="n")

#нажатие кнопок
def btn_script():
    file= easygui.fileopenbox(default= direct+"/*.mp3")
    tag = TinyTag.get(file)
    trackname = tag.title
    artist = tag.artist
    audio = File(file)

    if 'APIC:' in audio.keys():
        cover_data = audio['APIC:'].data
        cover_filename = "cover.jpg"
        with open(cover_filename, 'wb') as fp:
            fp.write(cover_data)
            canvas.delete("all")
            imagec = Image.open(cover_filename)
            imagec.thumbnail((250, 250))
            photoc = ImageTk.PhotoImage(imagec)
            canvas.create_image(127, 127, image=photoc)
            canvas.image = photoc
    else:
        canvas.delete("all")
        image = Image.open(locate1)
        image.thumbnail((250, 250))
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(127, 127, image=photo)
        canvas.image = photo

    
    if trackname:
        name1["text"]=trackname
    else:
        name1["text"]="Неизвестный"
        
    if artist:
        name2["text"]=artist
    else:
        name2["text"]="Неизвестный"
     
    #плеер
    mixer.music.load(file)
    mixer.music.play()
  
def pause_script():
    mixer.music.pause()
    labelp.configure(command=play_script)
    
def play_script():
    mixer.music.unpause()
    labelp.configure(command=pause_script)
    
def btn_select():
    os.remove("dir.txt")

#кнопка play/pause
image = Image.open(playi)
image1=image.resize((50,50))
photop = ImageTk.PhotoImage(image1)
labelp = Button(image=photop, command=pause_script, height=50, width=50, bg="gray11")
labelp.place(x=200, y=400,)

#кнопка выбор
btn = Button(text="Выбрать песню" , command=btn_script)
btn.place(x=180,  y=475)

select = Button(text="Очистить директорию", command=btn_select)
select.place(x=160, y=550)

root.mainloop()
