import time
import requests
from concurrent.futures import ThreadPoolExecutor


BASE_API_URL = "https://jsonplaceholder.typicode.com"


# 1. GET all users
def test_get_users():
    response = requests.get(
        f"{BASE_API_URL}/users",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


# 2. GET single user
def test_get_single_user():
    response = requests.get(
        f"{BASE_API_URL}/users/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert data["id"] == 1
    assert "name" in data
    assert "email" in data


# 3. POST - Create a new user
def test_create_user():
    payload = {
        "name": "Anamika",
        "username": "anamika",
        "email": "anamika@example.com"
    }

    response = requests.post(
        f"{BASE_API_URL}/users",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Anamika"
    assert data["username"] == "anamika"
    assert data["email"] == "anamika@example.com"


# 4. Negative test - User not found
def test_get_invalid_user():
    response = requests.get(
        f"{BASE_API_URL}/users/9999",
        timeout=10
    )

    assert response.status_code == 404


# 5. Performance / Concurrent API test
def test_concurrent_api_requests():

    def send_request(_):
        start_time = time.perf_counter()

        response = requests.get(
            f"{BASE_API_URL}/users",
            timeout=10
        )

        end_time = time.perf_counter()

        response_time = end_time - start_time

        return response, response_time

    start_total = time.perf_counter()

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(
            executor.map(send_request, range(5))
        )

    end_total = time.perf_counter()

    total_time = end_total - start_total

    responses = [result[0] for result in results]
    response_times = [result[1] for result in results]

    assert len(responses) == 5

    for response in responses:
        assert response.status_code == 200

    average_response_time = sum(response_times) / len(response_times)

    print("\n5 concurrent requests completed")
    print(f"Average response time: {average_response_time:.3f} seconds")
    print(f"Total execution time: {total_time:.3f} seconds")