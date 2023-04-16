from flask import Flask, render_template, url_for, request
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np

#class of tumor
class_names = ["glioma", "meningioma", "no-tumor", "pituitary"]
#load the trained model
model = load_model("./assets/brain_tumor_model_1.h5")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():        
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    #get the image
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    
    #load the image
    img = load_img(image_path, target_size=(224,224))
    #convert into numpy array
    img = img_to_array(img)
    #scale the image
    image = img / 255.0
    image = image.astype(np.float32)
    #reshape the image for predcition
    image = image.reshape(1, 224, 224, 3)
    #prediction
    prediction = model.predict(image)
    final = np.argmax(prediction)
    classi = class_names[final]
    print(classi)


    return render_template('index.html', classi=classi)


if __name__ == '__main__':
    app.run(debug=True)