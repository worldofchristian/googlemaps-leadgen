import os
import requests
import json
import pickle

# Google Places API
api_key = ''

with open("cities.pickle", "rb") as file:
    imported_cities = pickle.load(file)

# Function to get places for a specific city
def get_places_for_city(city):
    # Search query
    query = f'bars and restaurants in {city}'

    # API request
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}'
    response = requests.get(url)

    # API response
    if response.status_code == 200:
        data = response.json()

        # Extract the names of places from the response
        results = data.get('results', [])
        place_names = [place['name'] for place in results]

        return place_names

    else:
        print(f'Error occurred while searching for {city}. Status code: {response.status_code}')
        return []

# Create a folder for city-place if it doesn't exist
if not os.path.exists("city-place"):
    os.makedirs("city-place")

# Iterate over each city
for city in imported_cities:
    # Get places for the city
    places = get_places_for_city(city)

    # Create a dictionary for the city
    city_data = {"city": city, "places": places}

    # Create a file for the city and write the JSON data
    filename = f"city-place/{city}.json"
    with open(filename, "w") as file:
        json.dump(city_data, file)

print("Files created successfully in the 'city-place' folder.")