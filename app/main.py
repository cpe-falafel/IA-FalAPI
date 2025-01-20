import os
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from huggingface_hub import hf_hub_download
from PIL import Image
import numpy as np

app = Flask(__name__)

MODEL_REPO = "Nogellex/IA-FalAPI"
MODEL_FILENAME = "cnn_gore_model.h5"

MODEL_PATH = hf_hub_download(repo_id=MODEL_REPO, filename=MODEL_FILENAME)
model = load_model(MODEL_PATH, compile=False)

def preprocess_image(image_path):
    img = load_img(image_path, target_size=(256, 256))
    img_array = img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.route('/eval', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'Aucune image reçue'}), 400

    image = request.files['image']
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    image_path = f"{temp_dir}/{image.filename}"
    image.save(image_path)

    try:
        with Image.open(image_path) as img:
            width, height = img.size
            if width != 256 or height != 256:
                if os.path.exists(image_path):
                    os.remove(image_path)
                return jsonify({'error': 'Les dimensions de l\'image doivent être de 256x256 pixels'}), 400
    except Exception as e:
        if os.path.exists(image_path):
            os.remove(image_path)
        return jsonify({'error': f'Erreur lors de la lecture de l\'image : {str(e)}'}), 400

    processed_image = preprocess_image(image_path)
    prediction = model.predict(processed_image)[0][0] * 100

    if os.path.exists(image_path):
        os.remove(image_path)

    return jsonify({'gore_score': round(float(prediction), 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
