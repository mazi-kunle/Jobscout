#!/usr/bin/python3
'''
A python module that handles the
backend of jobscout
'''

from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
	'''
	returns the home page
	'''
	return render_template('index.html')


@app.route('/result', strict_slashes=False, methods=['POST'])
def form():
	'''
	extract data from form and parse it to the api
	'''
	specilization = request.form['specilization']
	location = request.form['location']

	return render_template('')




if __name__ == '__main__':
	app.run(debug=True)