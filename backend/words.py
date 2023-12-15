from http import HTTPStatus
from http.client import OK
import re
import requests

apiUrl = 'http://api.wordnik.com/v4'
excludedPartsOfSpeech = [
    'pronoun',
    'abbreviation',
    'affix',
    'family-name',
    'given-name',
    'idiom',
    'noun-posessive',
    'proper-noun',
    'proper-noun-plural',
    'suffix'
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
            'excludePartOfSpeech': ','.join(excludedPartsOfSpeech),
            'limit': 20,
            'minCorpusCount': 20
        }
        
        try:
            r = requests.get(f'{apiUrl}/words.json/randomWords', params=params)
            r.raise_for_status()
        except requests.HTTPError as e:
            if e.response.status_code == 401:
                raise ValueError("Invalid API key provided.") 

        results = [d.get('word') for d in r.json()]

        words = [w for w in results if not any(e.isupper() or e.isspace() for e in w)]

        return words

    def get_def(self, word):
        params = {
            'api_key': self.api_key,
            'useCanonical': True,
        }
        try:
            r = requests.get(f'{apiUrl}/word.json/{word}/definitions', params=params)
            if r.status_code == HTTPStatus.NOT_FOUND:
                return "IDK, Doom(tm) or something"

            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return f"Error {r.status_code}"

        defs = r.json()
        word_def = None
        for d in defs:
            word_def = d.get("text")
            if word_def:
                break

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
