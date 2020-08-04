# from flask import Flask
# app = Flask(__name__)

# @app.route('/api/hello')
# def start():
#     return "Hallo, Welt."

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')


import sys


def application(env, start_response):
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    start_response("200 OK", [("Content-Type", "text/plain")])
    message = "Hallo, Welt."
    return [message.encode("utf-8")]
    