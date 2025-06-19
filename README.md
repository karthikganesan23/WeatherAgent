🌤️ Rasa Weather Chatbot
This is a simple chatbot built using Rasa that can tell the current weather in any city. The bot understands user input like:

“What’s the weather in Chennai?”

and responds with real-time weather details such as temperature and wind speed.

🔧 How it Works
The user types a message asking about the weather in a specific city.

The chatbot extracts the city name using natural language understanding (NLU).

The bot uses OpenStreetMap (Nominatim) to convert the city name to latitude and longitude.

It then uses the Open-Meteo API to get the current weather data for that location.

The bot replies with the weather conditions including temperature and wind speed.

🧠 Technologies Used
Rasa (for chatbot framework)

OpenStreetMap Nominatim API (for location geocoding)

Open-Meteo API (for weather data)

Python

This chatbot can be run locally in a terminal or connected to a frontend UI.
