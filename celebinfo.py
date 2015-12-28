import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
from bs4 import BeautifulSoup
import requests
import json
import datetime

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/api/date/<day>/<month>')
def api(day, month):
	# Collecting individual celebrity link
	URL = "http://www.famousbirthdays.com/" + str(month) + str(day) + ".html"
	HTML = requests.get(URL).content
	SOUP = BeautifulSoup(HTML, "html.parser")
	ALL_LINKS = SOUP.find_all('a', 'celeb')

	# Variables to store date
	response = {}
	data = []

	# My info :p
	if day == '28' and month == 'september':
		data.append({"name": "Daxeel Soni", "photo_url": "http://daxeelsoni.in/images/me.jpg", "occupation": "Developer of this API. More: www.daxeelsoni.in", "birthday": "September 28", "birth_year": "1996", "birth_place": "Harij, Gujarat, India", "age": "18", "birth_sign": "Pisces"})

	# Gettinge data from each links
	for each in ALL_LINKS:

		URL = each['href']
		HTML = requests.get(URL).content
		SOUP = BeautifulSoup(HTML, "html.parser")

		try:name = SOUP.find_all('h2')[1].string
		except:name = "Not Found"

		try:photo_url = SOUP.figure.a.img['src']
		except:photo_url = "Not Found"
		
		try:occupation = SOUP.findAll("strong", { "class" : "uppercase" })[0].a.font.span.string
		except:occupation = "Not Found"

		try:birthday = SOUP.findAll("strong", { "class" : "overflow" })[0].time.a.b.font.string
		except:birthday = "Not Found"

		try:birth_year = SOUP.findAll("strong", { "class" : "overflow" })[0].time.find_all('a')[1].b.font.string
		except:birth_year = "Not Found"

		try:birth_place = SOUP.findAll("strong", { "class" : "overflow" })[1].a.b.font.string
		except:birth_place = "Not Found"

		try:age = int((SOUP.findAll("strong", { "class" : "overflow" })[2].b.font.a.font.string).split()[0])
		except:age = "Not Found"

		try:birth_sign = SOUP.findAll("strong", { "class" : "overflow" })[3].a.b.font.string
		except:birth_sign = "Not Found"

		data.append({"name": name, "photo_url": photo_url, "occupation": occupation, "birthday": birthday, "birth_year": birth_year, "birth_place": birth_place, "age": age, "birth_sign": birth_sign})

	# Return json response
	response['data'] = data
	return json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))

@app.route('/api/custom/<filter_type>')
def custom(filter_type):
	error = 0
	if filter_type == 'yesterday':
		day = str(int(datetime.datetime.now().strftime("%d")) - 1)
	elif filter_type == 'today':
		day = datetime.datetime.now().strftime("%d")
	elif filter_type == 'tomorrow':
		day = str(int(datetime.datetime.now().strftime("%d")) + 1)
	elif filter_type == 'tdat':
		day = str(int(datetime.datetime.now().strftime("%d")) + 2)
	else:
		error = 1
		
	if error == 0:
		month = datetime.datetime.now().strftime("%B").lower()
		return api(day, month)
	else:
		return {"error": "Invalid API syntax"}

@app.route('/api/name/<celeb_name>')
def name(celeb_name):
	URL = "http://www.famousbirthdays.com/names/" + celeb_name + ".html"
	HTML = requests.get(URL).content
	SOUP = BeautifulSoup(HTML, "html.parser")

	if SOUP.title.string == "Page Not Found":
		return json.dumps({"error": "Not found"}, sort_keys=True, indent=4, separators=(',', ': '))
	else:
		ALL_LINKS = SOUP.find_all('a', 'celeb')

		# Variables to store date
		response = {}
		data = []

		# Gettinge data from each links
		for each in ALL_LINKS:

			URL = each['href']
			HTML = requests.get(URL).content
			SOUP = BeautifulSoup(HTML, "html.parser")

			try:name = SOUP.find_all('h2')[1].string
			except:name = "Not Found"

			try:photo_url = SOUP.figure.a.img['src']
			except:photo_url = "Not Found"
			
			try:occupation = SOUP.findAll("strong", { "class" : "uppercase" })[0].a.font.span.string
			except:occupation = "Not Found"

			try:birthday = SOUP.findAll("strong", { "class" : "overflow" })[0].time.a.b.font.string
			except:birthday = "Not Found"

			try:birth_year = SOUP.findAll("strong", { "class" : "overflow" })[0].time.find_all('a')[1].b.font.string
			except:birth_year = "Not Found"

			try:birth_place = SOUP.findAll("strong", { "class" : "overflow" })[1].a.b.font.string
			except:birth_place = "Not Found"

			try:age = int((SOUP.findAll("strong", { "class" : "overflow" })[2].b.font.a.font.string).split()[0])
			except:age = "Not Found"

			try:birth_sign = SOUP.findAll("strong", { "class" : "overflow" })[3].a.b.font.string
			except:birth_sign = "Not Found"

			data.append({"name": name, "photo_url": photo_url, "occupation": occupation, "birthday": birthday, "birth_year": birth_year, "birth_place": birth_place, "age": age, "birth_sign": birth_sign})

		# Return json response
		response['data'] = data
		return json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    app.run()
