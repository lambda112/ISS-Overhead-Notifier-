import requests 
import datetime as dt
import smtplib

MY_LAT = 51.5123
MY_LONG = 0.0910

# Get ISS Position
response = requests.get(url = "http://api.open-notify.org/iss-now.json") # Get data that we want
response.raise_for_status() # if not 200 raise exception
data = response.json()

# ISS POSITION
iss_lat = float(data["iss_position"]["latitude"])
iss_lng = float(data["iss_position"]["longitude"])
iss_pos = (iss_lat, iss_lng)


# Get Sunrise and Sunset Times 
response = requests.get("https://api.sunrise-sunset.org/json", params=({"lat":MY_LAT, "lng":MY_LONG, "formatted":0}))
response.raise_for_status()
response = response.json()

# TIMES
sunrise = int(response["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(response["results"]["sunset"].split("T")[1].split(":")[0])


# Check to see if night
def check_times():
    is_night = False
    if dt.datetime.now().hour < sunrise or dt.datetime.now() > sunset:
        is_night = True
    else:
        is_night = False
    
    return is_night

# Check to see if overhead current location
def check_position():
    is_overhead = False
    if -6 < iss_lat - MY_LAT < 6 and -6 < iss_lng - MY_LONG < 6:
        is_overhead = True
    else:
        is_overhead = False

    return is_overhead

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="lambdaa112@gmail.com", password="moyn eugt kmga xrck")
        connection.sendmail(from_addr="lambdaa112@gmail.com", to_addrs="lambdaa112@gmail.com")