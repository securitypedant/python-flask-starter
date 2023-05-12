import logging, ajax
import logging.handlers as handlers
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# Details on the Secret Key: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing the session data.
app.secret_key = 'BAD_SECRET_KEY_CHANGE_ME'

# Setup logging file
logger = logging.getLogger("myapp")

with app.app_context():
    logger.setLevel('INFO')
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    logHandler = handlers.TimedRotatingFileHandler('logs/log.log', when='D', interval=1, backupCount=7)
    logHandler.setLevel('INFO')
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

@app.context_processor
def available_to_all_templates():
    listofdata = [1,2,3.4]
    return dict(listofdata=listofdata)

# ------------------ ROUTES  ------------------ 
app.add_url_rule('/ajax/getdata', view_func=ajax.ajax_getdata)

@app.route("/", methods=['GET'])
def home():

    date = datetime.now().strftime('%Y-%m-%d')
    favcolors = ["Blue", "Gold", "Orange"]

    return render_template(
        "home.html",
        date=date,
        favcolors=favcolors
    )

@app.route("/about", methods=['GET'])
def about():

    return render_template(
        "about.html",
    )

if __name__ == "__main__":
    app.run()