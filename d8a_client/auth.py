"""
Authentication module for the D8Acapture API client.

This module handles login and returns the authentication token needed
for accessing other API endpoints.
"""

import requests
import json

LOGIN_URL = 'https://d8acapture.com/api/login'


def login(email, password):
    """
    Authenticate with the D8Acapture API using an email and password.

    Args:
        email (str): The user's email address.
        password (str): The user's password.

    Returns:
        dict: A JSON response containing user information and the API token.

    Raises:
        requests.HTTPError: If authentication fails or the server returns an error.
    """
    data = {
        "email": email,
        "password": password,
        "device": "Python Client"
    }
    headers = {'Content-type': 'application/json'}
    response = requests.post(LOGIN_URL, data=json.dumps(data), headers=headers)
    response.raise_for_status()
    return response.json()
