# headers.py
import os
import requests
from ipss_utils.ipss_test import IpssTestCases  # Changed from IpssTestCase to IpssTestCases

class TestData:
    USERNAME = "ithod@pgc.com"
    PASSWORD = "dev@123456789"
    AUTH_URL = os.getenv("AUTH_URL", "https://ipssapi.techgenzi.com/users/login")

class AppTestCase(IpssTestCases):  # Changed from IpssTestCase to IpssTestCases
    @staticmethod
    def get_headers():
        """Return common API headers with authorization token."""
        # First get the token
        response = requests.post(TestData.AUTH_URL, json={
            'username': TestData.USERNAME,
            'password': TestData.PASSWORD
        })
        access_token = response.json()['access_token']
        
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
