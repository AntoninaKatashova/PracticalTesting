from utils.schemas import assert_json_schema, auth_response_schema

class TestToken:
    def test_create_token(self, client):
        payload = {
            "username": "admin",
            "password": "password123"
        }

        response = client.create_token(payload)
        assert response.ok, f"Expected ok response, got {response.status}"

        json_data = response.json()
        assert_json_schema(json_data, auth_response_schema)

        assert "token" in json_data, "Token not found in response"
        assert isinstance(json_data["token"], str), "Token should be a string"
