import requests
import logging

from app.models import User

API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_users() -> list[User]:
    try:
        response = requests.get(API_URL, timeout=5)

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            raise ValueError("Invalid API response format")

        return data

    except requests.Timeout:
        logging.warning("Request timed out")
        return []

    except requests.ConnectionError:
        logging.error("Connection error")
        return []

    except requests.HTTPError as error:
        logging.error(f"HTTP error: {error}")
        return []

    except ValueError as error:
        logging.error(f"Invalid JSON data: {error}")
        return []

    except requests.RequestException as error:
        logging.error(f"Unexpected request error: {error}")
        return []