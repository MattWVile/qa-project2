from flask import url_for
from flask_testing import TestCase

from app import app, main_dish

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_main(self):

        for num in range(20):
            response = self.client.get(url_for('get_main_dish'))
            self.assert200(response)
            self.assertIn(response.data.decode(), main_dish)