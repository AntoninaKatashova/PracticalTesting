import pytest
from utils.schemas import assert_json_schema, auth_response_schema

class TestTokenParametrized:
    valid_token_data = [
        {
            "username": "admin",
            "password": "password123"
        },
    ]

    invalid_token_data = [
        (
            {"username": "admin"},
            200
        ),
        (
            {"password": "password123"},
            200
        ),
        (
            {"username": 123, "password": "password123"},
            200
        ),
        (
            {"username": "admin", "password": 123},
            200
        ),
        (
            {},
            200
        ),
    ]

    @pytest.mark.parametrize("token_data", valid_token_data)
    def test_create_token_valid(self, client, token_data):
        response = client.create_token(token_data)
        if not response.ok:
            print(f"Request Data: {token_data}")
            print(f"Response Status: {response.status}")
            try:
                print(f"Response Body: {response.text()}")
            except Exception:
                print("Failed to get response text.")
        assert response.ok, f"Expected ok response, got {response.status}"

        json_data = response.json()
        assert_json_schema(json_data, auth_response_schema)

        assert "token" in json_data, "Token not found in response"
        assert isinstance(json_data["token"], str), "Token should be a string"

    @pytest.mark.parametrize("token_data, expected_status", invalid_token_data)
    def test_create_token_invalid(self, client, token_data, expected_status):
        response = client.create_token(token_data)
        if response.status != expected_status:
            print(f"Request Data: {token_data}")
            print(f"Response Status: {response.status}")
            try:
                print(f"Response Body: {response.text()}")
            except Exception:
                print("Failed to get response text.")
        assert response.status == expected_status, f"Expected {expected_status}, got {response.status}"

        try:
            response_json = response.json()
        except ValueError:
            response_json = {}

        assert "reason" in response_json, "Expected 'reason' field in response"
        assert response_json["reason"] == "Bad credentials", "Expected 'Bad credentials' message"
