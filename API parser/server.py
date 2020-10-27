from flask import Flask
from flask_cors import CORS
import os
from parser import parser

file_patch = 'raw_lessions.json'

app = Flask(__name__)
CORS(app)

@app.route("/get_data", methods=['GET'])
def get_data():
    return {'lessions': parser(file_patch)}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 8081)))