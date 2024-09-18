import requests

def load_api_data():
    url = "YOUR_API_URL"
    response = requests.get(url)
    return response.json()  # Assuming the API returns JSON data
