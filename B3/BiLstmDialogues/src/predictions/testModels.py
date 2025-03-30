import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os

model_path = "../../savedModels/bilstm.h5"
tokenizer_path = "../../savedModels/tokenizer.pkl"

model = tf.keras.models.load_model(model_path)

max_len = 100 
vocab_size = 30000 

with open(tokenizer_path, "rb") as handle:
    tokenizer = pickle.load(handle)

def predict_text(text):
    seq = tokenizer.texts_to_sequences([text])
    padded_seq = pad_sequences(seq, maxlen=max_len, padding='post')
    prediction = model.predict(padded_seq)
    return prediction

example_text = "Hello, how are you ?"
result = predict_text(example_text)
print("Prédiction :", result)

def decode_prediction(prediction):
    predicted_indices = np.argmax(prediction, axis=-1)
    predicted_words = [tokenizer.index_word.get(index, "<UNK>") for index in predicted_indices.flatten()]
    return " ".join(predicted_words)

example_text = "Bonjour, comment vas-tu ?"
result = predict_text(example_text)
decoded_result = decode_prediction(result)

print("Prédiction :", decoded_result)
