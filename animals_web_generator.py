import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)


def key_present_in_dictionary(key, dictionary):
  return key in dictionary


def get_animals_infos_json_as_string(json_string ):
  output=""
  for item in json_string:
    output += serialize_animal(item)
  return output


def serialize_animal(animal_obj):
  output = ""
  output += "<li class=\"cards__item\">"
  output += f"<div class=\"card__title\">{animal_obj["name"]}</div>\n"
  output += "<p class=\"card__text\">"
  output += f"<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n"
  output += f"<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n"

  if key_present_in_dictionary("type", animal_obj["characteristics"]):
    output += f"<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n"
  output += "  </p>"
  output += "</li>"
  return output


json_animals_infos_string = load_data('animals_data.json')
with open("animals_template.html", "r", encoding="utf-8") as handle:
  html_original_string = handle.read()

html_filled_wih_infos_as_string = html_original_string.replace("__REPLACE_ANIMALS_INFO__", get_animals_infos_json_as_string(json_animals_infos_string))

with open("animals.html", "w", encoding="utf-8") as handle:
  handle.write(html_filled_wih_infos_as_string)