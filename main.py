import json
import os
import geonamescache as gc
import requests
import datetime as dt
import pytz


# ------------------------------------
# Module_A

def set_settings_as_default(settings):
  current_dir = os.getcwd()
  with open(os.path.join(current_dir, "default_settings.json"), "w") as json_file:
    json.dump(settings, json_file)

def load_default_settings():
  current_dir = os.getcwd()
  with open(os.path.join(current_dir, "default_settings.json"), "r") as json_file:
    default_settings = json.load(json_file)
  return default_settings

def reset_favorites_list(settings = [['Type in a City Name']]):
  current_dir = os.getcwd()
  filename = os.path.join(current_dir, "favorite_settings.json")
  with open(filename, 'w') as json_file:
    json.dump(settings, json_file)

def save_settings_to_favorites(settings):
  current_dir = os.getcwd()
  filename = os.path.join(current_dir, "favorite_settings.json")

  # Load existing settings if the file exists
  if os.path.exists(filename):
    with open(filename, 'r') as json_file:
      all_settings = json.load(json_file)
  else:
    all_settings = 'Type in a City Name'

  all_settings_list = all_settings
  # Append new settings
  if settings not in all_settings_list:
    all_settings.append(settings)

  # Write updated settings back to the file
  with open(filename, 'w') as json_file:
    json.dump(all_settings_list, json_file)

def load_favorite_settings():
  current_dir = os.getcwd()
  with open(os.path.join(current_dir, "favorite_settings.json"), "r") as json_file:
    favorite_settings = json.load(json_file)
  return favorite_settings

def set_settings(settings_list = load_favorite_settings()):
  select = select_from_list(settings_list)
  if select == settings_list[0]:
    city_input = input('Type in a City Name')
    input_cities_gcdata = find_input_cities_gcdata(city_input)
    verified_city_input = verify_city_input(input_cities_gcdata)
    settings = make_settings(verified_city_input[0], verified_city_input[1], set_temp_units())
  else:
    settings = select
  return settings


# ---------------------------------
# Module_0
def select_from_list(lst):
  lst1 = {str(i) : item for i, item in enumerate(lst)}
  [print(f"[{key}] {value}") for key, value in lst1.items()]
  option = input(f"select option number: ")
  return lst1[option] if option in lst1 else None

def set_temp_units(units = ['Kelvin', 'Celsius', 'Fahrenheit']):
  selection = select_from_list(units)
  temp_units = 'standard' if (selection == units[0]) else ('metric' if (selection == units[1]) else 'imperial')
  return temp_units
def find_input_cities_gcdata(city_input):
  all_cities_cache = gc.GeonamesCache().get_cities()
  input_cities_gcdata = [value for key, value in all_cities_cache.items() if (city_input.lower().title() == value['name'] or city_input in value['alternatenames'] or city_input.lower().title() in value['alternatenames'])]
  return input_cities_gcdata

def verify_city_input(input_cities_gcdata):
  verified_city_input = []
  if len(input_cities_gcdata) == 0:
    print(f"Sorry, we did not find '{city_input}'..")
  elif len(input_cities_gcdata) == 1:
    verified_city_input.append(input_cities_gcdata[0]['name'])
    verified_city_input.append(input_cities_gcdata[0]['timezone'])
  else:
    input_cities_timezones = []
    for i, item in enumerate(input_cities_gcdata):
      input_cities_timezones.append([input_cities_gcdata[i]['name'], input_cities_gcdata[i]['timezone']])
    option = select_from_list(input_cities_timezones)
    verified_city_input = option
  return verified_city_input

def make_settings(name, tz, units):
  return [name, tz, units]

def set_settings(settings_list = load_favorite_settings()):
  select = select_from_list(settings_list)
  if select == settings_list[0]:
    city_input = input('Type in a City Name')
    input_cities_gcdata = find_input_cities_gcdata(city_input)
    verified_city_input = verify_city_input(input_cities_gcdata)
    settings = make_settings(verified_city_input[0], verified_city_input[1], set_temp_units())
  else:
    settings = select
  return settings

def get_current_owdata(settings = load_default_settings()):
  city_name = settings[0]
  temp_units = settings[2]
  ow_api_key = '0f4470337016fe83612563095537bf7a'
  url_call = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={ow_api_key}&units={temp_units}"
  city_owdata = requests.get(url_call)
  city_owdata = city_owdata.json()
  return city_owdata

def display_current_owdata(city_owdata, settings = load_default_settings()):
  city_name = settings[0]
  temp_units = settings[2]
  temp_unit = "C°" if temp_units == 'metric' else ("F°" if temp_units == 'imperial' else "K°")

  relevant_data = [
    city_owdata['weather'][0]['main'],
    city_owdata['weather'][0]['description'],
    city_owdata['main']['temp'],
    city_owdata['main']['feels_like'],
    city_owdata['main']['humidity']
  ]

  print(
    f"Current weather conditions for: '{city_name}' \n{'-' * (len('Current weather conditions for: ') + len(city_name) + 2)}",
    f"{'General:':17} {relevant_data[0]}\t'{relevant_data[1]}'",
    f"{'Temperature:':17} {relevant_data[2]}{temp_unit}\tfeels like {relevant_data[3]}{temp_unit}",
    f"{'Humidity Level:':17} {relevant_data[4]}%",
    sep='\n'
  )


# ------------------------------------
# Module_Alpha

def get_local_current_datetime():
  local_current_datetime_raw = dt.datetime.now()
  local_current_datetime = local_current_datetime_raw.strftime("%Y-%m-%d %H:%M:%S")
  return local_current_datetime

def display_local_current_datetime(local_current_datetime):
  print(f"Your current local date & time: \n{local_current_datetime}")

def get_city_current_datetime(settings):
  city_tz = settings[1]
  city_tzinfo = pytz.timezone(city_tz)
  city_current_datetime_raw = dt.datetime.now(tz=city_tzinfo)
  city_current_datetime = city_current_datetime_raw.strftime("%Y-%m-%d %H:%M:%S")
  return city_current_datetime

def display_city_current_datetime(settings, city_current_datetime):
  print(f"The current local date & time in {settings[0]}: \n{city_current_datetime}")


# ----------------------------------------
# ----------------------------------------
# Main

display_local_current_datetime(get_local_current_datetime())
current_settings = set_settings()
display_current_owdata(get_current_owdata(current_settings), current_settings)
display_city_current_datetime(current_settings, get_city_current_datetime(current_settings))

# set_settings_as_default(current_settings)
# load_default_settings()
# reset_favorites_list()
# save_settings_to_favorites(current_settings)
# load_favorite_settings()


