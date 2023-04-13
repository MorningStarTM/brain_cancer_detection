from flask import Flask, render_template, url_for, request
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded!'
        
        file = request.files['file']
        
        # Preprocess image for prediction
        img = Image.open(file.stream)
        img = img.resize((224, 224))
        print(file)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)