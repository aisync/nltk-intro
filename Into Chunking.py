# The regular expression you build to find chunks is called chunk grammar. A piece of chunk grammar can be written as follows:

chunk_grammar = "AN: {<JJ><NN>}"
# AN is a user-defined name for the kind of chunk you are searching for. You can use whatever name makes sense given your chunk grammar. In this case AN stands for adjective-noun
# A pair of curly braces {} surround the actual chunk grammar
# <JJ> operates similarly to a regex character class, matching any adjective
# <NN> matches any noun, singular or plural
# The chunk grammar above will thus match any adjective that is followed by a noun.

To use the chunk grammar defined, you must create a nltk RegexpParser object and give it a piece of chunk grammar as an argument.

chunk_parser = RegexpParser(chunk_grammar)
You can then use the RegexpParser object’s .parse() method, which takes a list of part-of-speech tagged words as an argument, and identifies where such chunks occur in the sentence!

Consider the part-of-speech tagged sentence below:

pos_tagged_sentence = [('where', 'WRB'), ('is', 'VBZ'), ('the', 'DT'), ('emerald', 'JJ'), ('city', 'NN'), ('?', '.')]
You can chunk the sentence to find any adjectives followed by a noun with the following:

chunked = chunk_parser.parse(pos_tagged_sentence)

from nltk import RegexpParser, Tree
from pos_tagged_oz import pos_tagged_oz

# define adjective-noun chunk grammar here
chunk_grammar = "AN: {<JJ><NN>}"

# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)

# chunk the pos-tagged sentence at index 282 in pos_tagged_oz here
scaredy_cat = chunk_parser.parse(pos_tagged_oz[282])
print(scaredy_cat)

# pretty_print the chunked sentence here
Tree.fromstring(str(scaredy_cat)).pretty_print()
