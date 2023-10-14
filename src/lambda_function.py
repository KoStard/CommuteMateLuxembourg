from api import MobiliteitLu
import json
import os
from dotenv import load_dotenv



if __name__ == "__main__":
    load_dotenv()  # load environment variables from .env file

    access_key = os.getenv("ACCESS_KEY")

    response = MobiliteitLu(access_key).get_nearby_stops(
        lat='49.626792',
        long='6.1264706'
    )
    print([(s['StopLocation']['id'], s['StopLocation']['name']) for s in response['stopLocationOrCoordLocation']])
