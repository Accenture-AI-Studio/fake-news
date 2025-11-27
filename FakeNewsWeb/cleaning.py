import re
import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# clean text function
def full_clean_text(text):
    if not isinstance(text, str):
        return ""

    # remove anything before "(Reuters) - "
    text = re.sub(r"^.*?(?:\(Reuters\)|Reuters)\s*-\s*", "", text, flags=re.IGNORECASE)

    # fix encoding artifacts
    try:
        text = text.encode('latin1').decode('utf-8')
    except:
        pass

    # remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)

    # remove month names and numbers
    text = re.sub(
    r'\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|'
    r'january|february|march|april|may|june|july|august|september|october|november|december)\b\.?',
    '',
    text,
    flags=re.IGNORECASE
    )
    text = re.sub(r'\d+', '', text)


    # remove stopwords
    words = text.split()
    words = [w for w in words if w.lower() not in stop_words]
    text = " ".join(words)

    # remove weird symbols
    text = re.sub(r'[^a-zA-Z0-9\s.,!?\'"-]', ' ', text)

    # get rid of multiple whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text