import json
from playwright.sync_api import APIRequestContext


class Base:
    def __init__(self, api_request_context: APIRequestContext):
        self._api = api_request_context

    def create_token(self, username: str, password: str):
        payload = {"username": username, "password": password}
        return self._api.post(
            "/auth",
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )

    def create_booking(self, firstname: str, lastname: str, totalprice: int, depositpaid: bool,
                       checkin: str, checkout: str, additionalneeds: str):
        payload = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }
        return self._api.post(
            "/booking",
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )

    def get_booking(self, booking_id: int):
        return self._api.get(f"/booking/{booking_id}")

    def delete_booking(self, booking_id: int, token: str):
        return self._api.delete(
            f"/booking/{booking_id}",
            headers={"Cookie": f"token={token}"}
        )