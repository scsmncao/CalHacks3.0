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

# CO2 Emission for Flights

def distance(fare):
    """Returns the DISTANCE (in miles) from FARE."""
    origin_lat, origin_lng = latitude(origin(fare)), longitude(origin(fare))
    destin_lat, destin_lng = latitude(destination(fare)), longitude(destination(fare))
    return vincenty((origin_lat, origin_lng), (destin_lat, destin_lng)).miles

def no_stop_distances(fares):
    """Returns a dictionary of the total distance (in miles) of each flight from FARES."""
    distances_by_fare = {}
    for f in fares:
        distances_by_fare['Flight #{0}'.format(flight_number(f))] = distance(f)
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
    minutes = int(distance(fare) // 7.45645)
    if minutes > 59:
        hours = int(minutes // 60)
        minutes -= 60 * hours
    return "{0}h {1}m".format(hours, minutes)

# Cheapest Priced Flight

def total_prices(fares):
    """Returns a dictionary of the total price of each flight from FARES."""
    prices_by_fare = {}
    for f in fares:
        total_price = float(f["fare"]["total_price"])
        prices_by_fare[flight_number(f)] = total_price
    return prices_by_fare

def cheapest_flight(fares):
    """Returns the cheapest flight in the form of FLIGHT NUMBER."""
    return min(total_prices(fares), key=total_prices(fares).get)

def cheapest_flight_price(fares):
    """Returns the cheapest flight from the dictionary of FARES_WITH_PRICES."""
    return min(total_prices(fares).values())

# Ecoflight

def eco_time(fares):
    """Returns the flight fom FARES that is closest to 6am in take off time."""
    fare_times = {}
    for f in fares:
        t = int(take_off_time_mil(f)[:2])
        fare_times[flight_number(f)] = t
    return min(fare_times, key=lambda x: fare_times[x] if fare_times[x] >= 6 else d[x]+12)

### Transit & Driving ###

# Transit Route Data Unpacker

def route(routes): # (FOR G-MAPS-TRANSIT & DRVING API)
    """Returns the route (transit or driving) from ROUTES."""
    return routes["legs"][0]

# Transit Data Elements

def t_origin(t):
    return t["start_address"]

def t_destination(t):
    return t["end_address"]

def t_arrive_time(t):
    return t["arrival_time"]["text"]

def t_depart_time(t):
    return t["departure_time"]["text"]

def t_arrive_date():
    fares = fares(results) # Amadeus API
    return take_off_date(fares)

def t_duration(t):
    return t["duration"]["text"]

def t_price(t):
    return int(t["distance"]["text"][:-3]) * 0.78

def t_emissions(t):
    return int(t["distance"]["text"][:-3]) * 0.08 * 0.453592

# Driving Data Elements

def d_duration(d):
    return d["duration"]["text"]

def d_emissions(d):
    return int(t["distance"]["text"][:-3]) * 0.35 * 0.453592

### Eco-Grade ###

# def eco_grade(emission):
#     """Return the ECO-GRADE based on CO-2 emitted."""
