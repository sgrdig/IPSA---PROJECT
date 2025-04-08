import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os
from tensorflow.keras.models import load_model

MAX_SEQUENCE_LENGTH = 40 

model_path = "../../savedModels/bilstm.h5"
tokenizer_path = "../../savedModels/tokenizer.pkl"

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)


model = load_model("chat_model.h5")

def generate_response(input_text):
    sequence = tokenizer.texts_to_sequences([input_text])
    padded = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH, padding='post', truncating='post')
    prediction = model.predict(padded)
    predicted_seq = np.argmax(prediction, axis=-1)[0]
    response_words = [word for idx in predicted_seq if idx != 0 for word, i in tokenizer.word_index.items() if i == idx]
    return ' '.join(response_words)

print("Chatbot prêt. Tape 'quit' pour sortir.")
while True:
    user_input = input("Vous: ")
    if user_input.lower() == 'quit':
        break
    response = generate_response(user_input)
    print("Bot:", response)