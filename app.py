from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.preprocessing.image import array_to_img
import os
import base64
import io
from PIL import Image 
import keras 
from keras import backend as K 
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
import numpy as np
from flask import Flask, jsonify, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html') 

def get_model():
    global model
    model = load_model('/Users/yari/2023/Applicerad_AI/fairfacedata/gender_classes/best_gender_model.h5')

get_model()
def preprocessing_image(image, target_size):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis = 0)
    image = image/ 225.0
    
    return image




@app.route('/predict', methods=['POST'])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocessing_image(image, target_size =(224, 224))

    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction': {
            'Female': prediction[0][0],
            'Male': prediction[0][1]
            # 'Black' : prediction[0][0],
            # 'East_Asian': prediction[0][1],
            # 'Indian': prediction[0][1],
            # 'Latino Hispanic': prediction[0][1],
            # 'Middle Eastern': prediction[0][1],
            # 'Southeast Asian': prediction[0][1],
            # 'White': prediction[0][1],
        }
    }
    return jsonify(response)








if __name__  == "__main__":
    app.run(debug=True, port = 5001)