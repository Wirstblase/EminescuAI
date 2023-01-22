# EminescuAI
An AI that generates poetry in the style of Mihai Eminescu

Introduction

This program is an eminescian poetry generator that uses a Recurrent Neural Network (RNN) trained on a dataset of poetry written by our famous poet Mihai Eminescu. The program is divided into two parts: the first part is used to train the model and the second part is used to generate new poetry using the trained model.


Data Collection

The training data used in this program is a text file containing a large collection of Eminescu's poetry. The text file is loaded and the unique characters in the file are identified. A mapping is then created from the unique characters to indices, which is later used to vectorize the text data.


Model Training

The program uses Tensorflow and Keras to train the RNN model on the vectorized text data. The model consists of an Embedding layer, a GRU layer, and a Dense layer. The model is trained using a categorical cross-entropy loss function and the Adam optimizer.


The model layers

Embedding layer: This layer is used to convert the vectorized text data into a lower-dimensional embedding space. The embedding space is a mathematical representation of the input data that captures the relationships between the input elements. The embedding layer takes in the vectorized text data and maps it to a dense vector representation, where each element in the vector corresponds to a unique character in the input data. This dense representation is then passed to the next layers in the model.

GRU layer: The GRU (Gated Recurrent Unit) layer is a type of RNN (Recurrent Neural Network) that processes the input data and maintains an internal state that captures dependencies between elements in the input sequence. The GRU layer takes in the dense vector representation from the Embedding layer and processes it in a way that allows the model to maintain an understanding of the context and dependencies between the characters in the input text. Essentially, the GRU layer allows the model to understand the meaning of the input text and maintain a memory of the previous input elements.

Dense layer: The Dense layer is a fully connected layer that makes predictions based on the output from the GRU layer. The Dense layer takes in the output from the GRU layer and applies a set of weights to it, which are learned during training. The output from the Dense layer is then used to make predictions about the next character in the sequence.

In summary, the Embedding layer converts the input data into a dense vector representation, the GRU layer processes the input data and maintains an understanding of the context and dependencies between the characters, and the Dense layer makes predictions based on the output from the GRU layer.


How is the magic done?

The layers in the model, when trained on a large dataset, learn patterns and relationships between the characters in the input data. These patterns and relationships allow the model to understand the structure and style of the input poetry.

When the trained model is used to generate new poetry, it uses the patterns and relationships it learned from the input data to generate new text that is similar in structure and style to the input data.

The Embedding layer converts the input data into a dense vector representation, which captures the relationships between the characters in the input data. The GRU layer, with its ability to maintain an understanding of the context and dependencies between the characters, uses this representation to process the input and generate new text that is similar in style to the input data.

The Dense layer, with the weights learned during the training phase, makes predictions about the next character in the sequence based on the output from the GRU layer. As the model generates new text, it uses the patterns and relationships it learned from the input data to make predictions about the next character in the sequence, resulting in new text that is similar in style to the input data.

It's worth noting that the model will never be able to perfectly recreate the input data, but it can generate new text that is similar in style and structure.


Model Evaluation

The trained model is evaluated by generating new poetry using a random seed and comparing the generated text to the original training data. The generated text is also inspected visually to ensure that it is coherent and semantically meaningful.


Poetry Generation

Once the model is trained and evaluated, it can be used to generate new poetry by providing a seed text as input. The program uses the trained model to generate new text by predicting the next character in the sequence based on the current input and the internal state of the model. The generated text is then concatenated to the seed text to form the final output.


Conclusion and Future Work

The program is able to generate new poetry that is coherent and semantically meaningful. However, the generated poetry is currently limited by the quality and diversity of the training data. In future work, the program could be improved by using a larger and more diverse training dataset, as well as experimenting with different model architectures and parameters.

In the future, this project can be taken to the next level by providing a hardware component: a 3D printed statue of our famous poet with a raspberry pi computer inside, and a little amplifier and a speaker, and a big button on the outside, that when pressed: the program will generate a poem and then it will pass it to another program that uses a text to speech algorithm to generate a sound file which is then played through the speaker, effectively making the Eminescu statue recite new poetry on demand.
