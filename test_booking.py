from utils.schemas import assert_json_schema, create_booking_response_schema

class TestBooking:
    def test_create_and_delete_booking(self, client, token):
        payload = {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": 150,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-05"
            },
            "additionalneeds": "Breakfast"
        }

        create_resp = client.create_booking(payload)
        assert create_resp.ok, f"Expected ok response for create booking, got {create_resp.status}"

        create_json = create_resp.json()
        assert_json_schema(create_json, create_booking_response_schema)

        booking_id = create_json.get("bookingid")
        assert booking_id is not None, "Booking ID should be present in the response"

        booking_data = create_json.get("booking", {})
        assert booking_data.get("firstname") == payload["firstname"], "Firstname does not match"
        assert booking_data.get("lastname") == payload["lastname"], "Lastname does not match"
        assert booking_data.get("totalprice") == payload["totalprice"], "Totalprice does not match"
        assert booking_data.get("depositpaid") == payload["depositpaid"], "Depositpaid does not match"
        assert booking_data.get("bookingdates", {}).get("checkin") == payload["bookingdates"]["checkin"], "Checkin date does not match"
        assert booking_data.get("bookingdates", {}).get("checkout") == payload["bookingdates"]["checkout"], "Checkout date does not match"
        assert booking_data.get("additionalneeds") == payload["additionalneeds"], "Additional needs do not match"

        delete_resp = client.delete_booking(booking_id, token)
        assert delete_resp.status == 201, f"Expected 201 on delete booking, got {delete_resp.status}"

        get_resp = client.get_booking(booking_id)
        assert get_resp.status == 404, f"Expected 404 after deletion, got {get_resp.status}"
