from django.shortcuts import render
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from .forms import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html', {
        "ScanTextForm": ScanTextForm()
    })


def scan_text(request):
    loss = 0
    accuracy = 0
    prediction = ""
    if request.method == "POST":
        form = ScanTextForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form_file = form.cleaned_data['image']
            #inblut dataset for text recognition
            mnist = tf.keras.datasets.mnist
            (x_train, y_train), (x_test, y_test) = mnist.load_data()

            x_train = tf.keras.utils.normalize(x_train, axis=1)
            x_test = tf.keras.utils.normalize(x_test, axis=1)

            ## creating model (neural network)
            model = tf.keras.models.Sequential()
            model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
            model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
            model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
            model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

            ## compiling the model
            model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

            model.fit(x_train, y_train, epochs=2)

            ##assigning loss and accuracy percentage
            loss, accuracy = model.evaluate(x_test, y_test)
            form.save()

            ##reading uploaded image
            img = cv.imread(f'./scanned_images/{form_file}')
            for i in range(1,2):
                img = np.invert(np.asarray([img]))
            ##predicting what letter of the image could be 
                pred = model.predict(img)
                prediction = np.argmax(pred)
                print("=============== prediction: ", prediction)

            ##saving uploaded image
        else:
            messages.error(request, 'invalid data entry')

    else:
        form = ScanTextForm()

    return render(request, "scaned-text.html", {
        "loss": loss,
        "accuracy": accuracy,
        "form": form,
        "prediction": prediction
    })