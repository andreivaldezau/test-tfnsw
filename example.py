import requests
import json
import os
from dotenv import load_dotenv

import gtfs_realtime_1007_pb2
from train import Train

# from google.protobuf.json_format import MessageToDict, MessageToJson

load_dotenv()
API_KEY = os.getenv("TFNSW_API_KEY")

url = "https://api.transport.nsw.gov.au/v2/gtfs/vehiclepos/sydneytrains"
headers = {
    "accept": "application/x-google-protobuf",
    "Authorization": f"apikey {API_KEY}",
}

feed = gtfs_realtime_1007_pb2.FeedMessage()
response = requests.get(url, headers=headers)
if response.status_code == 200:
    feed.ParseFromString(response.content)
    trains = []
    for entity in feed.entity:
        train = Train(entity)
        trains.append(train)
