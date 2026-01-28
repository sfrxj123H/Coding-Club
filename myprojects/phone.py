import folium
import phonenumbers
import opencage
from phonenumbers import geocoder
number = input("Enter phone number with country code: ")
apiKey = "21fa49f87c2841fdbf2f9613965ebcc3"
# Example number:
# number = "+84333833632"
print("Processing...")

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
#print(location)
print("Country found.")

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
#print(carrier.name_for_number(service_pro, "en"))
print("Service provider found.")

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(apiKey)
query = str(location)
results = geocoder.geocode(query)
print("Geocoding completed.")
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
timezone = results[0]['annotations']['timezone']['name']
currency_name = results[0]['annotations']['currency']['name']
currency_symbol = results[0]['annotations']['currency']['symbol']
flag = results[0]['annotations']['flag']
print("Results:")
print("Country:", location)
print("Service Provider:", carrier.name_for_number(service_pro, "en"))
print("Time-Zone : ",timezone)
print("Currency : ",currency_name)
print("Symbol : ",currency_symbol)
print("latitude: ",lat)
print("longitude: ",lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation4.html")