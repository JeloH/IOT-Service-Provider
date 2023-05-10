import os
from flask import Flask, request, render_template, url_for, redirect
from os import listdir
import json
import re

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return ("Hello")




if __name__ == "__main__":
    app.run(port=4555, debug=False, threaded=True)

#this will execute on app close
# conn.commit()
# conn.close()
