from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/api/hello')
def start():
    return "Hallo, Welt."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    