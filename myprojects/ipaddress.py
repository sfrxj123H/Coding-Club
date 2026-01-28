import requests
def get_location_from_ip(ip_address):
    try:
        url = f"https://ipapi.co/{ip_address}/json/"

        # Send GET request to the API
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes (4XX or 5XX)

        # Parse the JSON response
        location_data = response.json()

        # Extract relevant information
        if location_data.get("error"):
            return f"Error: {location_data.get('reason')}"

        city = location_data.get("city")
        region = location_data.get("region")
        country = location_data.get("country_name")
        latitude = location_data.get("latitude")
        longitude = location_data.get("longitude")

        return {
            "ip": ip_address,
            "city": city,
            "region": region,
            "country": country,
            "latitude": latitude,
            "longitude": longitude
        }

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

target_ip = "37.19.205.250"
location = get_location_from_ip(target_ip)
print(location)