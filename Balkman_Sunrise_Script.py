import requests

url = "https://api.sunrise-sunset.org/v2?lat=36.7201600&lng=-4.4203400"
headers = {
    "Accept": "application/json",
    "Authorization": "******"
}

response = requests.get(url, headers=headers)
data = response.json()

#prints the following times for your current latitude & longitude for today's date
for field in ("lat", "lng", "sunrise", "sunset", "dawn", "dusk", "golden_hour", "blue_hour"):
    print(f"{field}: {data.get(field, 'not found')}")
