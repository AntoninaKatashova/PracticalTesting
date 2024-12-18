from jsonschema import validate

auth_response_schema = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}

create_booking_response_schema = {
    "type": "object",
    "properties": {
        "bookingid": {"type": "integer"},
        "booking": {
            "type": "object",
            "properties": {
                "firstname": {"type": "string"},
                "lastname": {"type": "string"},
                "totalprice": {"type": "integer"},
                "depositpaid": {"type": "boolean"},
                "bookingdates": {
                    "type": "object",
                    "properties": {
                        "checkin": {"type": "string"},
                        "checkout": {"type": "string"}
                    },
                    "required": ["checkin", "checkout"]
                },
                "additionalneeds": {"type": "string"}
            },
            "required": ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"]
        }
    },
    "required": ["bookingid", "booking"]
}


def assert_json_schema(instance, schema):
    validate(instance=instance, schema=schema)