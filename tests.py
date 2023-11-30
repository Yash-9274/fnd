# tests.py
import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

        # Use the app context to ensure templates are rendered
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Pop the app context after the test is done
        self.app_context.pop()

    def test_home_route(self):
        response = self.app.get('/')
        # Log the rendered HTML for debugging
        print(response.data.decode('utf-8'))

        # Ensure status code is 200 and 'News Articles' is in the rendered HTML
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'News Articles', response.data)

    def test_verify_text_route(self):
        response = self.app.post('/verify', data={'verification_text': 'fake'})
        # Log the rendered HTML for debugging
        print(response.data.decode('utf-8'))

        # Ensure status code is 200 and 'Text Verification Result' is in the rendered HTML
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Text Verification Result', response.data)

if __name__ == '__main__':
    unittest.main()
