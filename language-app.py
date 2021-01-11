import csv
import easygui
import nltk
from nltk import word_tokenize, sent_tokenize

user_input_mode = input('Is the language sample speech(s) or text(t)? ')


def check_input_mode(input_mode):
    if input_mode == 's':
        print('Speech to text is not yet an enabled feature, coming soon!')
        exit()
    elif input_mode != 't':
        print('This is not a recognised input mode, please try again.')
        exit()


check_input_mode(user_input_mode)

text = input('Please enter a sentence or utterance to analyse. ')

sample_sentence_tokens = sent_tokenize(text)
print('Here is the sentence level tokenized language sample: {}'.format(sample_sentence_tokens))

analysed_language_data = []


def prepare_analysed_language_data(sentence_tokens):
    for sentence_token in sentence_tokens:
        word_tokens = word_tokenize(sentence_token)
        parsed_tokens = nltk.pos_tag(word_tokens)

        current_sentence_dictionary = {
            'sentence': sentence_token,
            'parsed_tokens': []
        }

        for parsed_token in parsed_tokens:
            current_parsed_token_dictionary = {
                'token': parsed_token[0],
                'tag': parsed_token[1]
            }

            current_sentence_dictionary['parsed_tokens'].append(current_parsed_token_dictionary)

        # remove the full stops from the parsed tokens list of dictionaries
        current_sentence_dictionary['parsed_tokens'].pop()
        analysed_language_data.append(current_sentence_dictionary)
    return analysed_language_data


parsed_language_data = prepare_analysed_language_data(sample_sentence_tokens)
print(parsed_language_data)

field_names = ['sentence', 'parsed_tokens']

with open('languageAnalysis.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(parsed_language_data)

easygui.msgbox("For interpretation of token tags, please see the table at this site: "
               "https://www.sketchengine.eu/modified-penn-treebank-tagset/", title="What's next")
