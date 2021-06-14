import telebot
from telebot import types
from datetime import datetime
from db_key import *
from config import *
now = datetime.now()
bot = telebot.TeleBot(TOKEN)
emoji = {'sad': '\U0001F614', 'next': '\U000027A1', 'back': '\U00002B05', 'loading': '\U0000231B','know':'\U0001F393',
         'map': '\U0001F5FA', 'ok': '\U0001F609', 'no': '\U0000274C', 'yes': '\U00002705','kamen':'\U0001F5FF','help':'\U0001F4A1'}
map_list = ['mirage', 'inferno', 'dust2', 'train', 'overpass', 'vertigo', 'cache', 'nuke', 'ancient']
map_names = {
    'mirage': 'https://sun9-62.userapi.com/impg/HLdD6Kl1VPDmErUNN0UgaEdX6KXKkU-672kM2w/pXuZMAh0RAs.jpg?size=992x821&quality=96&sign=24e46b03b1c0d58aa7e100e2e6a4cd90&type=album',
    'nuke': 'https://sun9-1.userapi.com/impg/GmlaMxi7xzz0vHyEwsQ8HUrf7qYwCA0jXIJP8A/POhBbl0uMhA.jpg?size=2000x2000&quality=96&sign=884294cb1bcb9e73d87a0782511766b2&type=album',
    'inferno': 'https://psv4.userapi.com/c536236/u320503302/docs/d38/5943de48d0b5/inferno.png?extra=MZNY9xoRBj7t_7hKhBOeHOsRh-PnXRJD8G8bp9wzgbf6YRXkd-zdIo_WX_l3ElMX6L1e3OpH2euB_GmDdKKQEqs731-wz0PE_af8h9BpOn1eP7oPvie51hPzZKjh8_37r0hkNn-iYnwenbeexrlfym9U',
    'train': 'https://psv4.userapi.com/c536236/u320503302/docs/d10/70920a4afb8c/train.png?extra=o78ULu2CS62gLiGjEvUimmZwNHrAIVCxlHapPu7ZNeKOkzu7-EXyW9jpTBGJDM8q0zoYKWazsNcYCWnhWtBftjWPVMZrKa8fgdhmmyJqMLNQxaH4llvwRhyLy4dG7i7yHeOo_hAu0ntuBDhjoZoxTlH3',
    'dust2': 'https://sun9-2.userapi.com/impg/CVocNKZbE1zltjPTlI3KlF1hEeSyHbe7Xs84sQ/QnPbYCQtVrg.jpg?size=2000x2000&quality=96&sign=c6d7b6ef10f8e921dc74917e533b8bc7&type=album',
    'vertigo': 'https://psv4.userapi.com/c536236/u320503302/docs/d1/4fb4f2cfd2e9/vertigo.png?extra=EyIx8LTJ92AI_XeqCJVWg62hfJSQtCNo5zIf59H4AR897dAgGfA86rwDsKyO483kljRgqe-zyjlB0NzJ9cGFaqnzhrjCuH40gQhPEMl5JTcEOGPAn68-3rvs-wLYUHmeoelqqhk-YqgP3L-c682v20SC',
    'cache': 'https://psv4.userapi.com/c536236/u320503302/docs/d12/72f3c88eea7e/cache.png?extra=iRGjYUXp-bgbF2clpRL5Xy0bJEfkse7qM29pb25ynUIahF3WdSbxi2snupS-ELIJsWKSsauJHqnJnn4qI7YNLMWQ_IpsGKIJ7QE5NTiD2wg1kynVLF0H9ZlXMQb12kvzbkcTVHwnOgKWPsYjgHqKjVrh',
    'overpass': 'https://psv4.userapi.com/c536236/u320503302/docs/d28/c0a4a654d463/overpass.png?extra=VB7qTescDb0VzqDoqZpQg8ZiDEdi1fCqt0ypHpxfvKK7jvc0122z1rp_5ZNmParozjwqFkruVLU00gGa6H_YBrcuSblsiN721vo1O4VzxBKfzrCHYjJQ0uT8Ldqyh03AL-3IT5Dl_SofL_c2Q48mTJqt',
    'ancient': 'https://psv4.userapi.com/c536236/u320503302/docs/d46/86ab3d3903c8/ancient.png?extra=jyhzoQRuXOyZyJxhZJ85mZ9WA78pGeNe0nLxzCCKHsRy2baUxDq-9ThsSUTB0IAqPN9_9gg0kAgivMIfp9HVOCrr0gRFQIVL36J7RwOcWZ_UPiTOwEyxgmid19giyT0-vGp2wVuBa7yapfa1D_w8Z45j'}


