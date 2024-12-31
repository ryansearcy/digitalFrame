from flask import Flask, render_template, request
import os

digitalFrame = Flask(__name__)

@digitalFrame.route("/")
def startServer():
    return render_template('settings.html', transitionTime=os.environ["TRANSITIONTIME"], photoPath=os.environ["PHOTOPATH"])

@digitalFrame.route("/setTransitionTime")
def setTransitionTime():
    os.environ["TRANSITIONTIME"] = request.form['transitionTime']
    return

@digitalFrame.route("/uploadPhotos")
def uploadPhotos():
    return