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

@app.route('/search/api/v1.0/drive-info', methods=['GET'])
def get_drive_info():
    drive = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=75+9th+Ave+New+York,+NY&destination=MetLife+Stadium+1+MetLife+Stadium+Dr+East+Rutherford,+NJ+07073&key=AIzaSyAupEuZynix3YD4F9QTknDAdLNEEIUqX7k')
    json_object = drive.json()
    return jsonify(json_object)
    
@app.route('/search/api/v1.0/transit-info', methods=['GET'])
def get_transit_info():
    transit = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=75+9th+Ave+New+York,+NY&destination=MetLife+Stadium+1+MetLife+Stadium+Dr+East+Rutherford,+NJ+07073&mode=transit&arrival_time=1391374800&key=AIzaSyAupEuZynix3YD4F9QTknDAdLNEEIUqX7k')
    json_object = transit.json()
    return jsonify(json_object)

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
