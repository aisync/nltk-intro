# Chunking Verb Phrases
# Another popular type of chunking is VP-chunking, or verb phrase chunking. A verb phrase is a phrase that contains a verb and its complements, objects, or modifiers.
#
# Verb phrases can take a variety of structures, and here you will consider two. The first structure begins with a verb VB of any tense, followed by a noun phrase, and ends with an optional adverb RB of any form. The second structure switches the order of the verb and the noun phrase, but also ends with an optional adverb.
#
# Both structures are considered because verb phrases of each form are essentially the same in meaning. For example, consider the part-of-speech tagged verb phrases given below:

(('said', 'VBD'), ('the', 'DT'), ('cowardly', 'JJ'), ('lion', 'NN'))
('the', 'DT'), ('cowardly', 'JJ'), ('lion', 'NN')), (('said', 'VBD'),
# The chunk grammar to find the first form of verb phrase is given below:
chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"

# VP is the user-defined name of the chunk you are searching for. In this case VP stands for verb phrase
#
# <VB.*> matches any verb using the . as a wildcard and the * quantifier to match 0 or more occurrences of any character. This ensures matching verbs of any tense (ex. VB for present tense, VBD for past tense, or VBN for past participle)
#
# <DT>?<JJ>*<NN> matches any noun phrase
#
# <RB.?> matches any adverb using the . as a wildcard and the optional quantifier to match 0 or 1 occurrence of any character. This ensures matching any form of adverb (regular RB, comparative RBR, or superlative RBS)

# ? is an optional quantifier, matching either 0 or 1 adverbs

# The chunk grammar for the second form of verb phrase is given below:

chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"
# Just like with NP-chunks, you can find all the VP-chunks in a text and perform a frequency analysis to identify important, recurring verb phrases. These verb phrases can give insight into what kind of action different characters take or how the actions that characters take are described by the author.
