from django.shortcuts import render
import os
import numpy as np
import keras
from keras.preprocessing import image
from django.core.files.storage import FileSystemStorage
from django.conf import settings

BASE = os.path.dirname(os.path.abspath(__file__))

# our home page view
def home(request):
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(image):

    model = keras.models.load_model(os.path.join(BASE, 'cnn_xray_model.h5'))
    prediction = model.predict_classes(image)

    if prediction[0] == 0:
        return "Normal"
    elif prediction[0] == 1:
        return "Covid"
    elif prediction[0] == 2:
        return "Pneumonia"
    else:
        return "error"


# our result page view
def result(request):
    if request.method == 'POST' and request.FILES['xray_image']:
        post = request.method == 'POST'

        myfile = request.FILES['xray_image']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)

        base_dir = settings.MEDIA_ROOT

        size = 100;
        img = image.load_img(os.path.join(base_dir, str(myfile)), target_size=(size, size), color_mode="grayscale")
        img = np.array(img)
        img = img / 255.0
        img = img.reshape(-1, size, size, 1)

        result = getPredictions(img)

        return render(request, 'result.html', {'result': result})