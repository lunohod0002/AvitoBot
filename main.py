from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
fio=""
birthd=""
model=""
year=""
fio2=""
year2=""
model2=""
phones=""
api_hash = "bf415d663df907799d4774c73806e713"
api_id = "27996868"
count=0
client= Client(name="12345", api_hash=api_hash, api_id=api_id)
client.start()
client.send_message("avinfoteka_bot","С044АХ199".lower())
client.stop()
@client.on_message(filters.chat("avinfoteka_bot"))
def all_messges(client:Client,mesage:Message):
    #mesage.reply(mesage.text,quote=True,reply_to_message_id=mesage.id)
    global phones
    global fio,fio2,year2,year,birthd,model,model2
    count=+1
    if count % 2 == 0:
        print(mesage.text)

        mesage = str(mesage.text)
        if (mesage.find("Владелец: ")!=-1):

            fisrt=mesage.find("Владелец: ")+10
            last=mesage.find("VIN:")-1
            fio2=mesage[fisrt:last]
            print(fio2)
        if (mesage.find("Марка, модель:") != -1):

            fisrt = mesage.find("Марка, модель:") + 15
            last = mesage.find("Год выпуска:") - 1
            model2 = mesage[fisrt:last]
            print(model2)
        if (mesage.find("Год выпуска:") != -1):

            fisrt = mesage.find("Год выпуска:") + 13
            last = mesage.find("Год выпуска:") + 17
            year2 = mesage[fisrt:last]
            print(year2)
    if count%2!=0:
        print(mesage.text)

        mesage=str(mesage.text)
        if (mesage.find("Владелец: ")!=-1):

            fisrt=mesage.find("Владелец: ")+10
            last=mesage.find("дата рождения:")-2
            fio=mesage[fisrt:last]
            print(fio)
        if (mesage.find("дата рождения: ") != -1):

            fisrt = mesage.find("дата рождения: ") + 15
            last = mesage.find("дата рождения: ") + 25
            birthd = mesage[fisrt:last]
            print(birthd)
        if (mesage.find("Марка, модель:") != -1):

            fisrt = mesage.find("Марка, модель:") + 15
            last = mesage.find("Год выпуска:") - 1
            model = mesage[fisrt:last]
            print(model)
        if (mesage.find("Год выпуска:") != -1):

            fisrt = mesage.find("Год выпуска:") + 13
            last = mesage.find("Год выпуска:") + 17
            year = mesage[fisrt:last]
            print(year)
        if (mesage.find("Связанные с гос. номером")!=-1 and fio!="" and birthd!=""):
            indexes = [
                index for index in range(len(mesage))
                if mesage.startswith(f"Владелец: {fio}, дата рождения: {birthd}", index)
            ]
            for i in indexes:
                fisrt=i-31
                last=i-20
                phones =phones+ mesage[fisrt:last]+","
            print(phones)

    if (fio==""):
        fio=fio2
    if (model==""):
        model=model2
    if (year==""):
        year=year2
client.run()
