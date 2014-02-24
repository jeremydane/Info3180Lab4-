""" 
JDF
"""

import os
import sys

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import render_template
app = Flask(__name__.split('.')[0])

@app.route('/')
@app.route('/<name>')
def menu(name=None):
  return render_template('menu.html', name=name)

@app.route('/catwalk')
@app.route('/<name>')
def cat(name=None):
  return render_template('catwalk.html', name=name)


@app.route('/madlib')
@app.route('/<name>')
def mad(name=None):
  return render_template('madlib.html', name=name)
