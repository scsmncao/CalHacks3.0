from flask import render_template, Flask, jsonify

import requests
from flask import request
from geopy.distance import vincenty
from datetime import datetime
from datetime import timedelta
import geocoder, json



### Flight ###

# Airlines Data

with open('airlines.json') as json_data:
    airlines_iata = json.load(json_data)

# Flight Route Data

def fares(results): # (FOR AMADEUS API - FLIGHTS)
    """Returns a list of all the cheapest fare options from RESULTS."""
    all_flights = []
    for flights in results:
        all_flights.append(flights)
    return all_flights

# Flight Data Elements

def price(fare):
    """Returns the PRICE of the FARE."""
    return fare["fare"]["total_price"]

def airline_name(fare):
    """Returns the AIRLINE NAME from FARE."""
    airline_code = fare["itineraries"][0]["outbound"]["flights"][0]["operating_airline"]
    for d in airlines_iata:
        if d['iata'] == airline_code:
            return d['name']
    return airline_code

def flight_number(fare):
    """Return the FLIGHT NUMBER from FARE."""
    return fare["itineraries"][0]["outbound"]["flights"][0]["flight_number"]

def take_off_time(fare):
    """Return the TAKE OFF TIME from FARE."""
    time = fare["itineraries"][0]["outbound"]["flights"][0]["departs_at"][11:]
    formatted_time = datetime.strptime(time, "%H:%M")
    return formatted_time.strftime("%I:%M %p")

def take_off_time_mil(fare):
    """Return the MILITARY TAKE OFF TIME from FARE."""
    return fare["itineraries"][0]["outbound"]["flights"][0]["departs_at"][11:]

def take_off_date(fare):
    """Return the TAKE OFF DATE from FARE."""
    time_str = fare["itineraries"][0]["outbound"]["flights"][0]["departs_at"]
    return time_str[5:7] + "/" + time_str[8:10] + "/" + time_str[:4]

def landing_time(fare):
    """Return the LANDING TIME from FARE."""
    time = fare["itineraries"][0]["outbound"]["flights"][0]["arrives_at"][11:]
    formatted_time = datetime.strptime(time, "%H:%M")
    return formatted_time.strftime("%I:%M %p")

def landing_time_mil(fare):
    """Return the MILITARY LANDING TIME from FARE."""
    return fare["itineraries"][0]["outbound"]["flights"][0]["arrives_at"][11:]

def landing_date(fare):
    """Return the LANDING DATE from FARE."""
    time_str = fare["itineraries"][0]["outbound"]["flights"][0]["arrives_at"]
    return time_str[5:7] + "/" + time_str[8:10] + "/" + time_str[:4]

def origin(fare):
    """Return the ORIGIN AIRPORT from FARE."""
    return fare["itineraries"][0]["outbound"]["flights"][0]["origin"]["airport"]

def destination(fare):
    """Return the DESTINATION AIRPORT from FARE."""
    return fare["itineraries"][0]["outbound"]["flights"][0]["destination"]["airport"]

def latitude(location):
    """Returns the LATITUDE COORDINATE of the LOCATION."""
    return geocoder.google('{0} AIRPORT'.format(location)).lat

def longitude(location):
    """Returns the LONGITUDE COORDINATE of the LOCATION."""
    return geocoder.google('{0} AIRPORT'.format(location)).lng

def reference(fares):
    """Reference JSON to each fare in FARES by FLIGHT NUMBER."""
    reference = {}
    for f in fares:
        reference[flight_number(f)] = f
    return reference


def price_cheap(fare):
    """Returns the PRICE of the FARE."""
    return fare["fare"]["total_price"]

def airline_name_cheap(fare):
    """Returns the AIRLINE NAME from FARE."""
    airline_code = fare["operating_airline"]
    for d in airlines_iata:
        if d['iata'] == airline_code:
            return d['name']
    return airline_code

def flight_number_cheap(fare):
    """Return the FLIGHT NUMBER from FARE."""
    return fare["flight_number"]

