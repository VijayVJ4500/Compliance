# shift_delete.py

import time
from concurrent.futures import ThreadPoolExecutor
from ipss_utils.ipss_test import IpssTestCases
from load_test import headers
import requests


class shiftdelete(IpssTestCases):
    def __init__(self, driver):
        self.driver = driver

    def load_test_concurrent_delete_requests(self, num_requests=100, num_threads=10):
        """
        Perform a load test for deleting shift configurations concurrently.

        Args:
            num_requests (int): Total number of requests to send.
            num_threads (int): Number of concurrent threads.
        """
        url = "https://ipssapi.techgenzi.com/shift_configure/shift_mast_hrm/132/"  # Example URL to delete a specific configuration
        headers_data = headers.get_headers()  # Assuming this returns necessary headers

        def make_delete_request(i):
            try:
                response = requests.delete(url, headers=headers_data)
                print(f"Request {i + 1} - Status Code: {response.status_code}")
                return response.status_code
            except requests.RequestException as e:
                print(f"Request {i + 1} - Exception: {e}")
                return None

        # Start the concurrent execution
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(make_delete_request, i) for i in range(num_requests)]
            for future in futures:
                future.result()
        end_time = time.time()

        # Print final summary
        print(f"\n[TEST COMPLETED] Total requests: {num_requests}, Threads: {num_threads}")
        print(f"Total Time Taken: {end_time - start_time:.2f} seconds")
