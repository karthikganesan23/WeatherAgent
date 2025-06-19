import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionGetWeather(Action):
    def name(self):
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        location = next(tracker.get_latest_entity_values("location"), None)

        if not location:
            dispatcher.utter_message(text="Please specify the city or place.")
            return []

        # Step 1: Convert location name to lat/lon using Nominatim
        geo_url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json"
        headers = {"User-Agent": "rasa-weather-bot"}
        geo_response = requests.get(geo_url, headers=headers)
        geo_data = geo_response.json()

        if not geo_data:
            dispatcher.utter_message(text=f"Couldn't find coordinates for '{location}'.")
            return []

        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']

        # Step 2: Get weather from Open-Meteo
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current_weather=true"
        )
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        if "current_weather" in weather_data:
            current = weather_data["current_weather"]
            temp = current["temperature"]
            wind = current["windspeed"]

            response = (f"🌍 Weather in {location.title()}:\n"
                        f"🌡️ Temperature: {temp}°C\n"
                        f"💨 Wind Speed: {wind} km/h")
        else:
            response = "Couldn't fetch the weather right now."

        dispatcher.utter_message(text=response)
        return [SlotSet("location", location)]
