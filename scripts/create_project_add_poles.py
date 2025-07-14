import json
from d8a_client import api, auth, config
from d8a_client.form_utils import build_pole_update_payload

# Update these:
FORM_NAME = "demo"
PROJECT_NAME = "Imported Poles"
POLE_FILE = "../example_poles.json"

def main():
    # Load credentials
    creds = config.get_credentials()

    # Authenticate
    login_response = auth.login(creds['email'], creds['password'])
    api_token = login_response['token']

    # Initialize client
    client = api.D8AClient(api_token, creds['x_company'])

    # Get form ID by name
    form_id = client.get_form_id_by_name(FORM_NAME)

    # Create new project (use lat/lng from first pole)
    with open(POLE_FILE, "r", encoding="utf-8") as f:
        poles = json.load(f)

    if not poles:
        print("No poles to import.")
        return

    first = poles[0]
    project = client.create_project(
        name=PROJECT_NAME,
        lat=first["lat"],
        lng=first["lng"],
        form_id=form_id
    )
    project_id = project["id"]
    print(f"Created project '{PROJECT_NAME}' with ID: {project_id}")

    # Get form definition once
    form = client.get_form(form_id)

    # Create and update poles
    for pole in poles:
        created = client.create_pole(project_id)
        updated_payload = build_pole_update_payload(form, pole["name"], pole["lat"], pole["lng"])
        client.update_pole(created["id"], updated_payload)
        print(f"Imported pole: {pole['name']}")

    print(f"Successfully imported {len(poles)} poles into project '{PROJECT_NAME}'.")

if __name__ == "__main__":
    main()
