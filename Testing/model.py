import tensorflow as tf
from tensorflow import keras
import numpy as np

class Model():
    def __init__(self):
        self.model = keras.Sequential([
            keras.layers.Input(shape=(128, 128, 3)),  # Input layer with the desired shape
            keras.layers.Conv2D(32, (3, 3), activation='relu'),
            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Conv2D(64, (3, 3), activation='relu'),
            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Flatten(),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(2, activation='sigmoid')
        ])

        # compile the model
        self.model.compile(
            optimizer='adam',
            loss=tf.keras.losses.BinaryCrossentropy(),
            metrics=['accuracy']
        )

        self.cp_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath="checkpoint.keras",
            save_weights_only=True,
            verbose=1
        )

        self.fields = [
            "Garbage",
            "Null"
        ]

    def train(self, X_train, Y_train, X_test, Y_test, epochs=3):
        history=self.model.fit(
            X_train, 
            Y_train, 
            epochs=epochs, 
            validation_data=(X_test, Y_test),
            callbacks=[self.cp_callback]
        )

    def test(self, X_test,Y_test):
        test_loss, test_acc = self.model.evaluate(X_test,Y_test)
        print('Test accuracy:', test_acc) 
    
    def save(self, filename="model.keras"):
        self.model.save(filename)
        # self.model.save_weights(filename)
    
    def load(self, filename="model.keras"):
        self.model = tf.keras.models.load_model(filename)
        # self.model.load_weights(filename)
        self.model.compile(
            optimizer='adam',
            loss=tf.keras.losses.BinaryCrossentropy(),
            metrics=['accuracy']
        )
    
    def predict(self, image):
        data = np.expand_dims(image, axis=0)
        scores = self.model.predict(data)
        scores = scores.tolist()
        scores = scores[0]

        maxScore = 0
        maxNo = 0
        for i in range(len(scores)):
            if scores[i] > maxScore:
                maxScore = scores[i]
                maxNo = i
        prediction = self.fields[maxNo]

        return scores, prediction
    



