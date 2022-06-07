def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Задание-1,2":
        dz12(bot, chat_id)

    elif ms_text == "Задание-3":
        dz3(bot, chat_id)

    elif ms_text == "Задание-4,5":
        dz45(bot, chat_id)

    elif ms_text == "Задание-6":
        dz6(bot, chat_id)

    elif ms_text == "Задание-7":
        dz7(bot, chat_id)

    elif ms_text == "Задание-8":
        dz8(bot, chat_id)

name = "Катерина"
age = 19


def dz12(bot, chat_id):
    bot.send_message(chat_id, text=f"Меня зовут {name}, мне {age} лет")


def dz3(bot, chat_id):
    bot.send_message(chat_id, text=name * 5)
    bot.send_message(chat_id, text=name + name + name + name + name)


def dz45(bot, chat_id):
    dz45_ResponseHandler1 = lambda user_name: my_inputInt(bot, chat_id, f"Здравствуйте, {user_name.text}! "
                                                                        f"Сколько вам лет?", dz45_ResponseHandler2)

    def dz45_ResponseHandler2(bot, chat_id, user_age):
        if 0 <= user_age < 18:
            bot.send_message(chat_id, text=f"О!В {user_age} дети уже могут разблокировать телефон, войти в интернет..")
        if 18 <= user_age < 45:
            bot.send_message(chat_id, text=f"О!В {user_age} уже не молодой, но все еще перспективный ")
        if 45 <= user_age < 150:
            bot.send_message(chat_id, text=f"О!В {user_age} уже можно законно называть  всех наркоманами ")

    my_input(bot, chat_id, "Как вас зовут?", dz45_ResponseHandler1)


def dz6(bot, chat_id):
    dz6_ResponseHandler = lambda message: bot.send_message(chat_id,
                                                           f"Добро пожаловать {message.text}! У тебя красивое имя, в нём {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", dz6_ResponseHandler, )

    # -----------------------------------------------------------------------


def dz7(bot, chat_id):
    def dz7_ResponseHandler1(user_name):
        global uname
        uname = user_name.text
        my_inputInt(bot, chat_id, f"Здравствуйте, {uname}! Сколько Вам лет?", dz7_ResponseHandler2)

    def dz7_ResponseHandler2(bot, chat_id, user_age):
        bot.send_message(chat_id, text=f"Длина Вашего имени - {len(uname)} символов")
        digit1 = user_age // 100
        digit2 = user_age // 10 % 10
        digit3 = user_age % 10
        if (digit1 == 0) and (digit2 == 0):
            product_of_numbers = digit3
            result = "Количество цифр Вашего возраста - 1"
        elif (digit1 == 0) and (digit2 != 0):
            product_of_numbers = digit2 * digit3
            result = "Количество цифр Вашего возраста - 2"
        else:
            product_of_numbers = digit1 * digit2 * digit3
            result = "Количество цифр Вашего возраста - 3"
        summ_of_numbers = digit1 + digit2 + digit3
        result += "\nСумма цифр возраста равна " + str(summ_of_numbers)
        result += "\nПроизведение цифр равно " + str(product_of_numbers)
        bot.send_message(chat_id, text=result)

    my_input(bot, chat_id, "Как вас зовут?", dz7_ResponseHandler1)


def dz8(bot, chat_id):
    dz8_ResponseHandler = lambda user_name: bot.send_message(chat_id,
                                                             text=f"{user_name.text.lower()}\n{user_name.text.upper()}\n{user_name.text.capitalize()}\n"
                                                                  f"{user_name.text.capitalize().swapcase()}")

    my_input(bot, chat_id, "Как вас зовут?", dz8_ResponseHandler)


def dz9(bot, chat_id):
    def dz9_ResponseHandler(bot, chat_id, answer):
        if answer == 6:
            bot.send_message(chat_id, text="Правильно!")
        else:
            bot.send_message(chat_id, text="Не правильно! Правильный ответ: 6")

    my_inputInt(bot, chat_id, "Сколько будет 2+2*2?", dz9_ResponseHandler)


# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)


# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt,
                                   ResponseHandler=ResponseHandler)


def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = int(message.text)
        # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                                 text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)



