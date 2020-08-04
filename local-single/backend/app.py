from flask import Flask
app = Flask(__name__)

@app.route('/api/hello')
def start():
    return "Hallo, Welt."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    