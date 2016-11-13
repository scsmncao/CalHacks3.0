# Amadeus Flight API Test

true, false = True, False

test = [
  {
    "fare": {
      "price_per_adult": {
        "tax": "59.02",
        "total_fare": "230.02"
      },
      "restrictions": {
        "change_penalties": true,
        "refundable": false
      },
      "total_price": "230.02"
    },
    "itineraries": [
      {
        "outbound": {
          "flights": [
            {
              "aircraft": "789",
              "arrives_at": "2016-11-26T08:35",
              "booking_info": {
                "booking_code": "H",
                "seats_remaining": 9,
                "travel_class": "ECONOMY"
              },
              "departs_at": "2016-11-25T21:20",
              "destination": {
                "airport": "LGW",
                "terminal": "S"
              },
              "flight_number": "7148",
              "marketing_airline": "DY",
              "operating_airline": "DY",
              "origin": {
                "airport": "BOS",
                "terminal": "E"
              }
            }
          ]
        }
      }
    ]
  },
  {
    "fare": {
      "price_per_adult": {
        "tax": "127.90",
        "total_fare": "1530.90"
      },
      "restrictions": {
        "change_penalties": true,
        "refundable": false
      },
      "total_price": "1530.90"
    },
    "itineraries": [
      {
        "outbound": {
          "flights": [
            {
              "aircraft": "744",
              "arrives_at": "2016-11-26T05:10",
              "booking_info": {
                "booking_code": "H",
                "seats_remaining": 9,
                "travel_class": "ECONOMY"
              },
              "departs_at": "2016-11-25T17:55",
              "destination": {
                "airport": "LHR",
                "terminal": "5"
              },
              "flight_number": "212",
              "marketing_airline": "BA",
              "operating_airline": "BA",
              "origin": {
                "airport": "BOS",
                "terminal": "E"
              }
            }
          ]
        }
      }
    ]
  }]

f = fares(test)

