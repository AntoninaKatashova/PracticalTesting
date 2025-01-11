import pytest
import uuid
from utils.schemas import assert_json_schema, create_booking_response_schema

class TestBookingParametrized:
    valid_booking_data = [
        {
            "firstname": f"John_{uuid.uuid4()}",
            "lastname": f"Doe_{uuid.uuid4()}",
            "totalprice": 150,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-05"
            },
            "additionalneeds": "Breakfast"
        },
        {
            "firstname": f"Анна_{uuid.uuid4()}",
            "lastname": f"Иванова_{uuid.uuid4()}",
            "totalprice": 200,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2024-02-10",
                "checkout": "2024-02-15"
            },
            "additionalneeds": "Lunch"
        },
    ]

    invalid_booking_data = [
        (
            {
                "lastname": "Doe",
                "totalprice": 150,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2024-01-01",
                    "checkout": "2024-01-05"
                }
            },
            500
        ),
        (
            {
                "firstname": "John",
                "totalprice": 150,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2024-01-01",
                    "checkout": "2024-01-05"
                }
            },
            500
        ),
        (
            {
                "firstname": "John",
                "lastname": "Doe",
                "totalprice": "one hundred fifty",
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2024-01-01",
                    "checkout": "2024-01-05"
                }
            },
            200
        ),
        (
            {
                "firstname": "John",
                "lastname": "Doe",
                "totalprice": 150,
                "depositpaid": "yes",
                "bookingdates": {
                    "checkin": "2024-01-01",
                    "checkout": "2024-01-05"
                }
            },
            200
        ),
        (
            {
                "firstname": "John",
                "lastname": "Doe",
                "totalprice": 150,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "01-01-2024",
                    "checkout": "05-01-2024"
                }
            },
            200
        ),
        (
            {},
            500
        ),
    ]

    @pytest.mark.parametrize("booking_data", valid_booking_data)
    def test_create_booking_valid(self, client, token, booking_data):
        create_resp = client.create_booking(booking_data)
        assert create_resp.ok, f"Expected ok response for create booking, got {create_resp.status}"

        create_json = create_resp.json()
        assert_json_schema(create_json, create_booking_response_schema)

        booking_id = create_json.get("bookingid")
        assert booking_id is not None, "Booking ID should be present in the response"

        booking = create_json.get("booking", {})
        assert booking.get("firstname") == booking_data["firstname"], "Firstname does not match"
        assert booking.get("lastname") == booking_data["lastname"], "Lastname does not match"
        assert booking.get("totalprice") == booking_data["totalprice"], "Totalprice does not match"
        assert booking.get("depositpaid") == booking_data["depositpaid"], "Depositpaid does not match"
        assert booking.get("bookingdates", {}).get("checkin") == booking_data["bookingdates"]["checkin"], "Checkin date does not match"
        assert booking.get("bookingdates", {}).get("checkout") == booking_data["bookingdates"]["checkout"], "Checkout date does not match"
        assert booking.get("additionalneeds") == booking_data["additionalneeds"], "Additional needs do not match"

        delete_resp = client.delete_booking(booking_id, token)
        assert delete_resp.status == 201, f"Expected 201 on delete booking, got {delete_resp.status}"

        get_resp = client.get_booking(booking_id)
        assert get_resp.status == 404, f"Expected 404 after deletion, got {get_resp.status}"

    @pytest.mark.parametrize("booking_data, expected_status", invalid_booking_data)
    def test_create_booking_invalid(self, client, token, booking_data, expected_status):
        create_resp = client.create_booking(booking_data)
        if create_resp.status != expected_status:
            print(f"Request Data: {booking_data}")
            print(f"Response Status: {create_resp.status}")
            try:
                print(f"Response Body: {create_resp.text()}")
            except Exception:
                print("Failed to get response text.")

        assert create_resp.status == expected_status, f"Expected {expected_status}, got {create_resp.status}"

        try:
            response_json = create_resp.json()
        except ValueError:
            response_json = {}

        if "totalprice" in booking_data and isinstance(booking_data["totalprice"], str):
            assert response_json.get("booking", {}).get("totalprice") is None, "Totalprice should be null for invalid type"
        if "depositpaid" in booking_data and isinstance(booking_data["depositpaid"], str):
            assert isinstance(response_json.get("booking", {}).get("depositpaid"), bool), "Depositpaid should be boolean"
        if "firstname" not in booking_data:
            assert "firstname" not in response_json.get("booking", {}) or response_json["booking"].get("firstname") is None, "Firstname should be null or absent"
        if "lastname" not in booking_data:
            assert "lastname" not in response_json.get("booking", {}) or response_json["booking"].get("lastname") is None, "Lastname should be null or absent"
