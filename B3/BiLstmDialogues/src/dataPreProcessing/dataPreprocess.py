import re 
from nltk.corpus import stopwords
import nltk


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