import json
import difflib
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input('Did you mean %s instead? ' % get_close_matches(word, data.keys())[0])
        if yn == 'Y' or yn == 'y':
            first_data_match = get_close_matches(word, data.keys())[0]
            return data[first_data_match]
        elif yn == 'N' or yn =='n':
            return 'That word doesn\'t exist!'
        else:
            return 'Entry not understood.'
    else:
        if word == 'q' or word == 'Q':
            return 'Goodbye!'
        else:
            return 'That word doesn\'t exist!'

while True:
    word = input('Enter word (or enter \'q\' to quit): ')

    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    if word == 'q' or word == 'Q':
        break

