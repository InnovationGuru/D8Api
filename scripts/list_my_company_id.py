from d8a_client import auth, config, api

def main():
    # Load credentials
    creds = config.get_credentials()

    # Authenticate
    login_response = auth.login(creds['email'], creds['password'])
    api_token = login_response['token']

    # Create API client (x_company not needed for this call)
    client = api.D8AClient(api_token)

    # Call /profile/roles
    url = "https://d8acapture.com/api/profile/roles"
    response = client.session.get(url, headers=client.headers)
    response.raise_for_status()

    data = response.json()

    # Print company names and IDs
    print("Available Companies:\n")
    for role in data:
        company = role.get("company", {})
        company_id = company.get("id")
        company_name = company.get("name")
        print(f"- {company_name} (ID: {company_id})")

if __name__ == "__main__":
    main()
