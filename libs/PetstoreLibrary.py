import requests
from requests import Response
import json


class PetstoreLibrary:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    BASE_URL = "https://petstore.swagger.io/v2"
    _last_response = None
    _last_json = None

    def __init__(self):
        self.created_entities = []

    # Response management methods
    def _store_response(self, response: Response):
        self._last_response = response
        try:
            self._last_json = response.json()
        except:
            self._last_json = None

    def get_last_response(self) -> Response:
        return self._last_response

    def get_last_json(self):
        return self._last_json

    def should_be_status(self, expected_status: int):
        actual_status = self._last_response.status_code
        if actual_status != expected_status:
            raise AssertionError(f"Expected status {expected_status}, but got {actual_status}")

    # User methods
    def create_user(self, payload: dict) -> Response:
        response = requests.post(f"{self.BASE_URL}/user", json=payload)
        self._store_response(response)
        if response.status_code == 200:
            self.created_entities.append(('user', payload['username']))
        return response

    def get_user(self, username: str) -> Response:
        response = requests.get(f"{self.BASE_URL}/user/{username}")
        self._store_response(response)
        return response

    def login_user(self, username: str, password: str) -> Response:
        response = requests.get(
            f"{self.BASE_URL}/user/login",
            params={"username": username, "password": password},
        )
        self._store_response(response)
        return response

    def logout_user(self) -> Response:
        response = requests.get(f"{self.BASE_URL}/user/logout")
        self._store_response(response)
        return response

    def update_user(self, username: str, payload: dict) -> Response:
        response = requests.put(f"{self.BASE_URL}/user/{username}", json=payload)
        self._store_response(response)
        return response

    def delete_user(self, username: str) -> Response:
        response = requests.delete(f"{self.BASE_URL}/user/{username}")
        self._store_response(response)
        return response

    # Pet methods
    def create_pet(self, payload: dict) -> Response:
        response = requests.post(f"{self.BASE_URL}/pet", json=payload)
        self._store_response(response)
        if response.status_code == 200:
            self.created_entities.append(('pet', payload['id']))
        return response

    def get_pet(self, pet_id: int) -> Response:
        response = requests.get(f"{self.BASE_URL}/pet/{pet_id}")
        self._store_response(response)
        return response

    def find_pets_by_status(self, status: str) -> Response:
        response = requests.get(f"{self.BASE_URL}/pet/findByStatus", params={"status": status})
        self._store_response(response)
        return response

    def delete_pet(self, pet_id: int) -> Response:
        response = requests.delete(f"{self.BASE_URL}/pet/{pet_id}")
        self._store_response(response)
        return response

    # Cleanup method
    def cleanup_created(self):
        for entity_type, identifier in self.created_entities:
            try:
                if entity_type == 'user':
                    self.delete_user(identifier)
                elif entity_type == 'pet':
                    self.delete_pet(identifier)
            except:
                pass  # Ignore cleanup errors
        self.created_entities = []