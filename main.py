import asyncio
import os
from excel import get_first_two_columns, create_book
from pyrogram.types import Message
from random import randint
from pyrogram import Client, filters

import re
from config import api_id, api_hash



def fio_fun(text):
    pattern = re.compile(r"(\w+\s+\w+\s+\w+),\s*(\d{2}\.\d{2}\.\d{4})")
    results = []
    for match in pattern.finditer(text):
        if match:
            name = match.group(1)
            dob = match.group(2)
            results.append((name, dob))
    return results
def number_fun(text):
    pattern = re.compile(r"[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}", re.IGNORECASE)
    results = pattern.findall(text)
    return results

def cleaned_phones(phones):
    cleaned_numbers = []
    mas={}

    for number in phones:
        start_digit = number[0]
        unique_part = number[1:]
        mas[unique_part]=start_digit
    for i in mas:
        cleaned_numbers.append(mas[i]+i)
    return cleaned_numbers
def fio_fun2(text):
    pattern = re.compile(r"(\w+\s+\w+\s+\w+)\s*(\d{2}\.\d{2}\.\d{4})")
    results = []
    for match in pattern.finditer(text):
        if match:
            name = match.group(1)
            dob = match.group(2)
            results.append((name, dob))
    return results




def phones_fun(text):
    pattern = re.compile(r'^(?:\+7|7|8)\d{10}$')
    results = pattern.findall(text)
    return results


dic = {}
fio_number = {}

client = Client(name="12345", api_hash=api_hash, api_id=api_id)
name = 53

chat_id = 6678354902


async def send_first(dic, id):
    global name
    for row in dic.keys():

        await client.send_message("avinfoteka_bot", row)
        await asyncio.sleep(randint(15, 25))
        await client.send_message("rkorerysebesir222bot", row)
        await asyncio.sleep(randint(12, 16))

        if dic[row]['fio'] != []:
            dic[row]['fio'] = list(dict.fromkeys(dic[row]['fio']))
            dic[row]['fio'] = list(filter(None, dic[row]['fio']))

            for data in dic[row]['fio']:
                await sp1(data[0], data[1])
                await asyncio.sleep(randint(7, 10))
        await asyncio.sleep(randint(7, 10))

        if dic[row]['phone'] != []:
            dic[row]['phone'] = list(dict.fromkeys(dic[row]['phone']))
            dic[row]['phone'] = list(filter(None, dic[row]['phone']))

            dic[row]['phone']=cleaned_phones(dic[row]['phone'] )

    list_of_dicts = [{**v, 'number': k} for k, v in dic.items()]
    name = name + 1
    create_book(f"Answer{name}.xlsx", list_of_dicts)
    await client.send_document(id, f"Answer{name}.xlsx")
    os.remove(f"Answer{name}.xlsx")
    dic.clear()
    fio_number.clear()


async def sp1(fio: str, date: str):
    if not fio.strip() and not date.strip():
        return
    result = await client.send_message("rkorerysebesir222bot", f"{fio}, {date}")


async def sp2(fio):
    if not fio.strip():
        return
    result = await client.send_message("rkorerysebesir222bot", f"{fio}")


@client.on_message(filters.chat("avinfoteka_bot"))
async def wdwf(client, message: Message):
    global dic, fio_number
    if message.reply_to_message != None:
        number = message.reply_to_message.text.strip()
        text = str(message.text).strip()

        if text.find("Возможные владельцы:") == -1 and message.text != None:
            # if (text.find("Владелец: ") != -1):
            #     fisrt = text.find("Владелец: ") + 10
            #     last = text.find("VIN:") - 1
            #     if last == -2:
            #         fio2 = text[fisrt:]
            #     else:
            #         fio2 = text[fisrt:last]
            #
            #     dic[number]['fio'] = fio2
            #
            #     (fio2 + "-------fio")
            #
            #     if fio2.count("*") != 0:
            #         fio2.replace("*", "")
            if (text.find("Машина:") != -1):
                fisrt = text.find("Машина:") + 8
                last1 = text.find("Количество владельцев:") - 1
                last2 = text.find("Дата операции:") - 1
                last = last2
                if last2 == -2:
                    last = last1
                model2 = text[fisrt:last]
                dic[number]['model'] = model2
            if (text.find("Марка, модель:") != -1):
                fisrt = text.find("Марка, модель:") + 15
                last = text.find("Год выпуска:") - 1
                model2 = text[fisrt:last]

                if last == -2:
                    end_index = text.find('\n', fisrt)
                    if end_index != -1:
                        # Возвращаем подстроку от 'a' до 'end_index'
                        model2 = text[fisrt:end_index]
                else:
                    model2 = text[fisrt:last]
                dic[number]['model'] = model2

            if (text.find("Год машины:") != -1):
                fisrt = text.find("Год машины:") + 12
                last = text.find("Год машины:") + 16
                year2 = text[fisrt:last]
                dic[number]['year'] = year2
            if (text.find("Год выпуска:") != -1):
                fisrt = text.find("Год выпуска:") + 12
                last = text.find("Год выпуска:") + 16
                year2 = text[fisrt:last]
                dic[number]['year'] = year2

            if (text.find("Телефон:") != -1):
                fisrt = text.find("Телефон:") + 9
                last = text.find("Телефон:") + 20
                phone2 = text[fisrt:last]
                dic[number]['phone'].append(phone2)

                (phone2)

        elif text.find("Возможные владельцы:") != -1 and message.text != None:
            if (text.find("Марка, модель:") != -1):
                fisrt = text.find("Марка, модель:") + 15
                last = text.find("Год выпуска:") - 1
                if last == -2:
                    end_index = text.find('\n', fisrt)
                    if end_index != -1:
                        model2 = text[fisrt:end_index]
                else:
                    model2 = text[fisrt:last]

                dic[number]['model'] = model2
            if (text.find("Год выпуска:") != -1):
                fisrt = text.find("Год выпуска:") + 12
                last = text.find("Год выпуска:") + 17
                year2 = text[fisrt:last]
                dic[number]['year'] = year2
            if (text.find("Связанные с гос. номером") != -1):
                last = text.find("Связанные с гос. номером") - 2
            else:
                last = -1
            first = text.find("Возможные владельцы:") + 21
            mes = text[first:last]
            fio = fio_fun(mes)

            phones = phones_fun(text)
            (fio)
            (phones)
            dic[number]['fio'] = list(dict.fromkeys(fio))
            dic[number]['phone'].extend(list(dict.fromkeys(phones)))
            for i in dic[number]['fio']:
                fio_number[i] = number

        count = + 1
        print(dic)



