import random
from unittest.mock import patch

import requests


def get_random_number():
    return random.randint(0, 10)


@patch("random.randint")
def test_get_random_number(mock_random):
    mock_random.return_value = 6
    assert get_random_number() == 6
    mock_random.assert_called_once_with(0, 10)


def get_github_user_info(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    return response.json()


@patch("requests.get")
def test_github_user_info(mock_get):
    mock_get.return_value.json.return_value = {"login": "kolya", "name": "Kolya Gendin"}
    assert get_github_user_info("kolya") == {"login": "kolya", "name": "Kolya Gendin"}
    mock_get.assert_called_once_with("https://api.github.com/users/kolya")
