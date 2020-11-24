import speech_recognition as sr


import logging
logging.basicConfig(level=logging.DEBUG)


def return_word_after_listening():
    # it will return the entire sentence
    logging.info("creating a speech recognizer")
    r = sr.Recognizer()
    mic = sr.Microphone()

    print("Ask for word meaning")
    logging.info("Prompting user to ask in particular format")
    with mic as source:
        audio = r.listen(source)

    logging.info("recognizing the sentence recognizer")
    word_spoken = r.recognize_google(audio)

    logging.info("returning the spoken sentence")
    return word_spoken


def return_split_of_sentence(sentence):
    logging.info(f"sentence passed is {sentence}")
    logging.info("splitting from the of word")
    return sentence.split('of')
