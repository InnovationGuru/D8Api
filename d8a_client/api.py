import requests
import json

BASE_URL = "https://d8acapture.com/api"


class D8AClient:
    """
    A client for interacting with the D8Acapture API.
    """

    def __init__(self, api_token, x_company=None):
        """
        Initialize the D8Acapture client.

        Args:
            api_token (str): The API token received after login.
            x_company (str, optional): The company UUID required for some endpoints.
        """
        self.api_token = api_token
        self.x_company = x_company
        self.headers = {
            'Content-type': 'application/json',
            'Cookie': f'api_token={self.api_token}'
        }
        if x_company:
            self.headers['x-company'] = x_company

        self.session = requests.Session()

    def get_forms(self):
        """
        Retrieve all form configurations available to the authenticated user.

        Returns:
            dict: JSON response containing all available forms.

        Raises:
            HTTPError: If the request fails.
        """
        url = f"{BASE_URL}/form-configuration?per_page=-1"
        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_form(self, form_id):
        """
        Retrieve a single form configuration by its ID.

        Args:
            form_id (str): The UUID of the form.

        Returns:
            dict: The full form object, including its fields.

        Raises:
            HTTPError: If the request fails.
        """
        url = f"{BASE_URL}/form-configuration/{form_id}"
        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_form_names(self):
        """
        List the names of all available forms.

        Returns:
            list[str]: A list of form names.
        """
        forms = self.get_forms()
        return [form.get('name') for form in forms]

    def get_form_id_by_name(self, name):
        """
        Get the form ID associated with a given form name (case-insensitive).

        Args:
            name (str): The name of the form to search for.

        Returns:
            str: The UUID of the form.

        Raises:
            ValueError: If no form matches the given name.
        """
        forms = self.get_forms()
        for form in forms:
            if form.get('name', '').lower() == name.lower():
                return form.get('id')
        raise ValueError(f"Form with name '{name}' not found.")

    def create_project(self, name, lat, lng, form_id):
        """
        Create a new project with the given details.

        Args:
            name (str): Project name.
            lat (float): Latitude of the project.
            lng (float): Longitude of the project.
            form_id (str): UUID of the form configuration to use.

        Returns:
            dict: JSON response containing the created project data.

        Raises:
            HTTPError: If the request fails.
        """
        url = f"{BASE_URL}/project"
        data = {
            "form_configuration_id": form_id,
            "name": name,
            "description": "",
            "status": "gathering",
            "lat": lat,
            "lng": lng,
            "reporters": [],
            "engineers": []
        }
        response = self.session.post(url, data=json.dumps(data), headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_pole(self, project_id):
        """
        Create a new pole associated with a given project.

        Args:
            project_id (str): The UUID of the project to associate the pole with.

        Returns:
            dict: JSON response containing the created pole data.

        Raises:
            HTTPError: If the request fails.
        """
        url = f"{BASE_URL}/pole"
        data = {"project_id": project_id}
        response = self.session.post(url, data=json.dumps(data), headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_pole(self, pole_id, payload):
        """
        Update an existing pole's metadata using a form-aligned payload.

        Args:
            pole_id (str): The UUID of the pole to update.
            payload (dict): The data payload to send (typically from form_utils).

        Returns:
            dict: JSON response containing the updated pole data.

        Raises:
            HTTPError: If the request fails.
        """
        url = f"{BASE_URL}/pole/{pole_id}"
        response = self.session.put(url, data=json.dumps(payload), headers=self.headers)
        response.raise_for_status()
        return response.json()
