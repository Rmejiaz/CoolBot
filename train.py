import nltk
import json
import pickle
import numpy as np

import tensorflow as tf
from utils import clean_message
import random


words = []
classes = []
documents = []

data_file = open('intents.json').read()
intents = json.loads(data_file)


for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = clean_message(pattern)
        words.extend(w)
        documents.append((w,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


classes = sorted(list(set(classes)))

print(len(classes), "classes", classes)

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []

output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Input(shape = len(train_x[0])))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dropout(0.6))
model.add(tf.keras.layers.Dense(64, activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.6))
model.add(tf.keras.layers.Dense(len(train_y[0]), activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer=tf.keras.optimizers.SGD(learning_rate=0.01, decay = 1e-6, momentum=0.9, nesterov = True), metrics = ['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs = 20, batch_size = 32, verbose = 1)

model.save('model1.h5')