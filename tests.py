import unittest
from flask import Flask
from unittest.mock import patch
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

    @patch('app.requests.get')  # Mocking the requests.get method
    def test_api_calling(self, mock_get):
        # Mock the response from the News API
        mock_get.return_value.json.return_value = {
            'articles': [
                {'title': 'Fake News Article', 'description': 'This is a fake news article.'},
                {'title': 'Real News Article', 'description': 'This is a real news article.'}
            ]
        }

        # Call the API method
        result = app.fetch_news_articles('example')

        # Assert that the result is as expected
        self.assertTrue(result)  # Assuming the result is True if any article contains the verification text

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
