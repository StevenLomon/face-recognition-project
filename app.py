from flask import Flask, request, render_template, jsonify
import base64
import io
from PIL import Image 
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html') 

def get_model(model_choice) ->object:
    if model_choice == 'gender':
        model = load_model('/Users/yari/2023/Applicerad_AI/fairfacedata/gender_classes/best_gender_model.h5')
    if model_choice == 'age':
        model = load_model('/Users/yari/2023/Applicerad_AI/fairfacedata/age_classes/best_age_model.h5')
    if model_choice == 'race':
        model = load_model('/Users/yari/2023/Applicerad_AI/fairfacedata/race_classes/race_model.h5')
    return model

def preprocessing_image(image, target_size):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis = 0)
    image = image/ 225.0
    
    return image

def get_target_size(model_choice) -> str:
    if model_choice == 'gender':
        target_size = (224, 224)
    else:
        target_size = (128, 128)
    return target_size
    



@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        model_choice = data.get('type')
        encoded_image = data.get('image')
        model = get_model(model_choice)
        if model is None:
            return jsonify({'error': 'Model could not be loaded'}), 500
        decoded = base64.b64decode(encoded_image)
        image = Image.open(io.BytesIO(decoded))
        target_size = get_target_size(model_choice= model_choice)
        processed_image = preprocessing_image(image, target_size)

        prediction = model.predict(processed_image).tolist()
    
        if model_choice == 'gender':
            response = {
                'prediction': {
                    'Female': prediction[0][0],
                    'Male': prediction[0][1]
                }
            }
        elif model_choice == 'race':
            response = {
                'prediction': {
                    'Black' : prediction[0][0],
                    'East_Asian': prediction[0][1],
                    'Indian': prediction[0][2],
                    'Latino Hispanic': prediction[0][3],
                    'Middle Eastern': prediction[0][4],
                    'Southeast Asian': prediction[0][5],
                    'White': prediction[0][6],
                }
            }
        elif model_choice == 'age':
            response = {
                'prediction': {
                    '20-29' : prediction[0][0],
                    '30-39': prediction[0][1],
                    '40-49': prediction[0][2],
                    '50-59': prediction[0][3],
                    '60-69': prediction[0][4],
                }
            }
        else:
            raise ValueError('No response please check if your model choice')
            
        return jsonify(response)
    except Exception as e:
        print(f'Failed to load model{e}')







if __name__  == "__main__":
    app.run(debug=True, port = 5001)