def take_off_time_cheap(fare):
    """Return the TAKE OFF TIME from FARE."""
    time = fare["departs_at"][11:]
    formatted_time = datetime.strptime(time, "%H:%M")
    return formatted_time.strftime("%I:%M %p")

def take_off_time_mil_cheap(fare):
    """Return the MILITARY TAKE OFF TIME from FARE."""
    return fare["departs_at"][11:]

def take_off_date_cheap(fare):
    """Return the TAKE OFF DATE from FARE."""
    time_str = fare["departs_at"]
    return time_str[5:7] + "/" + time_str[8:10] + "/" + time_str[:4]

def landing_time_cheap(fare):
    """Return the LANDING TIME from FARE."""
    time = fare["arrives_at"][11:]
    formatted_time = datetime.strptime(time, "%H:%M")
    return formatted_time.strftime("%I:%M %p")

def landing_time_mil_cheap(fare):
    """Return the MILITARY LANDING TIME from FARE."""
    return fare["itineraries"][0]["outbound"]["flights"][0]["arrives_at"][11:]

def landing_date_cheap(fare):
    """Return the LANDING DATE from FARE."""
    time_str = fare["itineraries"][0]["outbound"]["flights"][0]["arrives_at"]
    return time_str[5:7] + "/" + time_str[8:10] + "/" + time_str[:4]

def origin_cheap(fare):
    """Return the ORIGIN AIRPORT from FARE."""
    return fare["origin"]["airport"]

def destination_cheap(fare):
    """Return the DESTINATION AIRPORT from FARE."""
    return fare["destination"]["airport"]

# CO2 Emission for Flights

def distance(fare):
    """Returns the DISTANCE (in miles) from FARE."""
    origin_lat, origin_lng = latitude(origin(fare[0])), longitude(origin(fare[0]))
    destin_lat, destin_lng = latitude(destination(fare[0])), longitude(destination(fare[0]))
    return vincenty((origin_lat, origin_lng), (destin_lat, destin_lng)).miles

def emission(fare):
    """Returns the CO2 emissions of the FARE in kg."""
    return distance(fare) * 0.21 * 0.453592

def no_stop_distances(fares):
    """Returns a dictionary of the total distance (in miles) of each flight from FARES."""
    distances_by_fare = {}
    for f in fares:
        distances_by_fare[flight_number(f)] = distance(f)
    return distances_by_fare

def co2_flight_emissions(fares):
    """Returns a dictionary of the total CO2 emissions (in kg) of each flight from FARES."""
    co2_by_fare, distances_by_fare = {}, no_stop_distances(fares)
    for f in distances_by_fare:
        co2_by_fare[f] = distances_by_fare[f] * 0.21 * 0.453592
    return co2_by_fare

def lowest_co2_flight(fares):
    """Returns the flight with the lowest per passenger CO2-emission from FARES."""
    return min(co2_flight_emissions(fares), key=co2_flight_emissions(fares).get)

def lowest_co2_flight_amount(fares):
    """Returns the lowest per passenger CO2-emission from FARES."""
    return min(co2_flight_emissions(fares).values())

# Flight Duration

