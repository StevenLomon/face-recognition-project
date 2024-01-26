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

# Load your trained model
model_path = r"C:\Users\46722\Downloads\mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5"

def get_model():
    global model
    model = load_model('best_race_model.h5')
    print('*Model loaded*')

def preprocessing_image(image, target_size):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize(taget_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis = 0)
    
    return image

print('*loading keras model...')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if a file is received
    image = request.files['image']
    if image.filename == '':
        return 'No selected file'
    decoded = base64.b64decode(image)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocessing_image(image, target_size =(224, 224))

    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction': {
            'Black' : prediction[0][0],
            'East_Asian': prediction[0][1]
        }
    }
    return jsonify(response)











# @app.route('/', methods=['GET'])
# def index():
#     # Render the main page
#     return render_template('home.html')


# @app.route('/about', methods=['GET'])
# def about():
#     # Render the about page
#     return render_template('about.html')

# @app.route('/contact', methods=['GET'])
# def contact():
#     # Render the contact page
#     return render_template('contact.html')

# @app.route('/upload')
# def upload():
#     return render_template('upload_form.html')


# @app.route('/predict', methods=['POST'])
# def predict():
#     # Check if a file is received
#     file = request.files['file']
#     if file.filename == '':
#         return 'No selected file'





if __name__  == "__main__":
    app.run(debug=True, port = 5001)