# imports
from pyowm import OWM
from pyowm.utils.config import get_default_config
import math
import telebot
import constants


bot = telebot.TeleBot(constants.TELEGRAM_BOT_TOKEN)

@bot.message_handler(content_types=['text'])
def HandleBotMessage(message):
    # get config:
    config = getConfig()

    # create weather manager
    weatherManager = createWeatherManager(config)

    # get weather
    temperatureFloor, weather = getWeather(weatherManager, message.text)
    if temperatureFloor == 0 or weather == 0:
        sendMessageToUserIfError(message)
        return
    observation = weatherManager.weather_at_place (message.text)
    weather = observation.weather
    temperature = weather.temperature('celsius')['temp']
    temperatureFloor = math.floor(temperature)

    # send message to user about weather
    sendMessageAboutWeatherToUser(message, weather, temperatureFloor)

def sendMessageAboutWeatherToUser(message, weather, temperatureFloor):
    answer = "В городе " + message.text + " сейчас " +  weather.detailed_status +'\n'
    answer += 'Температура воздуха ' + str(temperatureFloor) + ' градусов по Цельсию'
    bot.send_message(message.chat.id,answer)


def sendMessageToUserIfError(message):
    answer = str(message.text) + ' не является городом'
    bot.send_message(message.chat.id, answer)


def getConfig():
    config = get_default_config()
    config['language'] = 'ru'
    return config


def createWeatherManager(resultConfig):
    openWeatherMap = OWM(constants.OPEN_WEATHER_MAP, resultConfig)
    weatherManager = openWeatherMap.weather_manager()
    return weatherManager


def getWeather(manager,place):
    try:
        observation = manager.weather_at_place (place)
    except:
        return 0, 0
    weather = observation.weather
    temperature = weather.temperature('celsius')['temp']
    temperatureFloor = math.floor(temperature)
    return temperatureFloor, weather


def printWeather(place,weather,temperatureFloor):
    print("В городе " + place + " сейчас " +  weather.detailed_status)
    print('Температура воздуха ' + str(temperatureFloor) + ' градусов по Цельсию')


def createNewBot():
    bot = telebot.TeleBot(constants.TELEGRAM_BOT_TOKEN)
    return bot

# start program
bot.polling(none_stop = True)
