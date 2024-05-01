from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def get_url():
    if request.method == 'POST':
        received = request.get_json()
        data = received['url']
        print(data)
        return {"sucess": True}

if __name__ == "__main__":
    app.run()