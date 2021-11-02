from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# import spacy
# import spacy_spanish_lemmatizer
import pickle
import numpy as np
import tensorflow as tf
import json
import random


def clean_message(text):
    """Pre-process a message

    Parameters
    ----------
    text : str
        input text
    """

    # stop_words = set(stopwords.words('spanish'))
    text = text.lower() # lowercase all
    # replace the spanish accents
    text = text.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú', 'u')
    
    tokens = word_tokenize(text) 
    
    tokens = [word for word in tokens if word.isalpha()] #remove the punctuation signs
    # tokens = [w for w in tokens if not w in stop_words]
    # text = ' '.join(tokens)

    return tokens

def bow(sentence, words_path, show_details = True):
    words = pickle.load(open(words_path,'rb'))
    sentence_words = clean_message(sentence)
    bag = [0]*len(words)

    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print(f"found in bag: {w}")
    
    return np.array(bag)

def predict_class(sentence, model):
    classes = pickle.load(open('classes.pkl','rb'))
    p = bow(sentence, 'words.pkl', show_details = False)
    p = np.expand_dims(p,axis = 0)
    y_pred = model.predict(np.array(p))[0]

    threshold = 0.55

    results = [[i,r] for i,r in enumerate(y_pred) if r>threshold]
    results.sort(key = lambda x: x[1], reverse = True)
    return_list = []

    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    print(return_list)
    return return_list


def get_response(ints, intents_json):
    if len(ints) == 0:
        tag = 'defaults'
        list_of_intents = intents_json['intents']
    
        for i in list_of_intents:
            if(i['tag'] == tag):
                result = random.choice(i['responses'])
                break
        
    else:
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        
        for i in list_of_intents:
            if(i['tag'] == tag):
                result = random.choice(i['responses'])
                break
    
    return result


def chat_response(message, model, intents):
    ints = predict_class(message, model)
    pred = get_response(ints, intents)
    return pred