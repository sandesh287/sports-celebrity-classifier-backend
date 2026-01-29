from flask import Flask, request, jsonify, send_from_directory
import util
from flask_cors import CORS


app = Flask(__name__, static_folder='../client', static_url_path='')
CORS(app)

app.config['MAX_CONTENT_LENGTH'] = 10*1024*1024   # 5 MB


@app.route('/')
def home():
  return send_from_directory(app.static_folder ,'index.html')


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
  image_data = request.form['image_data']
  
  response = jsonify(util.classify_image(image_data))
  
  response.headers.add('Access-Control-Allow-Origin', '*')
  
  return response


if __name__ == "__main__":
  print('Starting Python Flask Server for Sports Celebrity Image Classification...')
  util.load_saved_artifacts()
  app.run(port=5000)