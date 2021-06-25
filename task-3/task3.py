import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import http.client
import sys

win = tk.Tk()
win.geometry(f"820x500+100+200")
win.title ("covid")
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
       'x-rapidapi-key': "7c7462f4ecmshdbacb80693620b0p1ac60ejsna3ea048a05c5",
       'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
       }
conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
res = conn.getresponse()
data = res.read()
val = data.decode("utf-8")
corona=json.loads(val)
diction=[]
for item in corona:
       diction.append(item["Country"])
       diction.append(item["TotalCases"])
       diction.append(item["TotalDeaths"])
       diction.append(item["TotalRecovered"])

def update():
       conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
       headers = {
              'x-rapidapi-key': "7c7462f4ecmshdbacb80693620b0p1ac60ejsna3ea048a05c5",
              'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
              }
       conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
       res = conn.getresponse()
       data = res.read()
       val = data.decode("utf-8")
       corona=json.loads(val)
       diction=[]
       for item in corona:
              diction.append(item["Country"])
              diction.append(item["TotalCases"])
              diction.append(item["TotalDeaths"])
              diction.append(item["TotalRecovered"])
       output(diction)

def output(diction):
       text.delete("1.0", "end")
       for i in range(len(diction)):
              if diction[i] == "Japan":
                     textinsert="Країна:" + diction[i] + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість хворих:" + str(diction[i+1]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість смертей:" + str(diction[i+2]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість видужавших:" + str(diction[i+3]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="\n"
                     text.insert(END, textinsert)

              elif diction[i] == "China":
                     textinsert="Країна:" + diction[i] + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість хворих:" + str(diction[i+1]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість смертей:" + str(diction[i+2]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість видужавших:" + str(diction[i+3]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="\n"
                     text.insert(END, textinsert)
                     
              elif diction[i] == "Thailand":
                     textinsert="Країна:" + diction[i] + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість хворих:" + str(diction[i+1]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість смертей:" + str(diction[i+2]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість видужавших:" + str(diction[i+3]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="\n"
                     text.insert(END, textinsert)
                     
              elif diction[i] == "S. Korea":
                     textinsert="Країна:" + diction[i] + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість хворих:" + str(diction[i+1]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість смертей:" + str(diction[i+2]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість видужавших:" + str(diction[i+3]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="\n"
                     text.insert(END, textinsert)

              elif diction[i] == "India":
                     textinsert="Країна:" + diction[i] + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість хворих:" + str(diction[i+1]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість смертей:" + str(diction[i+2]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="Кількість видужавших:" + str(diction[i+3]) + "\n"
                     text.insert(END, textinsert)
                     textinsert="\n"
                     text.insert(END, textinsert)

tk.Button(text='Update info', bd=5,font=('Times New Roman', 20), command=update).place(x=90, y=90)                     
text=Text(win,height=50, width=30)
text.place(x=541, y=0)
output(diction)
win.mainloop()








