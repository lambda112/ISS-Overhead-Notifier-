import requests 
import datetime as dt

# import pandas as pd

# response = requests.get(url = "http://api.open-notify.org/iss-now.json") # Get data that we want
# response.raise_for_status() # if not 200 raise exception

# data = response.json()
# pos = data["iss_position"]

# print(data)

MY_LAT = 53.537876
MY_LONG = -2.092638

response = requests.get("https://api.sunrise-sunset.org/json", params=({"lat":MY_LAT, "lng":MY_LONG, "formatted":0}))
response.raise_for_status()
response = response.json()

sunrise = int(response["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(response["results"]["sunset"].split("T")[1].split(":")[0])

print(sunset, sunrise)
print(dt.datetime.now().hour)