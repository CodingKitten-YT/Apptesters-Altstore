import requests
import json
from datetime import datetime

# Function to fetch and load the JSON from a URL
def fetch_json_from_url(url):
    response = requests.get(url)
    return response.json()

# Function to convert the input JSON to the desired format
def convert_json(input_json):
    output_json = {
        "name": input_json["name"],
        "subtitle": input_json["subtitle"],
        "description": f"Welcome to {input_json['name']}! Here you'll find all of our apps.",
        "iconURL": input_json["iconURL"],
        "headerURL": "",  # Adjust as needed
        "website": input_json["website"],
        "tintColor": "#4185A9",  # Customize this
        "featuredApps": [],
        "apps": [],
        "news": []  # Add news logic if needed
    }

    for app in input_json["apps"]:
        # Create a list of versions from the "fullDate"
        versions = [{
            "version": app["version"],
            "date": datetime.strptime(app["fullDate"], "%Y%m%d%H%M%S").isoformat(),
            "size": app["size"],
            "downloadURL": app["downloadURL"],
            "localizedDescription": app["localizedDescription"],
            "minOSVersion": "12.0"  # Customize as necessary
        }]

        output_json["apps"].append({
            "name": app["name"],
            "bundleIdentifier": app["bundleIdentifier"],
            "developerName": app["developerName"] if app["developerName"] else "Unknown Developer",
            "subtitle": app["localizedDescription"][:50],  # First 50 chars as subtitle
            "localizedDescription": app["localizedDescription"],
            "iconURL": app["iconURL"],
            "tintColor": "#5CA399",  # Customize per app if needed
            "screenshots": [],  # Add logic for screenshots if available
            "versions": versions,
            "appPermissions": {
                "entitlements": [],  # Add actual entitlements if available
                "privacy": {}  # Add actual privacy settings if available
            }
        })

    return output_json

# URL to fetch the JSON from
url = 'https://raw.githubusercontent.com/apptesters-org/Repo/main/apps.json'

# Fetch and convert JSON
input_json = fetch_json_from_url(url)
output_json = convert_json(input_json)

# Save the output JSON to a file
with open('output.json', 'w') as f:
    json.dump(output_json, f, indent=4)

print("Converted JSON has been saved to output.json")
