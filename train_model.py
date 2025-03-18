import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint

# Load and preprocess data
file_path = "blue_castle.txt"
with open(file_path, "r", encoding="utf8") as file:
    data = file.read()

data = data.replace('\n', ' ').replace('\r', ' ').replace('\ufeff', ' ').replace('“', '').replace('”', '')
data = ' '.join(data.split())

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
sequence_data = tokenizer.texts_to_sequences([data])[0]

# Save tokenizer
pickle.dump(tokenizer, open('token.pkl', 'wb'))

# Generate sequences
sequences = []
for i in range(3, len(sequence_data)):
    words = sequence_data[i-3:i+1]
    sequences.append(words)
sequences = np.array(sequences)

X, y = sequences[:, :-1], sequences[:, -1]
y = to_categorical(y, num_classes=len(tokenizer.word_index) + 1)

# Model creation
model = Sequential([
    Input(shape=(3,)),
    Embedding(len(tokenizer.word_index) + 1, 10),
    LSTM(1000, return_sequences=True),
    LSTM(1000),
    Dense(1000, activation="relu"),
    Dense(len(tokenizer.word_index) + 1, activation="softmax")
])

model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=0.001))

# Model training
checkpoint = ModelCheckpoint("next_word.keras", monitor='loss', verbose=1, save_best_only=True)
model.fit(X, y, epochs=20, batch_size=64, callbacks=[checkpoint])

print("Model training complete! Model saved as 'next_word.keras'")
