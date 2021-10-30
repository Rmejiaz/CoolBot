from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def clean_message(text):
    """Pre-process a message

    Parameters
    ----------
    text : str
        input text
    """
    text = text.lower() # lowercase all
    # replace the spanish accents
    text = text.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú', 'u')
    
    tokens = word_tokenize(text) 
    
    tokens = [word for word in tokens if word.isalpha()] #remove the punctuation signs
    
    text = ' '.join(tokens)

    return text