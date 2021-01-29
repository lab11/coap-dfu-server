from github_webhook import Webhook
from flask import Flask
import sh
import os
import subprocess

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

app_path = os.environ.get('APP_PATH')
pkg_path = os.environ.get('PKG_PATH')
repo_url = os.environ.get('REPO_URL')

#sh.eval("$(ssh-agent -s)")
#sh.ssh-add("/root/.ssh/id_dfu_server")
subprocess.run("./webhook_rebuild.sh")
if not os.path.exists(app_path):
    ssh.git("clone", "--recursive", repo_url, "repo")

if not os.path.exists(pkg_path):
    print('building!')
    print(sh.make('-C', app_path, 'pkg_signed'))

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    print("Got push with: {0}".format(data))
    subprocess.run("./webhook_rebuild.sh")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
