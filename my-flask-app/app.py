#!/usr/bin/python3
'''
A python module that handles the
backend of jobscout
'''

from flask import Flask, render_template, request, abort, jsonify
import requests
import os
import json


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
	'''
	returns the home page
	'''
	return render_template('landing.html')


@app.route('/search', strict_slashes=False)
def search():
	'''
	handle the search route
	'''
	return render_template('search.html')


@app.route('/result', strict_slashes=False, methods=['POST'])
def form():
	'''
	extract data from form and parse it to the api
	'''
	form_data = request.form
	specialization = form_data['Specialization']
	location = form_data['Location']


	API_KEY = os.getenv('API_KEY')
	API_HOST = os.getenv('API_HOST')
	
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
	
	# with open('storage.json') as f:
	# 	data = json.load(f)
	data = res.json()
	return render_template('data.html', data=data)






if __name__ == '__main__':
	app.run(debug=True)