import unittest
from unittest.mock import patch, MagicMock
from telegram_scraper import TelegramScraper

class TestTelegramScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = TelegramScraper()

    def test_load_user_agents(self):
        # Test that user agents are loaded correctly
        self.assertGreater(len(self.scraper.user_agents), 0)

    @patch('telegram_scraper.requests.get')
    def test_request(self, mock_get):
        # Test that request method works correctly
        mock_get.return_value = MagicMock(status_code=200)
        response = self.scraper.request('https://example.com')
        self.assertEqual(response.status_code, 200)

    def test_extract_links(self):
        # Test link extraction
        text = "Check out https://x.com/user and https://facebook.com/user"
        links = self.scraper.extract_links(text, ['x.com', 'facebook.com'])
        self.assertEqual(len(links), 2)
        self.assertIn('x.com', links)
        self.assertIn('facebook.com', links)

    # Add more tests for other methods...

if __name__ == '__main__':
    unittest.main()