@bot.message_handler(commands=['adminpost'])
def admin(message):
    if str(message.chat.id) == ADMIN_ID:
        id_list = id_take()
        for i in id_list:
            for j in i:
                print(j, type(j))
                try:
                    bot.send_message(j, message.text[message.text.find(' '):])
                except:
                    print(f"USER {j} BLOCKED BOT")
        print(f"ADMIN SEND MESSAGE  {message.text[message.text.find(' '):]} FROM ALL USERS")
        bot.send_message(message.from_user.id,
                         f"YOUR MESSAGE {message.text[message.text.find(' '):]} HAS BEEN SENT TO : \n{users_count()} USERS")

    else:
        bot.send_message(message.from_user.id, "PERMISSION ERROR")


@bot.message_handler(commands=['users_count'])
def user_count(message):
    if str(message.chat.id) == ADMIN_ID:
        bot.send_message(message.from_user.id, f"Общее количество пользователей:\n{users_count()}")
    else:
        bot.send_message(message.from_user.id, "PERMISSION ERROR")


@bot.message_handler(commands=['start', 'help'])
def addUser(message):
    print(f"{now}  "
          f"U_id - {message.chat.id},"
          f"F_name-{message.chat.first_name},"
          f"L_name-{message.chat.last_name},"
          f"U_name-{message.chat.username}"
          )
    bot.send_message(message.from_user.id, f"Привет.Я знаю все гранаты в CSGO."
                                           f"\nВыбери на клавиатуре карту,если у тебя нет клавиатуры напиши /maps."
                                           f"(или нажми на команду {emoji['kamen']})"
                                           f"\nВ ответ я тебе пришлю карту с номерами позиций."
                                           f"\nТебе остаётся выбрать только позицию ")

    addUserToDB(message.chat.first_name, message.chat.last_name, message.chat.username, message.chat.id, now)