@client.on_message(filters.chat("rkorerysebesir222bot") and ~filters.outgoing and filters.bot)
async def second_bot(client: Client, message: Message):
    global dic, fio_number
    (message.text)

    if message.text in ["Выберите доступные действия:",
                        "Выберите страну, чтобы осуществить поиск"] and message.reply_markup:
        if (message.reply_markup.inline_keyboard[0][0].text == '🇷🇺 Россия'):
            await asyncio.sleep(randint(2, 4))
            if message.reply_markup.inline_keyboard != None:
                try:

                    await message.click(0, 0, timeout=5)
                except Exception as e:
                    (e)
        else:
            if message.reply_markup.inline_keyboard != None:
                await asyncio.sleep(randint(2, 4))

                await message.click(0, 1, timeout=5)
    elif "запись заблокирована: " in str(message.caption):
        ("!!!!!!!!!!!!!да бл!!!!!!!!!!!!!!!!!")
        try:

            await message.click(0, 0, timeout=5)
        except Exception as e:
            (e)
    elif str(message.text).find("Интересовались")!=-1:
        text=str(message.text).replace("\"РЕСО\\-Гарантия\"","")
        mas = text.replace("├", "").replace("└", "").replace("\n", "").split(" ")
        mas = list(filter(None, mas))
        for i in range(len(mas) - 1):
            (mas[i])
            mas[i] = mas[i][0].upper() + mas[i][1:].lower()
        text = " ".join(mas)
        fio = fio_fun2(text)
        phone=phones_fun(text)
        if phone!=[]:
            (phone)
        first = text.find("Номер: ") + 7
        last = text.find("Субъект:") -   1
        number =text[first:last].upper().replace("\n", "")
        ({number})
        (fio)
        dic[number]['phone'] += phone
        dic[number]['fio'] += fio
        for i in fio:
            fio_number[i] = number
    elif "ФИО: " in str(message.caption):

        (message.caption)
        first = message.caption.find("ФИО: ") + 6
        last = message.caption.find("День рождения: ") - 1
        fio = message.caption[first:last].strip()

        birthd = ""
        if last == -2:
            last = message.caption.find("Страна: ") - 2
        if last != -2:
            first = message.caption.find("День рождения: ") + 18
            last = message.caption.find("День рождения: ") + 28
            birthd = message.caption[first:last]
        if message.caption.find("Телефонов: ") == -1:
            if message.caption.find("Телефон: ") !=-1:

                first = message.caption.find("Телефон: ") + 17
                last = message.caption.find("Транспорт: ") + 5
                phone = message.caption[first:last].split(", ")
                a = f"{fio},{birthd}".split(",")
                for i in fio_number:
                    (i, a)
                    if tuple(a) == i:
                        ("---------ураааааааа-----------")
                        number = fio_number[i]
                        dic[number]['phone'] += phone
                (dic)
    elif str(message.caption).find("Личности")!=-1:
        text = message.caption
        number=number_fun(text)
        if number!=[]:
            number=number[0]
        mas = text.split(" ")
        mas = list(filter(None, mas))
        print(number)
        for i in range(len(mas)):
            mas[i] = mas[i][0].upper() + mas[i][1:].lower()
        text = " ".join(mas)

        fio = fio_fun2(text)
        fio = list(dict.fromkeys(fio))
        print(f"----------------------{fio}--------------------")
        if text.find("Телефонов: ") == -1:
            if text.find("Телефон: ") !=-1:
                first = text.find("Телефон: ") + 9
                last = text.find("Транспорт: ") + -2
                phone = text[first:last].replace("\n", "")
                phone = phone.split(", ")
                (phone)

                dic[number]['phone'] += phone

        dic[number]['fio'] += fio
        (fio,phone)
        for i in fio:
            fio_number[i] = number
    print(dic)


@client.on_message(filters.private and ~filters.outgoing and ~filters.bot)
async def handle_document(client: Client, message: Message):
    global dic

    if message.document.file_name.endswith(".xlsx") or message.document.file_name.endswith(
            ".xls"):
        file_path = f'document_{message.document.file_id}_{message.chat.id}.{message.document.file_name.split(".")[-1]}'
        await client.download_media(message, file_path)
        user_id = message.from_user.id
        lis = get_first_two_columns(file_path)
        for row in lis:

            if row[0] != None and row[1] != None:
                key, salt = row
                dic[key.upper()] = {'salt': salt, 'fio': [], 'model': '', 'phone': [], 'year': '', 'birthd': ''}

        await send_first(dic, int(message.chat.id))

if __name__ == '__main__':
    client.run()
