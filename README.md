# Speech_Recognized_Dictionary
A speech recognized dictionary

It uses basic speech recognition to take input in particular format,
then extract the word from that sentence and then pass that word to form a Url to hit google dictionary API to get the information related to the word.

The response part consist for the links to speech and the meaning of the word with part of speech, definition and example.

## Respose message example:

[{'word': 'convey', 
  'phonetics': [{'text': '/kənˈveɪ/', 'audio': 'https://lex-audio.useremarkable.com/mp3/xconvey_us_1.mp3'}],
  'meanings': [{'partOfSpeech': 'transitive verb', 'definitions': [{'definition': 'Transport or carry to a place.', 'example': 'pipes were laid to convey water to the house', 'synonyms': ['transport', 'carry', 'bring', 'take', 'fetch', 'bear', 'move', 'ferry', 'shuttle', 'shift', 'transfer']
  }]}]}]
  
## Working Log of the project:

INFO:root:creating a speech recognizer
Ask for word meaning
INFO:root:Prompting user to ask in particular format
INFO:root:recognizing the sentence recognizer
INFO:root:returning the spoken sentence
INFO:root:sentence recognized is meaning of convey
INFO:root:sentence passed is meaning of convey
INFO:root:splitting from the of word
INFO:root: list after splitting of the sentence from the 'of' word and list is ['meaning ', ' convey']
INFO:root:word recognized is  convey
INFO:root:language code en and word convey is passed
INFO:root:url created is https://api.dictionaryapi.dev/api/v2/entries/en/convey
INFO:root:url formed is https://api.dictionaryapi.dev/api/v2/entries/en/convey
INFO:root:url passed is https://api.dictionaryapi.dev/api/v2/entries/en/convey
transitive verb [{'definition': 'Transport or carry to a place.', 'example': 'pipes were laid to convey water to the house', 'synonyms': ['transport', 'carry', 'bring', 'take', 'fetch', 'bear', 'move', 'ferry', 'shuttle', 'shift', 'transfer']}]
INFO:root:data in json form [{'word': 'convey', 'phonetics': [{'text': '/kənˈveɪ/', 'audio': 'https://lex-audio.useremarkable.com/mp3/xconvey_us_1.mp3'}], 'meanings': [{'partOfSpeech': 'transitive verb', 'definitions': [{'definition': 'Transport or carry to a place.', 'example': 'pipes were laid to convey water to the house', 'synonyms': ['transport', 'carry', 'bring', 'take', 'fetch', 'bear', 'move', 'ferry', 'shuttle', 'shift', 'transfer']}]}]}]
INFO:root:data extracted is [{'word': 'convey', 'phonetics': [{'text': '/kənˈveɪ/', 'audio': 'https://lex-audio.useremarkable.com/mp3/xconvey_us_1.mp3'}], 'meanings': [{'partOfSpeech': 'transitive verb', 'definitions': [{'definition': 'Transport or carry to a place.', 'example': 'pipes were laid to convey water to the house', 'synonyms': ['transport', 'carry', 'bring', 'take', 'fetch', 'bear', 'move', 'ferry', 'shuttle', 'shift', 'transfer']}]}]}]
INFO:root:json data passed [{'word': 'convey', 'phonetics': [{'text': '/kənˈveɪ/', 'audio': 'https://lex-audio.useremarkable.com/mp3/xconvey_us_1.mp3'}], 'meanings': [{'partOfSpeech': 'transitive verb', 'definitions': [{'definition': 'Transport or carry to a place.', 'example': 'pipes were laid to convey water to the house', 'synonyms': ['transport', 'carry', 'bring', 'take', 'fetch', 'bear', 'move', 'ferry', 'shuttle', 'shift', 'transfer']}]}]}]
INFO:root: audio item extracted https://lex-audio.useremarkable.com/mp3/xconvey_us_1.mp3
INFO:root:Extracting meaning from json data
INFO:root:meaning list passed [{'partOfSpeech': 'transitive verb', 'definitions': [{'definition': 'Transport or carry to a place.', 'example': 'pipes were laid to convey water to the house', 'synonyms': ['transport', 'carry', 'bring', 'take', 'fetch', 'bear', 'move', 'ferry', 'shuttle', 'shift', 'transfer']}]}]
INFO:root:definition dict created is {'transitive verb': [{'definition': 'Transport or carry to a place.', 'example': 'pipes were laid to convey water to the house', 'synonyms': ['transport', 'carry', 'bring', 'take', 'fetch', 'bear', 'move', 'ferry', 'shuttle', 'shift', 'transfer']}]}

# *Happy to see additions to this.*