@bot.message_handler(commands=['maps'])
def start_func(message):
    keyboard = types.ReplyKeyboardMarkup()
    button_de_mirage = types.KeyboardButton(text="mirage")
    button_de_inferno = types.KeyboardButton(text="inferno")
    button_de_dust2 = types.KeyboardButton(text="dust2")
    button_de_nuke = types.KeyboardButton(text="nuke")
    button_de_overpass = types.KeyboardButton(text="overpass")
    button_de_vertigo = types.KeyboardButton(text="vertigo")
    button_de_cache = types.KeyboardButton(text="cache")
    button_de_train = types.KeyboardButton(text="train")
    button_de_ancient = types.KeyboardButton(text="ancient")

    keyboard.add(button_de_mirage, button_de_inferno, button_de_nuke, button_de_dust2, button_de_train,
                 button_de_ancient, button_de_vertigo, button_de_overpass, button_de_cache)
    bot.send_message(message.from_user.id, "BOT START", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    message_data = message.text.split()
    message_len = len(message_data)
    if map_names.get(message.text.lower()) != None:
        map_take_name = message.text.lower()
        print(map_take_name)
        markup_inline = make_keyboard_1()

        photo = map_names[map_take_name]
        bot.send_message(message.chat.id, f"{message_data}[.]({photo})", parse_mode='markdown',
                         reply_markup=markup_inline)
    else:
        bot.send_message(message.from_user.id,f"Если не получаеться,напишите /start или /help {emoji['help']}")


def make_keyboard_1():
    markup_inline_1 = types.InlineKeyboardMarkup()
    item_1 = types.InlineKeyboardButton(text='1', callback_data='1')
    item_2 = types.InlineKeyboardButton(text='2', callback_data='2')
    item_3 = types.InlineKeyboardButton(text='3', callback_data='3')
    item_4 = types.InlineKeyboardButton(text='4', callback_data='4')
    item_5 = types.InlineKeyboardButton(text='5', callback_data='5')
    item_6 = types.InlineKeyboardButton(text='6', callback_data='6')
    item_7 = types.InlineKeyboardButton(text='7', callback_data='7')
    item_8 = types.InlineKeyboardButton(text='8', callback_data='8')
    item_9 = types.InlineKeyboardButton(text='9', callback_data='9')
    item_10 = types.InlineKeyboardButton(text='10', callback_data='10')
    item_11 = types.InlineKeyboardButton(text='11', callback_data='11')
    item_next = types.InlineKeyboardButton(text=emoji['next'], callback_data='next_list_2')
    markup_inline_1.add(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11,
                        item_next)
    return markup_inline_1


def make_keyboard_2():
    markup_inline_2 = types.InlineKeyboardMarkup()
    item_12 = types.InlineKeyboardButton(text='12', callback_data='12')
    item_13 = types.InlineKeyboardButton(text='13', callback_data='13')
    item_14 = types.InlineKeyboardButton(text='14', callback_data='14')
    item_15 = types.InlineKeyboardButton(text='15', callback_data='15')
    item_16 = types.InlineKeyboardButton(text='16', callback_data='16')
    item_17 = types.InlineKeyboardButton(text='17', callback_data='17')
    item_18 = types.InlineKeyboardButton(text='18', callback_data='18')
    item_19 = types.InlineKeyboardButton(text='19', callback_data='19')
    item_20 = types.InlineKeyboardButton(text='20', callback_data='20')
    item_21 = types.InlineKeyboardButton(text='21', callback_data='21')

    item_back_list_1 = types.InlineKeyboardButton(text=emoji['back'], callback_data='back_list_1')
    item_next_list_3 = types.InlineKeyboardButton(text=emoji['next'], callback_data='next_list_3')
    markup_inline_2.add(item_12, item_13, item_14, item_15, item_16,item_17, item_18, item_19,item_20,
                        item_back_list_1,item_21, item_next_list_3)
    return markup_inline_2


def make_keyboard_3():
    markup_inline_3 = types.InlineKeyboardMarkup()
    item_22 = types.InlineKeyboardButton(text='22', callback_data='22')
    item_23 = types.InlineKeyboardButton(text='23', callback_data='23')
    item_24 = types.InlineKeyboardButton(text='24', callback_data='24')
    item_25 = types.InlineKeyboardButton(text='25', callback_data='25')
    item_26 = types.InlineKeyboardButton(text='26', callback_data='26')
    item_27 = types.InlineKeyboardButton(text='27', callback_data='27')
    item_28 = types.InlineKeyboardButton(text='28', callback_data='28')
    item_29 = types.InlineKeyboardButton(text='29', callback_data='29')
    item_30 = types.InlineKeyboardButton(text='30', callback_data='30')
    item_31 = types.InlineKeyboardButton(text='31', callback_data='31')
    item_back_list_2 = types.InlineKeyboardButton(text=emoji['back'], callback_data='back_list_2')
    markup_inline_3.add(item_22, item_23, item_24, item_25, item_26, item_27, item_28, item_29,
                        item_30,item_back_list_2,  item_31)
    return markup_inline_3


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    map_name = call.message.text
    true_map_name = ''
    photo= ''

    for i in map_list:
        if map_name.find(i) != -1:
            true_map_name = true_map_name + i
            photo = map_names[true_map_name]
    if call.data == 'next_list_2':
        markup_inline_2 = make_keyboard_2()
        bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                              text=f"{call.message.text}[.]({photo})", parse_mode='markdown',
                              reply_markup=markup_inline_2)
    elif call.data == 'back_list_1':
        markup_inline = make_keyboard_1()
        bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                              text=f"{call.message.text}[.]({photo})", parse_mode='markdown',
                              reply_markup=markup_inline)
    elif call.data == 'next_list_3':
        markup_inline_3 = make_keyboard_3()
        bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                              text=f"{call.message.text}[.]({photo})", parse_mode='markdown',
                              reply_markup=markup_inline_3)
    elif call.data =='back_list_2':
        markup_inline_4=make_keyboard_2()
        bot.edit_message_text(chat_id=call.from_user.id,message_id=call.message.message_id,
                                text=f"{call.message.text}[.]({photo})",parse_mode='markdown',
                                reply_markup=markup_inline_4)

    elif call.data == '1':
        date = datetime.now()


        link = db_take(true_map_name, '1')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id,f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №1 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date,'1','1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id,true_map_name,date,'1','0')
    elif call.data == '2':
        date = datetime.now()


        link = db_take(true_map_name, '2')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id,f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №2 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date,'2','1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date,'2','0')

    elif call.data == '3':
        date = datetime.now()


        link = db_take(true_map_name, '3')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №3 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date,'3','1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date,'3','0')

    elif call.data == '4':
        date = datetime.now()


        link = db_take(true_map_name, '4')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №4 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date,'4','1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date,'4','0')

    elif call.data == '5':
        date = datetime.now()


        link = db_take(true_map_name, '5')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №5 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date,'5','1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date,'5','0')


    elif call.data == '6':
        date = datetime.now()


        link = db_take(true_map_name, '6')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №6 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date,'6','1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date,'6','0')

    elif call.data == '7':
        date = datetime.now()


        link = db_take(true_map_name, '7')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №7 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date,'7','1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date,'7','0')

    elif call.data == '8':
        date = datetime.now()


        link = db_take(true_map_name, '8')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №8 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date,'8','1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date,'8','0')

    elif call.data == '9':
        date = datetime.now()


        link = db_take(true_map_name, '9')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №9 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date,'9','1',)
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date,'9','1')

    elif call.data == '10':
        date = datetime.now()


        link = db_take(true_map_name, '10')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №10 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '10', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '10', '0')

    elif call.data == '11':
        date = datetime.now()


        link = db_take(true_map_name, '11')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №11 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '11', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '11', '0')

    elif call.data == '12':
        date = datetime.now()


        link = db_take(true_map_name, '12')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №12 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '12', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '12', '0')

    elif call.data == '13':
        date = datetime.now()


        link = db_take(true_map_name, '13')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №13 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '13', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '13', '0')

    elif call.data == '14':
        date = datetime.now()


        link = db_take(true_map_name, '14')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №14 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '14', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '14', '0')

    elif call.data == '15':
        date = datetime.now()


        link = db_take(true_map_name, '15')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №15 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '15', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '15', '0')

    elif call.data == '16':
        date = datetime.now()
        link = db_take(true_map_name, '16')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №16 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '16', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '16', '0')

    elif call.data == '17':
        date = datetime.now()
        link = db_take(true_map_name, '17')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №17 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '17', '1')
                    except:
                        print('Video link error')
                        TestInsert(call.from_user.id, true_map_name, date, '17', '0')

    elif call.data == '18':
        date = datetime.now()
        link = db_take(true_map_name, '18')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №18 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '18', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '18', '0')

    elif call.data == '19':
        date = datetime.now()
        link = db_take(true_map_name, '19')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №19 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '19', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '19', '0')


    elif call.data == '20':
        date = datetime.now()
        link = db_take(true_map_name, '20')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №20 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '20', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '20', '0')

    elif call.data == '21':
        date = datetime.now()
        link = db_take(true_map_name, '21')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №21 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '21', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '21', '0')

    elif call.data == '22':
        date = datetime.now()
        link = db_take(true_map_name, '22')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №22 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '22', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '22', '0')

    elif call.data == '23':
        date = datetime.now()
        link = db_take(true_map_name, '23')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №23 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '23', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '23', '0')

    elif call.data == '24':
        date = datetime.now()
        link = db_take(true_map_name, '24')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №24 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '24', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '24', '0')

    elif call.data == '25':
        date = datetime.now()
        link = db_take(true_map_name, '25')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №25 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '25', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '25', '0')

    elif call.data == '26':
        date = datetime.now()
        link = db_take(true_map_name, '26')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №26 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '26', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '26', '0')

    elif call.data == '27':
        date = datetime.now()
        link = db_take(true_map_name, '27')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №27 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '27', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '27', '0')

    elif call.data == '28':
        date = datetime.now()
        link = db_take(true_map_name, '28')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №28 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '28', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '28', '0')

    elif call.data == '29':
        date = datetime.now()
        link = db_take(true_map_name, '29')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id,f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №29 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '29', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '29', '0')

    elif call.data == '30':
        date = datetime.now()
        link = db_take(true_map_name, '30')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №30 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '30', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '30', '0')

    elif call.data == '31':
        date = datetime.now()
        link = db_take(true_map_name, '31')
        print(link, type(link))
        if not link:
            bot.send_message(call.from_user.id, f"Я такой гранаты не знаю,скоро научусь {emoji['know']}")
        else:
            bot.send_message(call.from_user.id, f"Загружаю {true_map_name} №31 {emoji['loading']}")
            for i in link:
                for j in i:
                    try:
                        video = open(j, 'rb')
                        bot.send_video(call.from_user.id, video)
                        TestInsert(call.from_user.id, true_map_name, date, '31', '1')
                    except:
                        print('CANT OPEN VIDEO/LINK ERROR')
                        TestInsert(call.from_user.id, true_map_name, date, '31', '0')

    else:
        bot.send_message(call.from_user.id,f"Такой гранаты я еще не знаю, возможно в будущем я выучу {emoji['know']}.")


bot.polling(none_stop=True, interval=0)
