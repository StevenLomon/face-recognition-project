from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from flask_migrate import Migrate, upgrade

app = Flask(__name__)

# Load your trained model
model_path = r"C:\Users\46722\Downloads\mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5"

@app.route('/', methods=['GET'])
def index():
    # Render the main page
    return render_template('test.html')


@app.route('/about', methods=['GET'])
def about():
    # Render the about page
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    # Render the contact page
    return render_template('contact.html')

@app.route('/upload')
def upload():
    return render_template('upload_form.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Check if a file is received
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        # Preprocess the file here
        img = image.load_img(file, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        # Make prediction
        prediction = model.predict(img)

        # You'll need to translate the prediction to your desired output
        # For example, converting numerical prediction to labels

        # Format the response
        age, gender, race = parse_prediction(prediction)

        return render_template('result.html', age=age, gender=gender, race=race)

if __name__ == '__main__':
    app.run(debug=True)



if __name__  == "__main__":
    with app.app_context():
        upgrade()
