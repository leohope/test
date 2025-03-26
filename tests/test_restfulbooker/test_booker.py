import pytest
import requests
import random

BASE_URL = "https://restful-booker.herokuapp.com"


def test_get_booking():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    booking_ids = response.json()

    random_booking = random.choice(booking_ids)["bookingid"]

    booking_response = requests.get(f"{BASE_URL}/booking/{random_booking}")
    assert booking_response.status_code == 200

    booking_data = booking_response.json()

    assert "firstname" in booking_data
    assert "lastname" in booking_data
    assert "totalprice" in booking_data
