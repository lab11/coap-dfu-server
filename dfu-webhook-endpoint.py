from github_webhook import Webhook
from flask import Flask
import sh
import os

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

app_path = os.environ.get('APP_PATH')
pkg_path = os.environ.get('PKG_PATH')

if not os.path.exists(pkg_path):
    print('building!')
    sh.make('-C', app_path, 'pkg_signed')

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("Got push with: {0}".format(data))
    sh.make('-C', app_path, 'clean')
    sh.make('-C', app_path, 'pkg_signed')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
