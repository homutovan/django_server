from flask import Flask
import os

app = Flask(__name__)

@app.route("/get_data", methods=['GET'])
def get_data():
    return 'hello, world!'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 8081)))