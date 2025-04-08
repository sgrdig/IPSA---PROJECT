import numpy as np
import pandas as pd
import re
import os
from statistics import median
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Paramètres
data_path = "data"
lines_path = os.path.join(data_path, "movie_lines.tsv")
convos_path = os.path.join(data_path, "movie_conversations.tsv")

VOCAB_SIZE = 5000
EMBEDDING_DIM = 500

# Charger les dialogues
df_lines = pd.read_csv(lines_path, encoding='utf-8-sig', header=None)
lines = df_lines[0].str.split('\t')
dialogue_lines = [x[4] for x in lines if len(x) >= 5]

# Tokenisation
keras_tokenizer = Tokenizer(num_words=VOCAB_SIZE, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}\t\n')
keras_tokenizer.fit_on_texts(dialogue_lines)

# Sauvegarder le tokenizer
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(keras_tokenizer, f)

# Créer les séquences de texte
text_sequences = keras_tokenizer.texts_to_sequences(dialogue_lines)[:50000]
MAX_SEQUENCE_LENGTH = int(median(len(seq) for seq in text_sequences))

# Padding
x_train = pad_sequences(text_sequences, maxlen=MAX_SEQUENCE_LENGTH, padding='post', truncating='post', value=0)

# Créer les paires question-réponse
input_texts = x_train[:-1]
target_texts = x_train[1:]

# Sauvegarder les tableaux numpy
np.save("input_texts.npy", input_texts)
np.save("target_texts.npy", target_texts)

# Sauvegarder la longueur maximale
with open("max_seq_len.txt", "w") as f:
    f.write(str(MAX_SEQUENCE_LENGTH))

print("Preprocessing terminé. Tokenizer et données sauvegardées.")