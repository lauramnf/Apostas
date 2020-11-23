import requests
import re

#Download page
response = requests.get(url)
response.raise_for_status() #if error it will stop the program
