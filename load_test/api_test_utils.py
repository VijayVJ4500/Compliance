# api_test_utils.py
from config import num_requests as default_num_requests, num_threads as default_num_threads
import requests
from concurrent.futures import ThreadPoolExecutor


def load_test_requests(method, url, payload=None, headers=None, num_requests=None, num_threads=None):
    """
    Simulates API load testing with concurrent requests.

    Args:
        method (str): HTTP method (GET, POST, PATCH, DELETE).
        url (str): API endpoint URL.
        payload (dict): Data to send with the request.
        headers (dict): Headers for the request.
        num_requests (int): Number of total requests to send.
        num_threads (int): Number of concurrent threads.
    """
    num_requests = num_requests or default_num_requests
    num_threads = num_threads or default_num_threads

    def make_request(i):
        response = None
        try:
            if method == "POST":
                response = requests.post(url, json=payload, headers=headers)
            elif method == "GET":
                response = requests.get(url, params=payload, headers=headers)
            elif method == "PATCH":
                response = requests.patch(url, json=payload, headers=headers)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)

            print(f"Request {i + 1} - Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request {i + 1} - Exception: {e}")
        return response

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(make_request, range(num_requests))
