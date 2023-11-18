import requests

import requests
from typing import Any

from typing import List, Optional

class MobiliteitLu:
    BASE_URL_NEARBY_STOPS = 'https://cdt.hafas.de/opendata/apiserver/location.nearbystops'
    BASE_URL_DEPARTURE_BOARD = 'https://cdt.hafas.de/opendata/apiserver/departureBoard'


    def __init__(self, access_id):
        self.access_id = access_id

    def get_nearby_stops(self, lat, long, radius=500, max_no=10, lang='eng', **kwargs):
        """
        Gets nearby stops based on provided coordinates and other optional parameters.
        
        :param lat: Latitude of centre coordinate.
        :param long: Longitude of centre coordinate.
        :param radius: Search radius in meters around the given coordinate; defaults to 500.
        :param max_no: Maximum number of returned stops, ranging from 1 to 5000; defaults to 10.
        :param lang: Language of the journey planner; defaults to 'eng'.
        :param kwargs: Any other optional parameters defined in the API.
        :return: Response from the API as a JSON object.
        """
        fmt = 'json'
        params = {
            'accessId': self.access_id,
            'originCoordLat': lat,
            'originCoordLong': long,
            'r': radius,
            'maxNo': max_no,
            'lang': lang,
            'format': fmt,
        }
        params.update(kwargs)  # Add any other optional parameters
        response = requests.get(self.BASE_URL_NEARBY_STOPS, params=params)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    
    def get_departure_board(self, id: str, date: str = None, time: str = None, duration: int = 60, lang='eng'):
        """
        Fetches the departure board information for a specific station/stop.
        
        :param id: Specifies the station/stop ID for which the departures shall be retrieved.
        :param date: Sets the start date for which the departures shall be retrieved. Format: 'YYYY-MM-DD'; defaults to None.
        :param time: Sets the start time for which the departures shall be retrieved. Format: 'hh:mm'; defaults to None.
        :param duration: Sets the interval size in minutes for departures retrieval. Range: 0 to 1439; defaults to 60.
        :param lang: Language of the journey planner; defaults to 'eng'.
        :return: Response from the API as a JSON object.
        """

        params = {
            'accessId': self.access_id,
            'id': id,
            'date': date,
            'time': time,
            'duration': duration,
            'lang': lang,
            'format': 'json',
            'rtMode': 'FULL'
        }

        response = requests.get(self.BASE_URL_DEPARTURE_BOARD, params=params)
        response.raise_for_status()  # Check for HTTP errors
        api_response = response.json()
        return api_response
