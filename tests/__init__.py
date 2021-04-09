import application
import json


def get_response_data(route):
    with application.app.test_client() as client:
        response = client.get(route)
    return json.loads(response.get_data(as_text=True))
