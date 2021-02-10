#imports
from pyowm import OWM
import math
from pyowm.utils.config import get_default_config

#main func
def main():
    #get config:
    resultConfig = getConfig()
    
    #set token
    manager = setToken(resultConfig)

    #set place
    place = input ('В каком городе?:')

    #get weather
    temperatureFloor, weather = getWeather(manager,place)

    #print weather
    printWeather(place,weather,temperatureFloor)

def getConfig():
    config = get_default_config()
    config['language'] = 'ru'
    return config

def setToken(resultConfig):
    openWeatherMap = OWM('24a345956a2c1b5866917e8bec6cd548', resultConfig)
    manager = openWeatherMap.weather_manager()
    return manager

def getWeather(manager,place):
    observation = manager.weather_at_place (place)
    weather = observation.weather
    temperature = weather.temperature('celsius')['temp']
    temperatureFloor = math.floor(temperature)
    return temperatureFloor, weather

def printWeather(place,weather,temperatureFloor):
    print("В городе " + place + " сейчас " +  weather.detailed_status)
    print('Температура воздуха ' + str(temperatureFloor) + ' градусов по цельсию')

#start program
main()
