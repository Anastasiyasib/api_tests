import requests
import pytest


from api import get_bookings


@pytest.mark.smoke
@pytest.mark.parametrize("lastname", ["Brown", "Black", "White"])
def test_123(lastname):
    """Тест проверяет получение броней"""
    response = get_bookings(lastname)
    expected_status_code = 200
    assert response.status_code == expected_status_code, f"We are waiting for {expected_status_code}"
    response_json = response.json()
    print(response_json)
# собрать 2 способами айди (циклом и list comprehension)

@pytest.mark.extra
def test_124():
    response = requests.put('https://restful-booker.herokuapp.com/booking/:id', data={"firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"})
    print(response)

