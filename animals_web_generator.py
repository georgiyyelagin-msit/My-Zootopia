import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)



json_string = load_data('animals_data.json')

def key_present_in_dictionary(key, dictionary):
  return key in dictionary

for item in json_string:
  name = ""
  diet=""
  location=""
  type=""
  name = item["name"]
  diet = item["characteristics"]["diet"]
  location = item["locations"][0]
  if key_present_in_dictionary("type", item["characteristics"] ):
    type = item["characteristics"]["type"]
  print(f"Name: {name}")
  print(f"Diet: {diet}")
  print(f"Location: {location}")
  if type !="":
    print(f"Type: {type}")
