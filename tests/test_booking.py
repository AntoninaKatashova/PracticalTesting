from utils.schemas import assert_json_schema, create_booking_response_schema


class TestBooking:
    def test_create_and_delete_booking(self, client, token):
        firstname = "John"
        lastname = "Doe"
        totalprice = 150
        depositpaid = True
        checkin = "2024-01-01"
        checkout = "2024-01-05"
        additionalneeds = "Breakfast"

        create_resp = client.create_booking(firstname, lastname, totalprice, depositpaid, checkin, checkout,
                                            additionalneeds)

        assert create_resp.ok, f"Expected ok response for create booking, got {create_resp.status}"

        create_json = create_resp.json()

        assert_json_schema(create_json, create_booking_response_schema)

        booking_id = create_json["bookingid"]

        booking_data = create_json["booking"]
        assert booking_data["firstname"] == firstname
        assert booking_data["lastname"] == lastname
        assert booking_data["totalprice"] == totalprice
        assert booking_data["depositpaid"] == depositpaid
        assert booking_data["bookingdates"]["checkin"] == checkin
        assert booking_data["bookingdates"]["checkout"] == checkout
        assert booking_data["additionalneeds"] == additionalneeds

        delete_resp = client.delete_booking(booking_id, token)
        assert delete_resp.status == 201, f"Expected 201 on delete booking, got {delete_resp.status}"

        get_resp = client.get_booking(booking_id)
        assert get_resp.status == 404, f"Expected 404 after deletion, got {get_resp.status}"