
# tests.py
import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'News Articles', response.data)

    def test_verify_text_route(self):
        response = self.app.post('/verify', data={'verification_text': 'fake'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Text Verification Result', response.data)

if __name__ == '__main__':
    unittest.main()