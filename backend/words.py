from http import HTTPStatus
from http.client import OK
import re
import requests

apiUrl = 'http://api.wordnik.com/v4'
acceptedPartsOfSpeech = [
    'adjective',
    'adverb',
    'noun',
    'preposition',
    'verb'
]


class Words:
    bold = re.compile(r'\*\*(.+?)\*\*')
    italic = re.compile(r'\*(.+?)\*')

    def __init__(self, key=None):
        self.api_key = key


    def get_words(self):
        if not self.api_key:
            raise ValueError("No API key provided.")
        params = {
            'api_key': self.api_key,
            'hasDictionaryDef': True,
            'minLength': 4,
            'maxLength': 20,
            'minDictionaryCount': 3,
            'includePartOfSpeech': ','.join(acceptedPartsOfSpeech),
            'limit': 10
        }
        
        try:
            r = requests.get(f'{apiUrl}/words.json/randomWords', params=params)
            r.raise_for_status()
        except requests.HTTPError as e:
            if e.response.status_code == 401:
                raise ValueError("Invalid API key provided.") 
        words = [d.get('word') for d in r.json()]

        return words


    def get_def(self, word):
        params = {
            'api_key': self.api_key,
            'useCanonical': True,
            'limit': 1,
            'sourceDictionaries': 'ahd-5,webster,wordnet'
        }
        try:
            r = requests.get(f'{apiUrl}/word.json/{word}/definitions', params=params)
            if r.status_code == HTTPStatus.NOT_FOUND:
                return None

            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return err

        word_def = r.json()[0].get("text")

        res = self.format_def(word_def)

        return res


    def format_def(self, word_def):
        if not word_def:
            return None
        #There's surely a better way here, but this 'works'
        if type(word_def) == list:
            word_def = word_def[0]
        bolds = self.bold.findall(word_def)
        for entry in bolds:
            word_def = self.bold.sub(repl='<b>\\1</b>', string=word_def, count=1)
        italics = self.italic.findall(word_def)            
        for entry in italics:
            word_def = self.italic.sub('<i>\\1</i>', string=word_def, count=1)

        return word_def
