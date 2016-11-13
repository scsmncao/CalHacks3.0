from flask import render_template, Flask, jsonify
from app import app
from . import functions
import requests
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/results')
def results():
    airport_from = request.args.get('from')
    to = request.args.get('to')
    departure_date = request.args.get('departure_date')
    return_date = request.args.get('return_date')
    adults = request.args.get('adults')
    children = request.args.get('children')
    infants = request.args.get('infants')
    data = {
        'eco_flight':[{
            'duration': '2h 10m',
            'take_off_date': 'Sep 11, 2016',
            'landing_date': 'Sep 11, 2016',
            'take_off_time': '4:20 AM',
            'landing_time': '6:30 AM',
            'price_of_flight': '241',
            'destination_airport': 'LAX',
            'origin_airport': 'SFO',
            'eco_grade': 'A',
            'flight_number': '7143',
            'airline': 'Delta',
            'emissions': '40 kg'
        }],
        'cheap_flight':[{
            'duration': '2h 10m',
            'take_off_date': 'Sep 11, 2016',
            'landing_date': 'Sep 11, 2016',
            'take_off_time': '4:20 PM',
            'landing_time': '6:30 PM',
            'price_of_flight': '128',
            'destination_airport': 'LAX',
            'origin_airport': 'SFO',
            'eco_grade': 'B',
            'flight_number': '7543',
            'airline': 'Delta',
            'emissions': '40 kg'
        }],
        'public_transit': [
        {
            'origin': 'SFO',
            'destination': 'LAX',
            'depart_date': 'Sep 11, 2016',
            'arrive_date': 'Sep 11, 2016',
            'depart_time': '12:30 AM',
            'arrive_time': '8:40 PM',
            'duration': '10h 10m',
            'price': '54',
            'eco_grade': 'A'
        }
        ],
        'car': {
            'duration': '5h 30m',
            'eco_grade': 'A'
        }
    }
    return render_template("results.html", airport_from=airport_from, to=to, departure_date=departure_date, data=data)

@app.route('/search/api/v1.0/flight-info', methods=['GET'])
def get_flight_info(): # for Cheapest Flight
    flight = requests.get('https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=R26ZAzuBsJnmMFFX2RVh0qEK2PpDLgPx&origin=BOS&destination=LON&departure_date=2016-11-25&nonstop=false')
    json_object = flight.json()
    return jsonify(json_object['results'])

@app.route('/search/api/v1.0/nonstop-flight-info', methods=['GET'])
def get_nonstop_flight_info(): # for Ecoflight
    nonstop_flight = requests.get('https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=R26ZAzuBsJnmMFFX2RVh0qEK2PpDLgPx&origin=BOS&destination=LON&departure_date=2016-11-25&nonstop=true')
    json_object = nonstop_flight.json()
    return jsonify(json_object['results'])

@app.route('/search/api/v1.0/drive-info', methods=['GET'])
def get_drive_info():
    drive = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=Boston+Logan+International+Airport,+1+Harborside+Dr,+Boston,+MA+02128&destination=John+F.+Kennedy+International+Airport,+New+York,+NY+11430&key=AIzaSyAupEuZynix3YD4F9QTknDAdLNEEIUqX7k')
    json_object = drive.json()
    return jsonify(json_object['routes'])

@app.route('/search/api/v1.0/transit-info', methods=['GET'])
def get_transit_info():
    transit = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=Boston+Logan+International+Airport,+1+Harborside+Dr,+Boston,+MA+02128&destination=John+F.+Kennedy+International+Airport,+New+York,+NY+11430&mode=transit&key=AIzaSyAupEuZynix3YD4F9QTknDAdLNEEIUqX7k')
    json_object = transit.json()
    return jsonify(json_object['routes'])
