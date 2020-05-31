#!/usr/bin/python -u
import sys
import requests
from DataFetcher import DataFetcher
from dotenv import load_dotenv

load_dotenv()


dataFet = DataFetcher()
dataFet.init()
dataFet.fetch()
