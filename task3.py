import json
import tkinter as tk
from tkinter import
from tkinter import messagebox
import http.client
import sys
 
 win = tk.Tk()
 win.geometry(f"820x1080+100+200")
 win.title ("covid")

 def upd():
 	connect = http.client.HTTPSConnection("vaccovidlive-vaccovidlive-default/api/vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

 	headers = {
 	"x-rapidapi-key": "08f3c4c438msh9375243ba2ee924p14eff1jsncce3f03639ee"
	"x-rapidapi-host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
 	}
 	connect.req("Get", "/api/npm-covid-data/asia")
 	res = connect.getres()
 	data = res.read()
 	em = data.decode("utf-8")
 	corona=json.loads(val)
	for item in corona:
    	print(val)
 	js = json.loads(corona)

 	dict=[]
 	for item in js:
 		dict.append(item["COUNTRY"])
 		dict.append(item["TOTAL_CASES"])
 		dict.append(item["TOTAL_DEATHS"])
 		dict.append(item["TOTAL_RECOVERED"])

 tk.Button(text='Update info', bd=5,font=('Times New Roman', 20), command=update).place(x=90, y=700)


 	def output(dict)
 		text_1.delete("1.0", "end")
 		for i in range(len(dict))
 			if dict[i] == "Japan":
 				textinsert="Країна:" + diction[i] + "\n" 
 				text.insert(END, textinsert) 
 				textinsert="Кількість хворих:" + str(diction[i+1]) + "\n" 
 				text.insert(END, textinsert)
 				textinsert="Кількість смертей:" + str(diction[i+3]) + "\n"
 				text.insert(END, textinsert) 
 				textinsert="Кількість видужавших:" + str(diction[i+4]) + "\n"
 				text.insert(END, textinsert) 
 				textinsert="\v" 
 				text_1.insert(END, textinsert)

 			elif dict[i] == "China":
 				textinsert="Країна:" + diction[i] + "\n" 
 				text.insert(END, textinsert) 
 				textinsert="Кількість хворих:" + str(diction[i+1]) + "\n" 
 				text.insert(END, textinsert)
 				textinsert="Кількість смертей:" + str(diction[i+3]) + "\n"
 				text.insert(END, textinsert) 
 				textinsert="Кількість видужавших:" + str(diction[i+4]) + "\n"
 				text.insert(END, textinsert) 
 				textinsert="\v" 
 				text_1.insert(END, textinsert)

 			elif dict[i] == "Thailand":
 				textinsert="Країна:" + diction[i] + "\n" 
 				text.insert(END, textinsert) 
 				textinsert="Кількість хворих:" + str(diction[i+1]) + "\n" 
 				text.insert(END, textinsert)
 				textinsert="Кількість смертей:" + str(diction[i+3]) + "\n"
 				text.insert(END, textinsert) 
 				textinsert="Кількість видужавших:" + str(diction[i+4]) + "\n"
 				text.insert(END, textinsert) 
 				textinsert="\v" 
 				text_1.insert(END, textinsert)

 			elif dict[i] == "India":
 				textinsert="Країна:" + diction[i] + "\n" 
 				text.insert(END, textinsert) 
 				textinsert="Кількість хворих:" + str(diction[i+1]) + "\n" 
 				text.insert(END, textinsert)
 				textinsert="Кількість смертей:" + str(diction[i+3]) + "\n"
 				text.insert(END, textinsert) 
 				textinsert="Кількість видужавших:" + str(diction[i+4]) + "\n"
 				text.insert(END, textinsert) 
 				textinsert="\v" 
 				text_1.insert(END, textinsert)

 			elif dict[i] == "South Korea":
 				textinsert="Країна:" + diction[i] + "\n" 
 				text.insert(END, textinsert) 
 				textinsert="Кількість хворих:" + str(diction[i+1]) + "\n" 
 				text.insert(END, textinsert)
 				textinsert="Кількість смертей:" + str(diction[i+3]) + "\n"
 				text.insert(END, textinsert) 
 				textinsert="Кількість видужавших:" + str(diction[i+4]) + "\n"
 				text.insert(END, textinsert) 
 				textinsert="\v" 
 				text_1.insert(END, textinsert)

output(diction)

text=Text(window,height=50, width=30)
text.place(x=541, y=0)
for item in js:
	inserttetx=item["Country"]+"\v" 
	text.insert(END, inserttetx)
window.mainloop()





