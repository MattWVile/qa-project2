from flask import url_for
from flask_testing import TestCase

from service_3.app import app, side_dish

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_side(self):
        for num in range(20):
            response = self.client.get(url_for('get_side_dish'))
            self.assert200(response)
            self.assertIn(response.data.decode(), side_dish)