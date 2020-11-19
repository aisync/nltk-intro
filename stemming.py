# First, you must import and initialize the stemmer:
#
# from nltk.stem import PorterStemmer
# stemmer = PorterStemmer()
# Now that we have our stemmer, we can apply it to each word in a list using a list comprehension:
#
# tokenized = ['NBC', 'was', 'founded', 'in', '1926', '.', 'This', 'makes', 'NBC', 'the', 'oldest', 'major', 'broadcast', 'network', '.']
#
# stemmed = [stemmer.stem(token) for token in tokenized]
#
# print(stemmed)
# # ['nbc', 'wa', 'found', 'in', '1926', '.', 'thi', 'make', 'nbc', 'the', 'oldest', 'major', 'broadcast', 'network', '.']



from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
populated_island = 'Java is an Indonesian island in the Pacific Ocean. It is the most populated island in the world, with over 140 million people.'

stemmer = PorterStemmer()
island_tokenized = word_tokenize(populated_island)
stemmed = [stemmer.stem(token) for token in island_tokenized]






try:
  print('A stemmer exists:')
  print(stemmer)
except:
  print('Expected a variable called `stemmer`')
try:
  print('Words Tokenized:')
  print(island_tokenized)
except:
  print('Expected a variable called `island_tokenized`')
try:
  print('Stemmed Words:')
  print(stemmed)
except:
  print('Expected a variable called `stemmed`')
