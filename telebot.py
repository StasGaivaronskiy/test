#imports
import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config
import math

#get config
config = get_default_config()
config['language'] = 'ru'

#set token
bot = telebot.TeleBot("1623930936:AAFP3vXEu8j52wBfWJxS6URsSMsjYOYXKTI")
openWeatherMap = OWM('24a345956a2c1b5866917e8bec6cd548', config)
manager = openWeatherMap.weather_manager()

#main
@bot.message_handler(content_types=['text'])
def echo_all(message):
    try:
        observation = manager.weather_at_place (message.text)
    except Exception:
        answer = str(message.text) + ' не является городом'
        bot.send_message(message.chat.id,answer)
        return
    weather = observation.weather
    temperature = weather.temperature('celsius')['temp']
    temperatureFloor = math.floor(temperature)

    #print weather
    answer = "В городе " + message.text + " сейчас " +  weather.detailed_status +'\n'
    answer += 'Температура воздуха ' + str(temperatureFloor) + ' градусов по Цельсию' 
    bot.send_message(message.chat.id,answer)

bot.polling(none_stop = True)