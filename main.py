import asyncio

import pyrogram.types
from pyrogram import Client, filters, storage

storage = storage.MemoryStorage("db", "12345")

import time
from pyrogram.types import Message

dict = {}
api_hash = "bf415d663df907799d4774c73806e713"
api_id = "27996868"
client = Client(name="12345",api_hash=api_hash,api_id=api_id)
chat_id = 6678354902
finalDict = list()
fio = ""
birthd = ""
phone2 = ""
model = ""
year = ""
fio2 = ""
year2 = ""
model2 = ""
phones = ""


@client.on_message(filters.chat("avinfoteka_bot"))


def all_messges(client: Client, mesage: Message):
    # mesage.reply(mesage.text,quote=True,reply_to_message_id=mesage.id)
    global phones, dict, count, fio, fio2, year2, year, birthd, model, model2, phone2

    message = str(mesage.text)

    number = message[14:23]
    if number not in dict:
        dict[number] = {}
    print(number)
    if str(mesage.text).find("Субъект РФ") == -1:
        start_time = time.time()

        print(mesage.text)
        mesage = str(mesage.text)
        if (mesage.find("Владелец: ") != -1):
            fisrt = mesage.find("Владелец: ") + 10
            last = mesage.find("VIN:") - 1
            fio2 = mesage[fisrt:last]
            dict[number]['fio'] = fio2

            print(fio2 + "-------fio")

            if fio2.count("*") != 0:
                fio2.replace("*", "")
        if (mesage.find("Машина:") != -1):
            fisrt = mesage.find("Машина:") + 8
            last = mesage.find("Дата операции:") - 1
            model2 = mesage[fisrt:last]
            dict[number]['model'] = model2

            print(model2)
        if (mesage.find("Год машины:") != -1):
            fisrt = mesage.find("Год машины:") + 12
            last = mesage.find("Год машины:") + 17
            year2 = mesage[fisrt:last]
            dict[number]['year'] = year2

            print(year2)
        if (mesage.find("Телефон:") != -1):
            fisrt = mesage.find("Телефон:") + 9
            last = mesage.find("Телефон:") + 20
            phone2 = mesage[fisrt:last]
            dict[number]['phone'] = phone2

            print(phone2)

    else:
        mesage = str(mesage.text)
        if (mesage.find("Владелец: ") != -1):

            fisrt = mesage.find("Владелец: ") + 10
            last = mesage.find("дата рождения:") - 2
            if last == -3:
                last = len(mesage) - 1
                fio3 = mesage[fisrt:last].split(" ")
            fio = mesage[fisrt:last]
            print(fio)
        if (mesage.find("дата рождения: ") != -1):
            fisrt = mesage.find("дата рождения: ") + 15
            last = mesage.find("дата рождения: ") + 25
            birthd = mesage[fisrt:last]
            dict[number]['birthd'] = birthd

        if (mesage.find("Связанные с гос. номером") != -1 and fio != "" and birthd != ""):
            indexes = [
                index for index in range(len(mesage))
                if mesage.startswith(f"Владелец: {fio}, дата рождения: {birthd}", index)
            ]
            for i in indexes:
                fisrt = i - 31
                last = i - 20
                phones = phones + " " + mesage[fisrt:last]
            dict[number]['phone'] += phones

            print(phones)

    count = + 1


@client.on_message(filters.chat("rkorerysebesir222bot"))
def all_messges2(client: Client, mesage: Message):
    global phones, dictlist
    print(dictlist)
    if mesage.text == "Выберите доступные действия:" or mesage.text == "Выберите страну, чтобы осуществить поиск":
        mesage.click(0, 1)
    elif str(mesage.caption).find("ФИО: ") != -1:
        message = str(mesage.caption)

        fisrt = message.find("Личности: ") + 10
        last = message.find("Телефон: ") - 3
        string = message[fisrt:last]
        if string.isdigit():
            pass
        else:

            fisrt = message.find("Телефон: ") + 9
            last = message.find("Транспорт: ") - 2
            phone2 = message[fisrt:last]
            print(phone2)
            phones = phones + phone2
            dictlist[i]["phone"] += phone2




# Отправляем ответ на inline запрос

client.start()
a = []
i=0
mas = ["Т999АВ199", "C234AB199"]
dict[mas[i]] = {}

for name in mas:
    dict[name] = {}
    while True:
        if len(dict[name])!={}:
            break
        else:
            client.start()

            client.send_message("avinfoteka_bot",name)
            client.stop()
            asyncio.sleep(7)

