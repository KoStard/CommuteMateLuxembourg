from api import MobiliteitLu
import json
import os
from dotenv import load_dotenv



if __name__ == "__main__":
    load_dotenv()  # load environment variables from .env file

    access_key = os.getenv("MOBILITEIT_API_KEY")

    # response = MobiliteitLu(access_key).get_nearby_stops(
    #     lat='49.626792',
    #     long='6.1264706',
    #     radius=1000
    #     # lat='49.6321032',
    #     # long='6.1345412'
    # )
    # print([(s['StopLocation']['id'], s['StopLocation']['name']) for s in response['stopLocationOrCoordLocation']])
    print(json.dumps(MobiliteitLu(access_key).get_departure_board('A=1@O=Eich, Eecher Plaz@X=6129933@Y=49627566@u=0@U=82@L=200410003@'), indent=4))
