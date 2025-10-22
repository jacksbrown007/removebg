from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return "BgSub Background Remover API is running ✅"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No image file uploaded', 400

    img = request.files['image'].read()
    output = remove(img)
    return send_file(BytesIO(output), mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
