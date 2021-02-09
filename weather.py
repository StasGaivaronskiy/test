from pyowm import OWM
import math
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('24a345956a2c1b5866917e8bec6cd548', config_dict)
mgr = owm.weather_manager()
place = input ('В каком городе?:')
observation = mgr.weather_at_place('place')
w = observation.weather
temp = w.temperature('celsius')['temp']
TempFloor = math.floor(temp)
print("В городе " + place + " сейчас " +  w.detailed_status )
print('Температура воздуха ' + str(TempFloor) + ' градуса по цельсию')
