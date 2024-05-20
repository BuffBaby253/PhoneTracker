# Author: BuffBaby253
# Title: PhoneTracker
# Description: Phone Number Geolocater

import phonenumbers
import opencage
import folium
from phonenumber import number

from phonenumbers import geocoder

# Displays state of location
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

# Displays phone carrier
from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

# Import your API key from opencagedata.com
key = 'YOUR.API.KEY.FROM.opencagedata.com'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

# Displays longitude and latitude
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

# Creates an HTML file that displays a map view of the location
myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
