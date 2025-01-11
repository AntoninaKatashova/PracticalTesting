from playwright.sync_api import APIRequestContext
import json

class Base:
    def __init__(self, api_request_context: APIRequestContext):
        self._api = api_request_context

    def create_token(self, payload: dict):
        return self._api.post(
            "/auth",
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )

    def create_booking(self, payload: dict):
        return self._api.post(
            "/booking",
            data=json.dumps(payload),  # Отправляем сериализованный JSON
            headers={"Content-Type": "application/json"}
        )

    def get_booking(self, booking_id: int):
        return self._api.get(f"/booking/{booking_id}")

    def delete_booking(self, booking_id: int, token: str):
        return self._api.delete(
            f"/booking/{booking_id}",
            headers={"Cookie": f"token={token}"}
        )
