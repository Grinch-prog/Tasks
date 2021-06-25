import telebot
import json
import config
import http.client
import sys


diction=[]
bot = telebot.TeleBot(config.TOKEN)
jso={}

def renew():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "7c7462f4ecmshdbacb80693620b0p1ac60ejsna3ea048a05c5",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    corona = data.decode("utf-8")
    global jso
    jso = json.loads(corona)
    diction=[]
    for item in jso:
        diction.append(item["Country"])
        diction.append(item["TotalCases"])
        diction.append(item["TotalDeaths"])
        diction.append(item["TotalRecovered"])
    return diction

@bot.message_handler(commands=['renew'])
def renew_cmd(message):
    renew()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Доброго дня, {0.first_name}!\n /help дізнайтеся що вміє бот". format(message.from_user, bot.get_me()), parse_mode = 'html')
    global diction
    diction=renew()
    f = open('text.txt', 'w')
    f.write("")
    f.close()
    return diction

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"\n list - список\n/update - оновить інформацію\n/search - пошук інформації за країною\n/txt - надасть текстовый файл с результатами пошуку \n/help - надасть список команд\n")

@bot.message_handler(commands=['list'])
def list_of_countr(message):
    c_list=[]
    clist=""
    i=0
    for item in jso:
        c_list.append(item["Country"])
        clist+=str(c_list[i]) + "\n"
        i+=1
    bot.send_message(message.chat.id, clist)

@bot.message_handler(commands=['search'])
def search(message):
    chat_id = message.chat.id
    country = message.text
    msg = bot.send_message(chat_id, 'Введіть країну:')
    bot.register_next_step_handler(msg, countr)
    return country
    
def countr(message):
    chat_id = message.chat.id
    country = message.text
    country=searching(country)
    msg = bot.send_message(chat_id, country)
    if country=="Такої країни немає.":
        country=""
    f = open('text.txt', 'a')
    f.write(str(country))
    f.close()

def searching(country):
    global diction
    search=str(country)
    if search not in diction:
        country="Такої країни немає."
    for i in range(len(diction)):
        if diction[i]==search:
            country="Країна:" + diction[i] + "\n"
            country+="Кількість хворих:" + str(diction[i+1]) + "\n"
            country+="Кількість смертей:" + str(diction[i+3]) + "\n"
            country+="Кількість видужавших:" + str(diction[i+5]) + "\n"
            country+="\n"
    return country

@bot.message_handler(commands=['txt'])
def txt(message):
    try:
        file = open('text.txt', 'r')
        bot.send_document(message.chat.id, file)
        file.close()
    except:
        bot.send_message(message.chat.id, "Ошибка! Вы не производили поиск, поэтому текстовый файл пуст!")

@bot.message_handler(commands=['txtreset'])
def txtreset(message):
    f = open('text.txt', 'w')
    f.write("")
    f.close()
    bot.send_message(message.chat.id, "Здійсніть пошук!")

bot.polling(none_stop=True)