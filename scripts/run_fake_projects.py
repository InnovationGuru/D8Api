from d8a_client import config, auth, api
import json


def load_fake_projects(path="fake_telecom_projects.json"):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    creds = config.load_credentials()
    login_response = auth.login(creds['email'], creds['password'])
    api_token = login_response['token']
    x_company = creds['X_COMPANY']

    client = api.D8AClient(api_token, x_company)
    projects = load_fake_projects()

    form_name = "demo"
    form_id = client.get_form_id_by_name(form_name)
    for project in projects:
        created = client.create_project(project['Project Name'], project['Latitude'], project['Longitude'], form_id)
        print(f"Created project: {created['id']}")


if __name__ == "__main__":
    main()
