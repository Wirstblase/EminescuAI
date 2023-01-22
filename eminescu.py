import tensorflow as tf
from tensorflow import keras

import numpy as np
import os
import time

print("program started")

model = keras.models.load_model("eminescu_model_gpu.h5")

path_to_file = "eminescupoezii.txt"

text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
# length of text is the number of characters in it
print('Length of text: {} characters'.format(len(text)))

# Take a look at the first 250 characters in text
#print(text[:250])

# The unique characters in the file
vocab = sorted(set(text))
print('{} unique characters'.format(len(vocab)))

# Creating a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

#model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

#model.build(tf.TensorShape([1, None]))

model.summary()

print("SUCCESSFULLY LOADED TRAINED MODEL FROM FILE: "+path_to_file)

global droguri
droguri = 1.0

global lungime
lungime = 500

def generate_text(model, start_string):
    # Evaluation step (generating text using the learned model)

    # Number of characters to generate
    global lungime
    num_generate = lungime #500

    # Converting our start string to numbers (vectorizing)
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    # Empty string to store our results
    text_generated = []

    # Low temperature results in more predictable text.
    # Higher temperature results in more surprising text.
    global droguri
    temperature = droguri#= 1.0

    # Here batch size == 1
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        # remove the batch dimension
        predictions = tf.squeeze(predictions, 0)

        # using a categorical distribution to predict the character returned by the model
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

        # Pass the predicted character as the next input to the model
        # along with the previous hidden state
        input_eval = tf.expand_dims([predicted_id], 0)

        text_generated.append(idx2char[predicted_id])

    return (start_string + ''.join(text_generated))

#print(generate_text(model, start_string=u" "))

def poezie():
    print(generate_text(model, start_string=" "))

def poeziecustom(word):
    print(generate_text(model, start_string=word))

def poeziiinfinite():
    for i in range(2000):
        print(generate_text(model, start_string=" "))



for i in range(5):
    print("")

'''
inspiratie , eul eminescian , 
'''

def help():
    print("=======================")
    print("Comenzi disponibile:")
    print("poezie() zice o poezie")
    print("poeziecustom(cuvant) zice o poezie custom care incepe cu orice cuvant")
    print("droguri = numar (cuprins intre 0.0 si 2.0, default 1.0)")
    print("lungime = numar (cuprins intre 1 si 200000, default 500)")
    print("help() meniul acesta")
    print("=======================")

help()

