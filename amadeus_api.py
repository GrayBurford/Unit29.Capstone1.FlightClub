from amadeus import Client, ResponseError

# Cheat Sheet:
# https://possible-quilt-2ff.notion.site/Cheat-sheet-e059caf4fcd342b78705f9f3d6f88f1d
API_BASE_URL = "https://test.api.amadeus.com"
API_KEY = "gW89o76UnCoZqBPWxvo6yLPhNqfQaGtf"
API_SECRET = "RUaGyaznry7uGL5E"
API_ACCESS_TOKEN = ""

# Obtain 30 minute access token
#     response = requests.post(f'{API_BASE_URL}/v1/security/oauth2/token',
#                         headers = {"Content-Type" : "application/x-www-form-urlencoded"},
#                         data = f"grant_type=client_credentials&client_id={API_KEY}&client_secret={API_SECRET}"
#                         )

#     API_ACCESS_TOKEN = response.json()["access_token"]
#     print(response.json()["access_token"])
#     TOKEN_EXPIRATION = response.json()["expires_in"]

amadeus = Client(
    client_id = API_KEY,
    client_secret = API_SECRET
)

@app.route('/', methods=["GET"])
def home_page():
    """Display anon landing page."""

    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode='EWR',
            destinationLocationCode='ATL',
            departureDate='2022-10-14',
            adults=1,
            max=5,
            travelClass='ECONOMY',
            currencyCode='USD'
            # includedAirlineCodes='UA'
            # nonStop=True DOES NOT WORK!!!
            # SPIRIT FLIGHT TIMES ARE WRONG
        )
        print(response.data)
    except ResponseError as error:
        print(error)

    flash("Welcome to the home page", "primary")
    return render_template('base.html', response=response)
    

# *******************************************
# EXAMPLE JSON RESPONSE FROM FLIGHT OFFERS SEARCH:

# {
#   "meta": {
#     "count": 2,
#     "links": {
#       "self": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=EWR&destinationLocationCode=SEA&departureDate=2022-10-14&adults=1&travelClass=ECONOMY&nonStop=true&max=2"
#     }
#   },
#   "data": [
#     {
#       "type": "flight-offer",
#       "id": "1",
#       "source": "GDS",
#       "instantTicketingRequired": false,
#       "nonHomogeneous": false,
#       "oneWay": false,
#       "lastTicketingDate": "2022-10-04",
#       "numberOfBookableSeats": 7,
#       "itineraries": [
#         {
#           "duration": "PT6H19M",
#           "segments": [
#             {
#               "departure": {
#                 "iataCode": "EWR",
#                 "terminal": "B",
#                 "at": "2022-10-14T17:45:00"
#               },
#               "arrival": {
#                 "iataCode": "SEA",
#                 "at": "2022-10-14T21:04:00"
#               },
#               "carrierCode": "AS",
#               "number": "15",
#               "aircraft": {
#                 "code": "7M9"
#               },
#               "operating": {
#                 "carrierCode": "AS"
#               },
#               "duration": "PT6H19M",
#               "id": "1",
#               "numberOfStops": 0,
#               "blacklistedInEU": false
#             }
#           ]
#         }
#       ],
#       "price": {
#         "currency": "EUR",
#         "total": "238.46",
#         "base": "208.00",
#         "fees": [
#           {
#             "amount": "0.00",
#             "type": "SUPPLIER"
#           },
#           {
#             "amount": "0.00",
#             "type": "TICKETING"
#           }
#         ],
#         "grandTotal": "238.46"
#       },
#       "pricingOptions": {
#         "fareType": [
#           "PUBLISHED"
#         ],
#         "includedCheckedBagsOnly": false
#       },
#       "validatingAirlineCodes": [
#         "AS"
#       ],
#       "travelerPricings": [
#         {
#           "travelerId": "1",
#           "fareOption": "STANDARD",
#           "travelerType": "ADULT",
#           "price": {
#             "currency": "EUR",
#             "total": "238.46",
#             "base": "208.00"
#           },
#           "fareDetailsBySegment": [
#             {
#               "segmentId": "1",
#               "cabin": "ECONOMY",
#               "fareBasis": "NH7OAVBN",
#               "brandedFare": "SV",
#               "class": "X",
#               "includedCheckedBags": {
#                 "quantity": 0
#               }
#             }
#           ]
#         }
#       ]
#     },
#     {
#       "type": "flight-offer",
#       "id": "2",
#       "source": "GDS",
#       "instantTicketingRequired": false,
#       "nonHomogeneous": false,
#       "oneWay": false,
#       "lastTicketingDate": "2022-10-04",
#       "numberOfBookableSeats": 7,
#       "itineraries": [
#         {
#           "duration": "PT6H19M",
#           "segments": [
#             {
#               "departure": {
#                 "iataCode": "EWR",
#                 "terminal": "B",
#                 "at": "2022-10-14T19:09:00"
#               },
#               "arrival": {
#                 "iataCode": "SEA",
#                 "at": "2022-10-14T22:28:00"
#               },
#               "carrierCode": "AS",
#               "number": "715",
#               "aircraft": {
#                 "code": "7M9"
#               },
#               "operating": {
#                 "carrierCode": "AS"
#               },
#               "duration": "PT6H19M",
#               "id": "2",
#               "numberOfStops": 0,
#               "blacklistedInEU": false
#             }
#           ]
#         }
#       ],
#       "price": {
#         "currency": "EUR",
#         "total": "238.46",
#         "base": "208.00",
#         "fees": [
#           {
#             "amount": "0.00",
#             "type": "SUPPLIER"
#           },
#           {
#             "amount": "0.00",
#             "type": "TICKETING"
#           }
#         ],
#         "grandTotal": "238.46"
#       },
#       "pricingOptions": {
#         "fareType": [
#           "PUBLISHED"
#         ],
#         "includedCheckedBagsOnly": false
#       },
#       "validatingAirlineCodes": [
#         "AS"
#       ],
#       "travelerPricings": [
#         {
#           "travelerId": "1",
#           "fareOption": "STANDARD",
#           "travelerType": "ADULT",
#           "price": {
#             "currency": "EUR",
#             "total": "238.46",
#             "base": "208.00"
#           },
#           "fareDetailsBySegment": [
#             {
#               "segmentId": "2",
#               "cabin": "ECONOMY",
#               "fareBasis": "NH7OAVBN",
#               "brandedFare": "SV",
#               "class": "X",
#               "includedCheckedBags": {
#                 "quantity": 0
#               }
#             }
#           ]
#         }
#       ]
#     }
#   ],
#   "dictionaries": {
#     "locations": {
#       "EWR": {
#         "cityCode": "NYC",
#         "countryCode": "US"
#       },
#       "SEA": {
#         "cityCode": "SEA",
#         "countryCode": "US"
#       }
#     },
#     "aircraft": {
#       "7M9": "BOEING 737 MAX 9"
#     },
#     "currencies": {
#       "EUR": "EURO"
#     },
#     "carriers": {
#       "AS": "ALASKA AIRLINES"
#     }
#   }
# }