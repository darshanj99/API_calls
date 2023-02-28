import requests 
import pprint
import json
import os
from dotenv import load_dotenv
load_dotenv()
access_token = os.getenv('access_token')
response = requests.get("https://globalmart-api.onrender.com/mentorskool/v1/sales", 
headers={"access_token": access_token},).json()
pprint.pprint(response["data"])
