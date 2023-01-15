import requests
from datetime import datetime as dt
from dotenv import load_dotenv
import os

GENDER = 'male'
WEIGHT_KG = 53.4
HEIGHT_CM = 1.75
AGE = 24
BEARER_TOKEN = os.environ.get('SHEET_BEARER_TOKEN')

APP_ID = os.environ.get('NT_APP_ID')
API_KEY = os.environ.get('NT_API_KEY')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input('Tell me which exercises you did: ')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

data = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

exercise_response = requests.post(exercise_endpoint, json=data, headers=headers)
exercise_data = exercise_response.json()

today_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")

sheet_headers = {
    'Authorization': f'Basic {BEARER_TOKEN}'
}

for exercise in exercise_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheety_endpoint = os.environ.get('SHEET_ENDPOINT')

sheety_response = requests.post(sheety_endpoint, json=sheet_inputs, headers= sheet_headers)
sheety_response.raise_for_status()
