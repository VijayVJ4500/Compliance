import unittest
from ipss_utils.ipss_test import IpssTestCases
from customer.app import create_app
from customer.customer import config

app = create_app(config.Config)

sample_data = {
      "customer_type": "Individual",
      "organization_name": "Testhhhh",
      "website": "www.tech.com",
      "address": "South street",
      "city": "ppm",
      "state": "tamilnadu",
      "customer_name": "Titan",
      "job_position": "Backend developer"
    }

class AppTestCase(IpssTestCases):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()
        super(AppTestCase, self).setUp()

    def test_list_customer(self):
        response = self.client.get(
            "/customer/",

            headers={
                'Authorization': f"Bearer {self.access_token}"
            }
        )
        assert response.status_code == 200

    def test_single_get_customer(self):
        response = self.client.get(
            "/customer/48716/",

            headers={
                'Authorization': f"Bearer {self.access_token}"
            }
        )
        print(response.json)
        print(response.status_code)
        assert response.status_code == 200

    def test_create_customer(self):
        response = self.client.post(
            "/customer/",
                json=sample_data,
            headers={
                'Authorization': f"Bearer {self.access_token}"
            }
        )
        print(response.status_code)
        print(response.json)
        assert response.status_code == 200

    def test_delete_customer(self):
        response = self.client.delete(
            "/customer/1/",

            headers={
                'Authorization': f"Bearer {self.access_token}"
            })

        assert response.status_code == 200

    def test_patch_scustomer(self):
        response = self.client.patch(
            "/customer/1/",
            json=sample_data,
            headers={
                'Authorization': f"Bearer {self.access_token}"
            })

        assert response.status_code == 200

    def test_put_customer(self):
        response = self.client.put(
            "/customer/1/",
            json=sample_data,
            headers={
                'Authorization': f"Bearer {self.access_token}"
            })

        assert response.status_code == 200


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(AppTestCase())
    unittest.TextTestRunner().run(suite)
