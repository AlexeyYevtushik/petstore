import requests
from requests import Response


class PetstoreLibrary:

    BASE_URL = "https://petstore.swagger.io/v2"

    def create_user(self, payload: dict) -> Response:
        return requests.post(f"{self.BASE_URL}/user", json=payload)

    def get_user(self, username: str) -> Response:
        return requests.get(f"{self.BASE_URL}/user/{username}")

    def login_user(self, username: str, password: str) -> Response:
        return requests.get(
            f"{self.BASE_URL}/user/login",
            params={"username": username, "password": password},
        )

    def update_user(self, username: str, payload: dict) -> Response:
        return requests.put(f"{self.BASE_URL}/user/{username}", json=payload)

    def delete_user(self, username: str) -> Response:
        return requests.delete(f"{self.BASE_URL}/user/{username}")

    def create_pet(self, payload: dict) -> Response:
        return requests.post(f"{self.BASE_URL}/pet", json=payload)

    def get_pet_by_status(self, status: str) -> Response:
        return requests.get(f"{self.BASE_URL}/pet/findByStatus", params={"status": status})

    def delete_pet(self, pet_id: int) -> Response:
        return requests.delete(f"{self.BASE_URL}/pet/{pet_id}")