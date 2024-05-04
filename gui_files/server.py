from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

# used to store the url received in post request
url_string = ''

# This function takes a post request and decodes the request data
# This allows us to save the url as a string
@app.route('/', methods=['POST'])
@cross_origin()
def get_url():
    if request.method == 'POST':
        global url_string
        resp_json = request.get_data()
        url = resp_json.decode()
        url_string = url_cleaner(url)
        print(url_string)
        return url_string

# Allows kivy gui to make a get request to this function to get the url
@app.route('/get', methods=['GET'])
@cross_origin()
def send_url():
    if request.method == 'GET':
        global url_string
        clean_url = url_string.strip()
        print(f'get request: {url_string}')
        return url_string
# strips the url to get the domain name only
def url_cleaner(link):
    url = link.replace('url', '').replace('"', '').replace('}', '').replace('{','').replace(':', '').replace('www.', '')
    return url
    
if __name__ == "__main__":
    app.run()