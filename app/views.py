from flask import render_template, Flask, jsonify
from app import app
from functions import *
import requests

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/search/api/v1.0/flight-info', methods=['GET'])
def get_flight_info():
    flight = requests.get('https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=R26ZAzuBsJnmMFFX2RVh0qEK2PpDLgPx&origin=BOS&destination=LON&departure_date=2016-11-25&nonstop=true')
    json_object = flight.json()
    return jsonify(json_object['results'])

# @app.route('/')
# @app.route('/index')

# def index():
#     user = {'nickname': 'Miguel'}  # fake user
#     posts = [  # fake array of posts
#         {
#             'author': {'nickname': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'nickname': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template("index.html",
#                            title='Home',
#                            user=user,
#                            posts=posts)
