import urllib.request
import json

import logging
logging.basicConfig(level=logging.DEBUG)


def form_url_for_data(langcode, word):
    logging.info(f"language code {langcode} and word {word.strip()} is passed")
    # {language_code} the language you want to use
    url = f"https://api.dictionaryapi.dev/api/v2/entries/{langcode}/{word.strip()}"

    logging.info(f"url created is {url}")
    return url


def get_data_from_url(url):
    logging.info(f"url passed is {url}")
    content = urllib.request.urlopen(url)
    data = json.load(content)

    logging.info(f"data in json form {data}")
    return data


def get_phonetics_from_response(json_data):
    logging.info(f"json data passed {json_data}")
    return json_data[0]['phonetics']


def get_sound_links_from_response(json_data):
    logging.info(f"json data passed {json_data}")
    audio_list = []

    for item in (json_data[0]['phonetics']):
        logging.info(f" audio item extracted {item['audio']}")
        audio_list.append(item['audio'])

    return audio_list


def get_meanings_from_response(json_data):
    logging.info(f"Extracting meaning from json data")
    return json_data[0]['meanings']


def get_definitions_with_part_of_speech(meaning_list):
    logging.info(f"meaning list passed {meaning_list}")
    # will form a dict using key = part of speech and value = meaning for the speech
    definition_dict = {}

    for item in meaning_list:
        key = item['partOfSpeech']
        value = item['definitions']
        definition_dict[key] = value

    logging.info(f"definition dict created is {definition_dict}")
    return definition_dict

