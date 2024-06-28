import io
import unittest
from unittest.mock import patch
from main import main

class TestFootballDataFetcher(unittest.TestCase):

    @patch('builtins.input', side_effect=['6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exit_program(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Thank you for using Football Data Fetcher! Exiting the program.", output)

    @patch('builtins.input', side_effect=['3', 'Real Madrid', 'Premier League', '2021', 'yes', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_real_madrid_in_prem(self, mock_stdout, mock_input):
        with patch('football_api.fetch_team_stats') as mock_fetch:
            mock_fetch.return_value = True
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Real Madrid", output)
            self.assertIn("Premier League", output)
            self.assertIn("England", output)

if __name__ == '__main__':
    unittest.main()