def duration(fare):
    """Returns the string DURATION of the FARE, given an average flight travels 7.45645 mi/min."""
    minutes = int(distance(fare) / 7.45645)
    print(distance(fare))
    print(minutes)
    hours = 0
    if minutes > 59:
        hours = int(minutes // 60)
        minutes -= 60 * hours
    return "{0}h {1}m".format(hours, minutes)

# Cheapest Priced Flight

def cheapest_flights(fares):
    """Returns the 3 cheapest flights from FARES while removing the cheapest fare from the list."""
    prices_by_fare, ref, lst = {}, reference(fares), []
    for f in fares:
        total_price = float(f["fare"]["total_price"])
        prices_by_fare[flight_number(f)] = total_price
    c1 = min(prices_by_fare, key=prices_by_fare.get)
    ref.pop(c1)
    try:
        c2 = min(prices_by_fare, key=prices_by_fare.get)
        ref.pop(c2)
    except KeyError:
        c2 = None
    try:
        c3 = min(prices_by_fare, key=prices_by_fare.get)
        ref.pop(c3)
    except KeyError:
        c3 = None
    for c in [c1, c2, c3]:
        if c:
            lst.append(c)
        else:
            lst.append(None)
    return lst

# def total_prices(fares):
#     """Returns a dictionary of the total price of each flight from FARES."""
#     prices_by_fare = {}
#     for f in fares:
#         total_price = float(f["fare"]["total_price"])
#         prices_by_fare[flight_number(f)] = total_price
#     return prices_by_fare
#
# def cheapest_flight_og(fares):
#     """Returns the cheapest flight in the form of FLIGHT NUMBER."""
#     return min(total_prices(fares), key=total_prices(fares).get)
#
# def cheapest_flight_price(fares):
#     """Returns the cheapest flight from the dictionary of FARES_WITH_PRICES."""
#     return min(total_prices(fares).values())

def cheapest(l):
    return l[0]

def alt_1(l):
    return l[1]

def alt_2(l):
    return l[2]

# Ecoflight

def eco_time(fares):
    """Returns the flight fom FARES that is closest to 6am in take off time."""
    fare_times = {}
    for f in fares:
        t = int(take_off_time_mil(f)[:2])
        fare_times[flight_number(f)] = t
    return min(fare_times, key=lambda x: fare_times[x] if fare_times[x] >= 6 else fare_times[x]+8)

### Transit & Driving ###

# Transit Route Data Unpacker

def route(routes): # (FOR G-MAPS-TRANSIT & DRVING API)
    """Returns the route (transit or driving) from ROUTES."""
    if (len(routes) > 0):
        return routes[0]["legs"][0]

# Transit Data Elements

def t_origin(t):
    return t["start_address"]

def t_destination(t):
    return t["end_address"]

def t_arrive_time(t):
    return t["arrival_time"]["text"]

def t_depart_time(t):
    return t["departure_time"]["text"]

def t_duration(t):
    return t["duration"]["text"]

def t_price(t):
    return int(t["distance"]["text"][:-3].replace(",", "")) * 0.78

def t_emissions(t):
    return int(t["distance"]["text"][:-3].replace(",", "")) * 0.08 * 0.453592

# Driving Data Elements

def d_duration(d):
    return d["duration"]["text"]

def d_emissions(d):
    return int(t["distance"]["text"][:-3].replace(",", "")) * 0.35 * 0.453592

### Eco-Grade ###

# def eco_grade(emission):
#     """Return the ECO-GRADE based on CO-2 emitted."""


def results():
    airport_from = request.args.get('from')
    to = request.args.get('to')
    departure_date = request.args.get('departure_date')
    adults = request.args.get('adults')
    children = request.args.get('children')
    infants = request.args.get('infants')

    c_routes = get_flight_info(airport_from, to, departure_date, adults, children, infants)
    e_routes = get_nonstop_flight_info(airport_from, to, departure_date, adults, children, infants)
    d_routes = get_drive_info(airport_from, to)
    t_routes = get_transit_info(airport_from, to)

    l_c_routes = fares(c_routes)

    d_cheap_flight_2 = []
    flights = l_c_routes[1]["itineraries"][0]["outbound"]["flights"]
    for flight in flights:
        d_cheap_flight_2.append({
        'duration': duration(l_c_routes[1]),
        'take_off_time': take_off_time_cheap(flight),
        'landing_time': landing_time_cheap(flight),
        'price_of_flight': price_cheap(l_c_routes[1]),
        'destination_airport': destination_cheap(flight),
        'origin_airport': origin_cheap(flight),
        'eco_grade': 'A',
        'airline': airline_name_cheap(flight),
        'emissions': emission(l_c_routes[1]) })

    d_cheap_flight_3 = []
    flights = l_c_routes[2]["itineraries"][0]["outbound"]["flights"]
    for flight in flights:
        d_cheap_flight_3.append({
        'duration': duration(l_c_routes[2]),
        'take_off_time': take_off_time_cheap(flight),
        'landing_time': landing_time_cheap(flight),
        'price_of_flight': price_cheap(l_c_routes[2]),
        'destination_airport': destination_cheap(flight),
        'origin_airport': origin_cheap(flight),
        'eco_grade': 'A',
        'airline': airline_name_cheap(flight),
        'emissions': emission(l_c_routes[2]) })

    d_cheap_flight_1 = []
    flights = l_c_routes[0]["itineraries"][0]["outbound"]["flights"]
    for flight in flights:
        d_cheap_flight_1.append({
        'duration': duration(l_c_routes[0]),
        'take_off_time': take_off_time_cheap(flight),
        'landing_time': landing_time_cheap(flight),
        'price_of_flight': price_cheap(l_c_routes[0]),
        'destination_airport': destination_cheap(flight),
        'origin_airport': origin_cheap(flight),
        'eco_grade': 'A',
        'airline': airline_name_cheap(flight),
        'emissions': emission(l_c_routes[0]) })


    l_e_routes = fares(e_routes)
    r_e_routes = reference(l_e_routes)
    if (len(d_cheap_flight_1) > 1):
        eco_flight = l_e_routes[0]
    else:
        eco_flight = r_e_routes[eco_time(l_e_routes)]

    if t_routes:
        l_t_routes = route(t_routes)
        d_transit = [{
            'depart_time': t_depart_time(l_t_routes),
            'arrive_time': t_arrive_time(l_t_routes),
            'duration': t_duration(l_t_routes),
            'price': t_price(l_t_routes),
            'eco_grade': 'A' }]
    else:
        d_transit = []
    if d_routes:
        l_d_routes = route(d_routes)
        d_drive = [{
            'duration': d_duration(l_d_routes),
            'eco_grade': 'A' }]
    else:
        d_drive = []

    # Dictionaries

    d_eco_flight = [{
        'duration': duration(eco_flight),
        'take_off_time': take_off_time(eco_flight),
        'landing_time': landing_time(eco_flight),
        'price_of_flight': price(eco_flight),
        'destination_airport': destination(eco_flight),
        'origin_airport': origin(eco_flight),
        'eco_grade': 'A',
        'airline': airline_name(eco_flight),
        'emissions': emission(eco_flight) }]

    data = {
        'eco_flight':d_eco_flight,
        'cheap_flight_1':d_cheap_flight_1,
        'cheap_flight_2':d_cheap_flight_2,
        'cheap_flight_3':d_cheap_flight_3,
        'public_transit':d_transit,
        'car': d_drive
    }
    return render_template("results.html", airport_from=airport_from, to=to, departure_date=departure_date, data=data)

def date_to_api(s):
    return s[6:] + "-" + s[:2] + "-" + s[3:5]

def get_flight_info(airport_from, to, departure_date, adults, children, infants): # for Cheapest Flight
    flight = requests.get("https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=R26ZAzuBsJnmMFFX2RVh0qEK2PpDLgPx&origin={0}&destination={1}&departure_date={2}&adults={3}&children={4}&infants={5}&nonstop=false&number_of_results=5".format(airport_from, to, date_to_api(departure_date), adults, children, infants))
    json_object = flight.json()
    return json_object['results']

def get_nonstop_flight_info(airport_from, to, departure_date, adults, children, infants): # for Ecoflight
    nonstop_flight = requests.get("https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=R26ZAzuBsJnmMFFX2RVh0qEK2PpDLgPx&origin={0}&destination={1}&departure_date={2}&adults={3}&children={4}&infants={5}&nonstop=true&number_of_results=3".format(airport_from, to, date_to_api(departure_date), adults, children, infants))
    json_object = nonstop_flight.json()
    return json_object['results']

def get_drive_info(airport_from, to):
    drive = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination=J{1}&key=AIzaSyAupEuZynix3YD4F9QTknDAdLNEEIUqX7k'.format(airport_from, to))
    json_object = drive.json()
    return json_object['routes']

def get_transit_info(airport_from, to):
    transit = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&mode=transit&key=AIzaSyAupEuZynix3YD4F9QTknDAdLNEEIUqX7k'.format(airport_from, to))
    json_object = transit.json()
    return json_object['routes']
