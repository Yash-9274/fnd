import unittest
from flask import Flask
from app import app

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        # Test the home route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fake News Detection', response.data)

    def test_verify_text_route(self):
        # Test the verify text route with a sample verification text
        verification_text = 'example'
        response = self.app.post('/verify', data={'verification_text': verification_text})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Text Verification Result', response.data)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
