from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
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

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html') 

def get_model():
    global model
    model = load_model('/Users/yari/2023/Applicerad_AI/Classification project/face-recognition-project/models/best_race_model.h5')
    print('*Model loaded*')
get_model()
def preprocessing_image(image, target_size):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis = 0)
    
    return image

print('*loading keras model...')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocessing_image(image, target_size =(128, 128))

    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction': {
            'Black' : prediction[0][0],
            'East_Asian': prediction[0][1]
        }
    }
    return jsonify(response)







if __name__  == "__main__":
    app.run(debug=True, port = 5001)