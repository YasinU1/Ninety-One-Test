import unittest
from unittest.mock import patch, mock_open
from main import read_csv_file, parse_csv_data, get_top_scorers, main

class TestTopScorers(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="test content")
    def test_read_csv_file(self, mock_file):
        """
        Testing the read_csv_file function.
        Mock the built-in function so you can read from a file without actually needing the file.
        Assert that the output matches our expected output.
        """
        content = read_csv_file('test_file.csv')
        self.assertEqual(content, "test content")

    def test_parse_csv_data(self):
        """
        Test the parse_csv_data function using test CSV data.
        Assert that the parsed output matches our expected hashmap.
        """
        csv_data = """First Name,Second Name,Score
                        Dee,Moore,56
                        Sipho,Lolo,78
                        """
        expected = {
            "Dee Moore": 56,
            "Sipho Lolo": 78
        }
        result = parse_csv_data(csv_data)
        self.assertEqual(result, expected)

    def test_get_top_scorers(self):
        """
        Testing the get_top_scorers function using a dummy scores.
        Assert that the retrieved scorers match our expected.
        """
        scores_dict = {
            "Dee Moore": 56,
            "Sipho Lolo": 78,
            "Noosrat Hoosain": 64,
            "George Of The Jungle": 78
        }
        expected = ["George Of The Jungle", "Sipho Lolo"]
        result = get_top_scorers(scores_dict)
        self.assertEqual(result, expected)

    @patch('builtins.print')
    def test_main(self, mock_print):
        """
        Testiing the main function.
        Mock the built-in print function to capture its output for testing.
        Assert that the print function was called with the expected output.
        """
        main("TestData.csv")
        mock_print.assert_called_with("Sipho Lolo: 78")

if __name__ == "__main__":
    unittest.main()
