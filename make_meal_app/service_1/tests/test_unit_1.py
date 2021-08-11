from flask import url_for
from flask_testing import TestCase
from requests_mock import mock
from service_1.application import app, db


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///"
        )
        return app
    
    def setUp(self):
        db.create_all()
    
    def tearDown(self):
        db.drop_all()

class TestResponse(TestBase):

    def test_index(self):

        with mock() as mocker:
            mocker.get('http://service-2:5000/get/main_dish', text='Pie')
            mocker.get('http://service-3:5000/get/side_dish', text='Chips')
            mocker.post('http://service-4:5000/post/meal', json=4)

            result = self.client.get(url_for('home'))

        self.assert200(result)
        self.assertIn('pasta', result.data.decode())
        self.assertIn('Chips', result.data.decode())
        self.assertIn('£4', result.data.decode())