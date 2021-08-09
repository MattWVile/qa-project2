from flask import url_for
from flask_testing import TestCase
from requests_mock import mock
from application import app, db

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
            mocker.get('http://service-4:5000/post_meal', json=4)

            result = self.client.get(url_for('home'))

        self.assert500(result)
        self.assertIn('Pie Chips £4', result.data.decode())