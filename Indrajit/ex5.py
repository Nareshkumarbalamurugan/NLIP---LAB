from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
texts = [
    "I love this product",
    "This is a great movie",
    "I hate this product",
    "This movie is terrible"
]

labels = ["Positive", "Positive", "Negative", "Negative"]

# Convert text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X, labels)

# Test sentence
test_sentence = ["I love this movie"]

# Convert test sentence into vector
test_vector = vectorizer.transform(test_sentence)

# Predict class
prediction = model.predict(test_vector)

print("Sentence:", test_sentence[0])
print("Predicted Class:", prediction[0])