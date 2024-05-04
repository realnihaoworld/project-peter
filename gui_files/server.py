from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def get_url():
    if request.method == 'POST':
        #received = request.get_json()
        #ata = received['url']
        # data = request.form.get("url")
        # print(f"data: {data}")
        # return {"url": data}
        resp_json = request.get_data()
        url = resp_json.decode()
        print(json.dumps(url))
        #return make_response(jsonify({'url': url}), 200)
        return json.dumps(url)
        
if __name__ == "__main__":
    app.run()