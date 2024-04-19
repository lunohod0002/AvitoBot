import asyncio
import os

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


def phones_fun(text):
    pattern = re.compile(r"(\+\d{11}|\d{10,11})")
    results = pattern.findall(text)
    return results
from excel import get_first_two_columns, create_book
from pyrogram.types import Message

dic = {}
fio_number = {}

client = Client(name="12345", api_hash=api_hash, api_id=api_id)
name = 52

chat_id = 6678354902


async def send_first(dic, id):
    global name
    for row in dic.keys():

        await client.send_message("avinfoteka_bot", row)
        await asyncio.sleep(randint(15, 25))
        if dic[row]['fio'] != []:
            for data in dic[row]['fio']:
                await sp1(data[0], data[1])
                await asyncio.sleep(randint(7, 10))
        await asyncio.sleep(randint(7, 10))

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
            print(number)
            if (text.find("Марка, модель:") != -1):
                fisrt = text.find("Марка, модель:") + 15
                last = text.find("Год выпуска:") - 1
                if last == -2:
                    end_index = text.find('\n', fisrt)
                    if end_index != -1:
                        model2 = text[fisrt:end_index]
                else:
                    model2 = text[fisrt:last]
                print(model2)

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
            phones = phones_fun(mes)
            print(fio)
            print(phones)
            dic[number]['fio'] = list(dict.fromkeys(fio))
            dic[number]['phone'].extend(phones)
            for i in dic[number]['fio']:
                fio_number[i] = number

        count = + 1
        print(dic)


@client.on_message(filters.chat("rkorerysebesir222bot") and ~filters.outgoing and filters.bot)
async def second_bot(client: Client, message: Message):
    global dic, fio_number
    if message.text in ["Выберите доступные действия:",
                        "Выберите страну, чтобы осуществить поиск"] and message.reply_markup:
        if (message.reply_markup.inline_keyboard[0][0].text == '🇷🇺 Россия'):
            await asyncio.sleep(randint(2, 4))
            if message.reply_markup.inline_keyboard != None:
                try:
                    print(message.reply_markup.inline_keyboard)

                    await message.click(0, 0, timeout=5)
                except Exception as e:
                    print(e)
        else:
            if message.reply_markup.inline_keyboard != None:
                await asyncio.sleep(randint(2, 4))

                await message.click(0, 1, timeout=5)


    elif "ФИО: " in str(message.caption):
        print(message.caption)
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

        first = message.caption.find("Телефон: ") + 17
        last = message.caption.find("Транспорт: ") + 5
        phone = message.caption[first:last].split(", ")
        a = f"{fio},{birthd}".split(",")
        for i in fio_number:
            print(i, a)
            if tuple(a) == i:
                print("---------ураааааааа-----------")
                number = fio_number[i]
                dic[number]['phone'] += phone
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
                dic[key] = {'salt': salt, 'fio': [], 'model': '', 'phone': [], 'year': '', 'birthd': ''}

        await send_first(dic, int(message.chat.id))


client.run()
