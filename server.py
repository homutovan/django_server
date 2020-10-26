from flask import Flask, request
from flask_cors import CORS
import os
from parser import parser
from utils import filter_by_date

file_patch = 'raw_lessions.json'

app = Flask(__name__) 
CORS(app)

@app.route('/get_data', methods=['GET'])
def get_data():
    lessions = parser(file_patch)
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    group_count = request.args.get('group_count')
    offset = request.args.get('offset')
    if start_date and end_date:
        lessions = filter_by_date(start_date, end_date, lessions)
    if group_count:
        group_count = int(group_count)
        offset = int(offset)
        lessions = lessions[offset: offset + group_count]
    return {
        'success': 'true',
        'lessions': lessions,
        }

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 8081)))