vocabulary_dictionary = {"how": 0, "much": 1, "wood": 2, "would": 3, "a": 4, "woodchuck": 5, "chuck": 6, "if": 7, "could": 8}

new_text = "Would a woodchuck chuck much wood if a woodchuck could?"

the_vector = [0, 0, 0, 1, 2, 2, 1, 1, 1]

same_as_the_vector = convert_text_to_vector(new_text)

print(the_vector == same_as_the_vector)

# True

For vectorization, you can use `CountVectorizer` from the machine learning library `scikit-learn`. You can use `fit()` to train the features dictionary and then `transform()` to transform text into a vector:




training_documents = ["Five fantastic fish flew off to find faraway functions.", "Maybe find another five fantastic fish?", "Find my fish with a function please!"]
test_text = ["Another five fish find another faraway fish."]
bow_vectorizer = CountVectorizer()
bow_vectorizer.fit(training_documents)
bow_vector = bow_vectorizer.transform(test_text)
print(bow_vector.toarray())
# [[2 0 1 1 2 1 0 0 0 0 0 0 0 0 0]]


`fit_transform()` does two things: creations of the features dictionary and the vectorization of the training data.

```python
# Import CountVectorizer from sklearn:
from sklearn.feature_extraction.text import CountVectorizer

# Define bow_vectorizer:
bow_vectorizer = CountVectorizer()

# Define training_vectors:
training_vectors = bow_vectorizer.fit_transform(training_docs)
# Define test_vectors:
test_vectors = bow_vectorizer.transform(test_docs)
```
