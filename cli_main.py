import numpy as np
import time
from utils import chat_response
import logging
import tensorflow as tf
logging.getLogger("tensorflow").setLevel(logging.WARNING)
import json
import os
import matplotlib.pyplot as plt



model = tf.keras.models.load_model('model1.h5')
intents = json.loads(open('intents.json').read())

info = """
*****************************************************************
|               Bienvenido a CoolBot!                           |       
|                                                               |   
|   Creado por Rafael Mejía Zuluaga y Santiago Buitrago Osorio  |   
|                                                               |   
|           Escribe 'salir' para cerrar el programa.            |   
*****************************************************************
"""
print(info)

while(True):
    user_message = input("You: ") 
    if user_message == 'salir':
        break
    bot_message = chat_response(user_message, model, intents)
    time.sleep(0.5)
    if bot_message[-3:] != 'png':
        print("CoolBot: ", bot_message)
    else:
        bot_message = bot_message[1:]
        plt.imshow(plt.imread(bot_message))
        plt.axis('off')
        plt.show()

