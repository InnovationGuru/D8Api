import json
from d8a_client import api, auth, config

PROJECT_ID = "Enter a project name"
OUTPUT_FILE = "../example_poles.json"

def main():
    # Load credentials from .env
    creds = config.get_credentials()

    # Authenticate
    login_response = auth.login(creds['email'], creds['password'])
    api_token = login_response['token']

    # Init API client
    client = api.D8AClient(api_token, creds['x_company'])

    # Fetch project details
    url = f"https://d8acapture.com/api/project/{PROJECT_ID}"
    response = client.session.get(url, headers=client.headers)
    response.raise_for_status()

    project_data = response.json()
    poles = project_data.get("poles", [])

    # Extract name, lat, lng
    output = []
    for pole in poles:
        output.append({
            "name": pole.get("name"),
            "lat": pole.get("lat"),
            "lng": pole.get("lng")
        })

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Exported {len(output)} poles to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
