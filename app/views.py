from flask import render_template, Flask, jsonify
from app import app
from . import functions
import requests

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

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
