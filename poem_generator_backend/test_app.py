import unittest
from app import app  # Make sure this is the correct import from your Flask app

class TestPoemGenerator(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Set up a test client to send HTTP requests to the app
        self.app.testing = True  # Enable testing mode

    def test_generate_poem(self):
        # Test the POST request to generate a poem
        response = self.app.post('/api/generate-poem', json={
            "theme": "love", "style": "sonnet", "emotion": "happy"
        })
        self.assertEqual(response.status_code, 200)  # Check if status code is 200 (OK)
        self.assertIn("poem", response.json)  # Check if the response contains a poem

    
if __name__ == "__main__":
    unittest.main()
