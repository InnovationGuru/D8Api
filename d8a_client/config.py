"""
Configuration module for D8Acapture API tools.

Handles loading credentials and other environment-based settings
from a `.env` file using python-dotenv.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file at module import time
load_dotenv()

def get_credentials():
    """
    Retrieve API credentials and company ID from environment variables.

    Returns:
        dict: A dictionary containing:
            - 'email' (str): The login email address.
            - 'password' (str): The login password.
            - 'x_company' (str): The company UUID used for requests.

    Raises:
        ValueError: If any required environment variables are missing.
    """
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    x_company = os.getenv("X_COMPANY")

    if not all([email, password, x_company]):
        raise ValueError("Missing one or more required environment variables: EMAIL, PASSWORD, X_COMPANY")

    return {
        'email': email,
        'password': password,
        'x_company': x_company,
    }
