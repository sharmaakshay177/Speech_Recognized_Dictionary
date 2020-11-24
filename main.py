from SpeechRecognitionForWord import return_word_after_listening
from SpeechRecognitionForWord import return_split_of_sentence
from GettingWordResposeByGoogleApi import form_url_for_data
from GettingWordResposeByGoogleApi import get_data_from_url
from GettingWordResposeByGoogleApi import get_sound_links_from_response
from GettingWordResposeByGoogleApi import get_meanings_from_response
from GettingWordResposeByGoogleApi import get_definitions_with_part_of_speech

import logging
logging.basicConfig(level=logging.DEBUG)


def get_definition_of_the_word(word):
    logging.info(f"word recognized is {word}")

    url = form_url_for_data('en', word)
    logging.info(f"url formed is {url}")

    entire_data = get_data_from_url(url)
    logging.info(f"data extracted is {entire_data}")

    return entire_data


def get_a_word_to_search():
    sentence = return_word_after_listening()
    logging.info(f"sentence recognized is {sentence}")

    return_list = return_split_of_sentence(sentence)
    logging.info(f" list after splitting of the sentence from the 'of' word and list is {return_list}")
    return return_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # using Speech recognition to get the sentence in desired format
    word_list = get_a_word_to_search()

    # getting the word and sending it for the meaning extraction
    json_response = get_definition_of_the_word(word_list[1])

    # extracting the sound links from the response
    sound_links = get_sound_links_from_response(json_response)

    # getting the meaning of the word from the response.
    meanings_list = get_meanings_from_response(json_response)

    # getting the part of speech to meaning dict
    meaning_dict = get_definitions_with_part_of_speech(meanings_list)

    for key,val in meaning_dict.items():
        print(key, val)
