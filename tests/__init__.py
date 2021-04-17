import application
import json
import os


def get_response_data(route):
    os.environ['FLASK_ENV'] = 'development'
    with application.app.test_client() as client:
        response = client.get(route)
    return response.get_data(as_text=True)


def get_response_json(route):
    data = get_response_data(route)
    return json.loads(data)
