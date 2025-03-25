import re 
from nltk.corpus import stopwords
import nltk
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9' ]", "", text)
    text = re.sub(r"\d+", "<num>", text)
    text = re.sub(r"(\w)'(\w)", r"\1 ' \2", text)
    text = re.sub(r"\s+", " ", text).strip()
    
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    return " ".join(words)


def token(df):
    max_length = 40
    vocab_size = 10000
    tokenizer = Tokenizer(num_words=vocab_size, oov_token="<OOV>")

    tokenizer.fit_on_texts(df['questions'].tolist() + df['reponce'].tolist())

    X = tokenizer.texts_to_sequences(df['questions'].tolist())
    y = tokenizer.texts_to_sequences(df['reponce'].tolist())

    X = pad_sequences(X, maxlen=max_length, padding='post')  
    y = pad_sequences(y, maxlen=max_length, padding='post')