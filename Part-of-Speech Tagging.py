# Wow! Ramona and her class are happily studying the new textbook she has on NLP.
#
# Noun: the name of a person (Ramona,class), place, thing (textbook), or idea (NLP)
# Pronoun: a word used in place of a noun (her,she)
# Determiner: a word that introduces, or “determines”, a noun (the)
# Verb: expresses action (studying) or being (are,has)
# Adjective: modifies or describes a noun or pronoun (new)
# Adverb: modifies or describes a verb, an adjective, or another adverb (happily)
# Preposition: a word placed before a noun or pronoun to form a phrase modifying another word in the sentence (on)
# Conjunction: a word that joins words, phrases, or clauses (and)
# Interjection: a word used to express emotion (Wow)
import nltk
from nltk import pos_tag
from word_tokenized_oz import word_tokenized_oz

# save and print the sentence stored at index 100 in word_tokenized_oz here
witches_fate = word_tokenized_oz[100]
print(witches_fate)


# create a list to hold part-of-speech tagged sentences here
pos_tagged_oz = []

# create a for loop through each word tokenized sentence in word_tokenized_oz here
for token in word_tokenized_oz:
  pos_tagged_oz.append(pos_tag(token))
  # part-of-speech tag each sentence and append to pos_tagged_oz here
witches_fate_pos = pos_tagged_oz[100]

# store and print the 101st part-of-speech tagged sentence here
print(witches_fate_pos)
