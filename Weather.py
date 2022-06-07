def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "прислать погоду":
        send_geo(bot, chat_id)


def send_geo(bot,chat_id,ms_text):
    bot.send_message(chat_id, text="Отправь мне свою геопозицию, чтобы я мог вывести информацию о погоде")
    bot.delete_message(ms_text, chat_id)
    bot.register_next_step_handler(ms_text, get_weather)

def get_weather(message,bot,chat_id):
    import requests
    print(message.location)
    proxy = {
    'http': "http://116.54.113.15:7890",
    'https': "http://116.54.113.15:7890"
    }
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={message.location.latitude}&lon={message.location.longitude}&units=metric&appid=798593d7db58eacdf8755a741c332d8e', proxies = proxy, headers={'User-Agent': UserAgent().chrome}).json()
    bot.send_message(message.from_user.id, text=f'Ваше местоположение {res["sys"]["country"]}\n Температура: {res["main"]["temp"]}')
    bot.infinity_polling()
