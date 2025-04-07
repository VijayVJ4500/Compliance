# sequence_edit.py

import time
from concurrent.futures import ThreadPoolExecutor
from ipss_utils.ipss_test import IpssTestCases
from load_test import headers
import requests


class deptedit(IpssTestCases):
    def __init__(self, driver):
        self.driver = driver

    def load_test_concurrent_patch_requests(self, num_requests=100, num_threads=10):
        """
        Perform a load test for updating sequence configurations concurrently.

        Args:
            num_requests (int): Total number of requests to send.
            num_threads (int): Number of concurrent threads.
        """
        url = "https://ipssapi.techgenzi.com/department_hrm/394/"

        payload = {
    "description": "DESCRIPTION",
    "dept_name": "cutting deparmtnet"
}

        headers_data = headers.get_headers()  # Assuming this returns necessary headers

        def make_patch_request(i):
            try:
                response = requests.patch(url, json=payload, headers=headers_data)
                print(f"Request {i + 1} - Status Code: {response.status_code}")
                return response.status_code
            except requests.RequestException as e:
                print(f"Request {i + 1} - Exception: {e}")
                return None

        # Start the concurrent execution
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(make_patch_request, i) for i in range(num_requests)]
            for future in futures:
                future.result()
        end_time = time.time()

        # Print final summary
        print(f"\n[TEST COMPLETED] Total requests: {num_requests}, Threads: {num_threads}")
        print(f"Total Time Taken: {end_time - start_time:.2f} seconds")
