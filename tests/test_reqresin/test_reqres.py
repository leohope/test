import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.mark.parametrize("email, password, expected_status", [
    ("eve.holt@reqres.in", "cityslicka", 200),  # Верные данные
    ("eve.holt@reqres.in", "", 400),  # Неверный пароль
    ("", "cityslicka", 400)  # Пустой email
])
def test_login(email, password, expected_status):
    response = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password})

    assert response.status_code == expected_status

    if expected_status == 200:
        assert "token" in response.json(), "Токен отсутствует в ответе"
