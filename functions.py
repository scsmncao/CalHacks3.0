from geopy.distance import vincenty
import geocoder

# Data

def fares(results):
    """Returns a list of all the cheapest fare options from RESULTS."""
    all_flights = []
    for flights in results:
        all_flights.append(flights)
    return all_flights

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


# Cheapest Priced Flight

def total_prices(fares):
    """Returns a dictionary of the total price of each flight from FARES,
    with origin & destination airports as the key and total price as the values."""
    prices_by_fare = {}
    for f in fares:
        total_price = float(f["fare"]["total_price"])
        prices_by_fare['[{0}] to [{1}]'.format(origin(f), destination(f))] = total_price
    return prices_by_fare

def cheapest_flight(fares):
    """Returns the cheapest flight in the format '[ORIGIN] to [DESTINATION]'."""
    return min(total_prices(fares), key=total_prices(fares).get)

def cheapest_flight_price(fares):
    """Returns the cheapest flight from the dictionary of FARES_WITH_PRICES."""
    return min(total_prices(fares).values())


# CO2 Emission

def no_stop_distances(fares):
    """Returns a dictionary of the total distance (in miles) of each flight from FARES,
    with origin & destination airports as the key and distance as the values."""
    distances_by_fare = {}
    for f in fares:
        origin_lat, origin_lng = latitude(origin(f)), longitude(origin(f))
        destin_lat, destin_lng = latitude(destination(f)), longitude(destination(f))
        distance = vincenty((origin_lat, origin_lng), (destin_lat, destin_lng)).miles
        distances_by_fare['[{0}] to [{1}]'.format(origin(f), destination(f))] = distance
    return distances_by_fare

# def multiple_stop_distance(fares):
    # STILL NEED TO WORK ON: Get distance with multiple stops (?)

def co2_flight_emissions(fares):
    """Returns a dictionary of the total CO2 emissions (in kg) of each flight from FARES."""
    co2_by_fare, distances_by_fare = {}, no_stop_distances(fares)
    for f in distances_by_fare:
        co2_by_fare[f] = distances_by_fare[f] * 0.21 * 0.453592
    return co2_by_fare

# def co2_train_emissions(fares):
    # STILL NEED TO WORK ON: Train's CO2-Emission per MILE, lol.

def lowest_co2_flight(fares):
    """Returns the flight with the lowest per passenger CO2-emission from FARES."""
    return min(co2_flight_emissions(fares), key=co2_flight_emissions(fares).get)

def lowest_co2_flight_amount(fares):
    """Returns the lowest per passenger CO2-emission from FARES."""
    return min(co2_flight_emissions(fares).values())
