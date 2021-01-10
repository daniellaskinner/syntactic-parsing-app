import nltk
from nltk import ne_chunk, word_tokenize, sent_tokenize

# read from a text file a language sample
text = input('Please enter a sentence or utterance to analyse. ')

# tokenize the sample by sentence and word level
sentence_tokens = sent_tokenize(text)
print('Here is the sentence level tokenized language sample: {}'.format(sentence_tokens))

word_tokens = word_tokenize(text)
tagged_utterance = nltk.pos_tag(word_tokens)
print('Here is the word level tokenized and parsed language sample: {}'.format(tagged_utterance))

print('Here we can see chunking:')
chunks = ne_chunk(tagged_utterance)
print(chunks)
print(chunks.__repr__())


# for each of the sentence_tokens in array display in a csv text file

# display in a csv file for each of the word tokens in tagged_utterance with the tag code
