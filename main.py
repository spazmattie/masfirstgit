import sys

from flask import Flask
import matplotlib
import pandas as pd
import requests

print(sys.executable)
# print(sys.version)

r = requests.get("https://www.google.com/")

print(r.status_code)

for i in range(5):
    print("ok")