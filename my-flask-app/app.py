#!/usr/bin/python3
'''
A python module that handles the
backend of jobscout
'''

from flask import Flask, render_template, request, abort
import requests
import os


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
	'''
	returns the home page
	'''
	return render_template('landing.html')


@app.route('/result', strict_slashes=False, methods=['POST'])
def form():
	'''
	extract data from form and parse it to the api
	'''
	specialization = request.form['specialization']
	location = request.form['location']

	API_KEY = os.getenv('API_KEY')
	API_HOST = os.genenv('API_HOST')

	url = "https://linkedin-jobs-search.p.rapidapi.com/"
	payload = {
		'search_terms': specialization,
		'location': location,
		'page': '1'
	}

	headers = {
		'content-type': 'application/json',
		'X-RapidAPI-Key': API_KEY,
		'X-RapidAPI-Host': API_HOST
	}

	res = requests.post(url, json=payload, headers=headers)

	if res.status_code != 200:
		abort(404, description='Resource not found')
	
	data = res.json()






if __name__ == '__main__':
	app.run(debug=True)