'''
  ,
  {
    "fare": {
      "price_per_adult": {
        "tax": "127.90",
        "total_fare": "1530.90"
      },
      "restrictions": {
        "change_penalties": true,
        "refundable": false
      },
      "total_price": "1530.90"
    },
    "itineraries": [
      {
        "outbound": {
          "flights": [
            {
              "aircraft": "744",
              "arrives_at": "2016-11-26T05:10",
              "booking_info": {
                "booking_code": "H",
                "seats_remaining": 9,
                "travel_class": "ECONOMY"
              },
              "departs_at": "2016-11-25T17:55",
              "destination": {
                "airport": "LHR",
                "terminal": "5"
              },
              "flight_number": "4639",
              "marketing_airline": "IB",
              "operating_airline": "BA",
              "origin": {
                "airport": "BOS",
                "terminal": "E"
              }
            }
          ]
        }
      }
    ]
  },
  {
    "fare": {
      "price_per_adult": {
        "tax": "127.90",
        "total_fare": "1530.90"
      },
      "restrictions": {
        "change_penalties": true,
        "refundable": false
      },
      "total_price": "1530.90"
    },
    "itineraries": [
      {
        "outbound": {
          "flights": [
            {
              "aircraft": "744",
              "arrives_at": "2016-11-26T05:10",
              "booking_info": {
                "booking_code": "H",
                "seats_remaining": 9,
                "travel_class": "ECONOMY"
              },
              "departs_at": "2016-11-25T17:55",
              "destination": {
                "airport": "LHR",
                "terminal": "5"
              },
              "flight_number": "5412",
              "marketing_airline": "AY",
              "operating_airline": "BA",
              "origin": {
                "airport": "BOS",
                "terminal": "E"
              }
            }
          ]
        }
      }
    ]
  },
  {
    "fare": {
      "price_per_adult": {
        "tax": "127.90",
        "total_fare": "1530.90"
      },
      "restrictions": {
        "change_penalties": true,
        "refundable": false
      },
      "total_price": "1530.90"
    },
    "itineraries": [
      {
        "outbound": {
          "flights": [
            {
              "aircraft": "744",
              "arrives_at": "2016-11-26T05:10",
              "booking_info": {
                "booking_code": "H",
                "seats_remaining": 7,
                "travel_class": "ECONOMY"
              },
              "departs_at": "2016-11-25T17:55",
              "destination": {
                "airport": "LHR",
                "terminal": "5"
              },
              "flight_number": "6163",
              "marketing_airline": "AA",
              "operating_airline": "BA",
              "origin": {
                "airport": "BOS",
                "terminal": "E"
              }
            }
          ]
        }
      }
    ]
  },
  {
    "fare": {
      "price_per_adult": {
        "tax": "286.90",
        "total_fare": "1530.90"
      },
      "restrictions": {
        "change_penalties": true,
        "refundable": true
      },
      "total_price": "1530.90"
    },
    "itineraries": [
      {
        "outbound": {
          "flights": [
            {
              "aircraft": "76W",
              "arrives_at": "2016-11-26T07:20",
              "booking_info": {
                "booking_code": "H",
                "seats_remaining": 9,
                "travel_class": "ECONOMY"
              },
              "departs_at": "2016-11-25T19:34",
              "destination": {
                "airport": "LHR",
                "terminal": "3"
              },
              "flight_number": "58",
              "marketing_airline": "DL",
              "operating_airline": "DL",
              "origin": {
                "airport": "BOS",
                "terminal": "A"
              }
            }
          ]
        }
      }
    ]
  },
  {
    "fare": {
      "price_per_adult": {
        "tax": "286.90",
        "total_fare": "1530.90"
      },
      "restrictions": {
        "change_penalties": true,
        "refundable": true
      },
      "total_price": "1530.90"
    },
    "itineraries": [
      {
        "outbound": {
          "flights": [
            {
              "aircraft": "76W",
              "arrives_at": "2016-11-26T07:20",
              "booking_info": {
                "booking_code": "K",
                "seats_remaining": 9,
                "travel_class": "ECONOMY"
              },
              "departs_at": "2016-11-25T19:34",
              "destination": {
                "airport": "LHR",
                "terminal": "3"
              },
              "flight_number": "3681",
              "marketing_airline": "AF",
              "operating_airline": "DL",
              "origin": {
                "airport": "BOS",
                "terminal": "A"
              }
            }
          ]
        }
      }
    ]
  },
  {
    "fare": {
      "price_per_adult": {
        "tax": "286.90",
        "total_fare": "1530.90"
      },
      "restrictions": {
        "change_penalties": true,
        "refundable": true
      },
      "total_price": "1530.90"
    },
    "itineraries": [
      {
        "outbound": {
          "flights": [
            {
              "aircraft": "76W",
              "arrives_at": "2016-11-26T07:20",
              "booking_info": {
                "booking_code": "L",
                "seats_remaining": 9,
                "travel_class": "ECONOMY"
              },
              "departs_at": "2016-11-25T19:34",
              "destination": {
                "airport": "LHR",
                "terminal": "3"
              },
              "flight_number": "4012",
              "marketing_airline": "VS",
              "operating_airline": "DL",
              "origin": {
                "airport": "BOS",
                "terminal": "A"
              }
            }
          ]
        }
      }
    ]
  },
  {
    "fare": {
      "price_per_adult": {
        "tax": "286.90",
        "total_fare": "1530.90"
      },
      "restrictions": {
        "change_penalties": true,
        "refundable": true
      },
      "total_price": "1530.90"
    },
    "itineraries": [
      {
        "outbound": {
          "flights": [
            {
              "aircraft": "76W",
              "arrives_at": "2016-11-26T07:20",
              "booking_info": {
                "booking_code": "K",
                "seats_remaining": 9,
                "travel_class": "ECONOMY"
              },
              "departs_at": "2016-11-25T19:34",
              "destination": {
                "airport": "LHR",
                "terminal": "3"
              },
              "flight_number": "6186",
              "marketing_airline": "KL",
              "operating_airline": "DL",
              "origin": {
                "airport": "BOS",
                "terminal": "A"
              }
            }
          ]
        }
      }
    ]
  },
  {
    "fare": {
      "price_per_adult": {
        "tax": "27.90",
        "total_fare": "5201.90"
      },
      "restrictions": {
        "change_penalties": false,
        "refundable": true
      },
      "total_price": "5201.90"
    },
    "itineraries": [
      {
        "outbound": {
          "flights": [
            {
              "aircraft": "744",
              "arrives_at": "2016-11-26T05:10",
              "booking_info": {
                "booking_code": "Y",
                "seats_remaining": 9,
                "travel_class": "ECONOMY"
              },
              "departs_at": "2016-11-25T17:55",
              "destination": {
                "airport": "LHR",
                "terminal": "5"
              },
              "flight_number": "8912",
              "marketing_airline": "EI",
              "operating_airline": "EI",
              "origin": {
                "airport": "BOS",
                "terminal": "E"
              }
            }
          ]
        }
      }
    ]
  }
]
'''
