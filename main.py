import sys

import flask
import matplotlib
import pandas as pd
import requests

print(sys.executable)
# print(sys.version)

r = requests.get("https://www.google.com/")

print(r.status_code)

print("LMAO")