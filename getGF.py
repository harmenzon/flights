import json
import requests

dir = '/services/python/flights/'
# dir = 'E:/Dropbox/GitHub/flights/'

api_key = "AIzaSyAkNllJiGRiCP-iBvx1sZ8LLHnoUnwEv8c"
url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
headers = {'content-type': 'application/json'}

params = {
  "request": {
    "slice": [
      {
        "origin": "AMS",
        "destination": "MNL",
        "date": "2017-12-27",
        "maxStops": 1,
        "permittedCarrier": [
          "CX",
          "CZ",
          "KL",
          "MH",
          "QR",
          "SQ",
          "TK",
          "EK"
        ]
      },
      {
        "origin": "MNL",
        "destination": "AMS",
        "date": "2018-01-08",
        "maxStops": 1,
        "permittedCarrier": [
          "CX",
          "CZ",
          "KL",
          "MH",
          "QR",
          "SQ",
          "TK",
          "EK"
        ]
      }
    ],
    "passengers": {
      "adultCount": 2,
      "infantInLapCount": 0,
      "infantInSeatCount": 0,
      "childCount": 1,
      "seniorCount": 0
    },
    "solutions": 20,
    "refundable": False
  }
}

response = requests.post(url, data=json.dumps(params), headers=headers)
data = response.json()

with open(dir + 'dataGF.json', 'w') as outfile:
    json.dump(data, outfile)
