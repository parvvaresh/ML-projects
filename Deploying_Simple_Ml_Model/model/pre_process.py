import re
import string
import unicodedata
import contractions
from word2number import w2n
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load stopwords from NLTK
stop_words = set(stopwords.words('english'))

def remove_special_characters(text: str) -> str:
    """Removes URLs, non-ASCII characters, and punctuation."""
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove non-ASCII characters
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    # Remove any remaining non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Remove extra spaces that may have been created
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def case_normalization(text: str) -> str:
    """Converts all characters in the text to lowercase."""
    return text.lower()

def remove_accents_diacritics(text: str) -> str:
    """Removes accents and diacritics from the text."""
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

def expand_contractions(text: str) -> str:
    """Expands common contractions in the text."""
    return contractions.fix(text)

def normalize_numbers_and_units(text: str) -> str:
    """Normalizes numbers and units in the text."""
    text = re.sub(r'\bkm\b', 'kilometres', text)
    text = re.sub(r'\bapprox\.\b', 'approximately', text)
    text = re.sub(r'\bcm\b', 'centimetres', text)
    text = re.sub(r'\bkg\b', 'kilograms', text)
    text = re.sub(r'\blbs\b', 'pounds', text)
    text = re.sub(r'\bmm\b', 'millimetres', text)
    text = re.sub(r'\bml\b', 'millilitres', text)
    text = re.sub(r'\bl\b', 'litres', text)
    text = re.sub(r'\bsec\b', 'seconds', text)
    text = re.sub(r'\bmin\b', 'minutes', text)
    text = re.sub(r'\bhr\b', 'hours', text)
    text = re.sub(r'\bhrs\b', 'hours', text)
    text = re.sub(r'\bft\b', 'feet', text)
    text = re.sub(r'\bmph\b', 'miles per hour', text)
    text = re.sub(r'\bkph\b', 'kilometres per hour', text)
    text = re.sub(r'\bm\s\b', 'metres per second', text)

    tokens = text.split()
    normalized_tokens = []

    for token in tokens:
        try:
            normalized_tokens.append(str(w2n.word_to_num(token)) if token.isdigit() else token)
        except ValueError:
            normalized_tokens.append(token)

    return ' '.join(normalized_tokens)

def tokenize_text(text: str) -> list:
    """Tokenizes the text into individual words."""
    return word_tokenize(text)

def lemmatize_tokens(tokens: list) -> list:
    """Lemmatizes each token (word) in the tokenized list."""
    return [lemmatizer.lemmatize(token) for token in tokens]

def remove_stopwords(tokens: list) -> list:
    """Removes stopwords from the tokenized list of words."""
    return [token for token in tokens if token not in stop_words]

def remove_punctuation_tokens(tokens: list) -> list:
    """Removes punctuation from tokenized words."""
    return [token for token in tokens if token not in string.punctuation]

def pre_process(text: str) -> list:
    """Normalizes the text through all the processing steps."""
    text = case_normalization(text)
    text = remove_accents_diacritics(text)
    text = expand_contractions(text)
    text = normalize_numbers_and_units(text)
    
    # Tokenize the text 
    tokens = tokenize_text(text)
    
    # Remove stopwords from the tokenized list
    tokens = remove_stopwords(tokens)

    # Remove punctuation tokens
    tokentrain_save_models = remove_punctuation_tokens(tokens)

    # Lemmatize the tokens
    lemmatized_tokens = lemmatize_tokens(tokentrain_save_models)
    
    # Return the pre-processed tokens
    return lemmatized_tokens    