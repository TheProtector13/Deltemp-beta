import os
from configparser import ConfigParser
import shutil
import time as t
import glob
from pathlib import Path
import datetime
import tkinter as TK

homepath=Path.home()
cwd=os.getcwd()
config=ConfigParser()

config.read(cwd+"\\deltemp_setting.ini")

if config.has_section("CONFIG") == False:
    config.add_section("CONFIG")
    config.add_section("LOGGING")
    config.set("CONFIG","delete_temp","True")
    config.set("CONFIG","delete_%temp%","True")
    config.set("CONFIG","delete_prefetch","True")
    config.set("LOGGING","exceptionlogs","True")
    config.set("LOGGING","log_all","True")
    config.write(open("deltemp_setting.ini", "w"))

delete_temp=config.getboolean("CONFIG","delete_temp")
delete_usertemp=config.getboolean("CONFIG","delete_%temp%")
delete_prefetch=config.getboolean("CONFIG","delete_prefetch")
exceptionlogs=config.getboolean("LOGGING","exceptionlogs")
log_all=config.getboolean("LOGGING","log_all")

def time():
    time=t.strftime("%Y-%m-%d %H:%M:%S", t.localtime())
    print(time)
    f=open(cwd+"\\del_temp_log.txt","a+")
    f.write("\n"+str(time)+"\n")
    f.close

class pathfolder:
    def __init__(self,path,name):
        self.path=path
        self.name=name

    def delete(self):
        folder=glob.glob(self.path)
        print("\n\n"+self.name+" ürítése:\n")
        prompt.config(state="normal")
        prompt.insert(TK.END, "\n\n"+self.name+" ürítése:\n")
        prompt.config(state="disabled")
        prompt.see(TK.END)
        for i in folder:
            print("Deleting ... "+i)
            prompt.config(state="normal")
            prompt.insert(TK.END, "Deleting ... "+i)
            prompt.config(state="disabled")
            prompt.see(TK.END)
            try:
                os.remove(i)
                print ("Deleted ...")
                message=("deleted..."+str(i)+"\n")
                prompt.config(state="normal")
                prompt.insert(TK.END, "\n"+message)
                prompt.config(state="disabled")
                prompt.see(TK.END)
                if log_all == True:
                    f=open(cwd+"\\del_temp_log.txt","a+")
                    f.write(message)
                    f.close
            except:
                print ("FAIL !!! ===> Starting shutil.rmtree delete.")
                try:
                    shutil.rmtree(i)
                    print("Deleted ...")
                    message=("deleted with rmtree..."+str(i)+"\n")
                    prompt.config(state="normal")
                    prompt.insert(TK.END, "\n"+message)
                    prompt.config(state="disabled")
                    prompt.see(TK.END)
                    if log_all == True:
                        f=open(cwd+"\\del_temp_log.txt","a+")
                        f.write(message)
                        f.close
                except Exception as e:
                    message=(str(e)+"\n")
                    print(message)
                    if exceptionlogs == True:
                        prompt.config(state="normal")
                        prompt.insert(TK.END, "\n"+message)
                        prompt.config(state="disabled")
                        prompt.see(TK.END)
                        f=open(cwd+"\\del_temp_log.txt","a+")
                        f.write(message)
                        f.close
            menu.update()
        menu.update()

def start():
    time()
    if delete_temp == True:
        temp.delete()
        sleep()
    if delete_usertemp == True:
        temp2.delete()
        sleep()
    if delete_prefetch == True:
        prefetch.delete()
        sleep()
    print("Kész!")
    prompt.config(state="normal")
    prompt.insert(TK.END, "Kész!")
    prompt.config(state="disabled")
    prompt.see(TK.END)

def sleep():
    for i in range(60):
        t.sleep(0.05)
        menu.update()

def close():
    exit()


temp=pathfolder("C:\\Windows\\Temp\\*","temp")
temp2=pathfolder(str(homepath)+"\\AppData\\Local\\Temp\\*","%temp%")
prefetch=pathfolder("C:\\Windows\\Prefetch\\*","prefetch")


menu=TK.Canvas()
menu.grid()
text=TK.Label(menu, text="Ez a program törli a TEMP mappák tartalmát.\nBizonyosodj meg róla, hogy minden munkafolyamatot lementettél, és minden programot bezártál!\n\n - A beállításokat a deltemp_setting.ini fájlban módosíthatod.")
text.grid(row=1,column=1)
startbutton=TK.Button(menu, text="START", bg="blue", fg="white", command=start, width=10)
startbutton.grid(row=2,column=1)
prompt=TK.Text(menu, width=60, height=15, state="disabled",bg="darkgreen",fg="white")
prompt.grid(row=4,column=1)
close=TK.Button(menu, text="CLOSE", bg="red", fg="white", command=close, width=8)
close.grid(row=5,column=1)
menu.mainloop()
