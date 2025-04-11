import time
from constants import COINMARKET_KEY
from quixstreams import Application
from requests import Session
from  requests.exceptions import Timeout, TooManyRedirects
import json
from pprint import pprint

app=Application(
    broker_addres='localhost:9092',
    consumer_group='coinmarket_monitoring'
)