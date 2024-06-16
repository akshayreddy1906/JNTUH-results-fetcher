import unittest
from unittest.mock import patch
from project import display_total_gpa, display_semester_details, display_cgpa_credits

class TestJNTUHResultsFunctions(unittest.TestCase):

    def setUp(self):
        import json
        with open('sample_data.json', 'r') as f:
            self.sample_data = json.load(f)

    def test_display_total_gpa(self):
        result = display_total_gpa(self.sample_data)
        self.assertEqual(result, "Total GPA: 6.76")

    @patch('builtins.input', side_effect=['1-1'])
    def test_display_semester_details_single(self, mock_input):
        result = display_semester_details(self.sample_data)
        self.assertIn("ENGINEERING WORKSHOP", result)
        self.assertIn("A+", result)
        self.assertIn("2.5", result)

    @patch('builtins.input', side_effect=['ALL'])
    def test_display_semester_details_all(self, mock_input):
        result = display_semester_details(self.sample_data)
        self.assertIn("1-1", result)
        self.assertIn("4-2", result)
        self.assertIn("ENGINEERING WORKSHOP", result)
        self.assertIn("NON CONVENTIONAL SOURCES OF ENERGY", result)

    @patch('builtins.input', side_effect=['1-1 1-2'])
    def test_display_cgpa_credits_multiple(self, mock_input):
        result = display_cgpa_credits(self.sample_data)
        self.assertIn("1-1", result)
        self.assertIn("19", result)
        self.assertIn("7.61", result)
        self.assertIn("1-2", result)
        self.assertIn("18", result)
        self.assertIn("6.64", result)

    @patch('builtins.input', side_effect=['ALL'])
    def test_display_cgpa_credits_all(self, mock_input):
        result = display_cgpa_credits(self.sample_data)
        self.assertIn("1-1", result)
        self.assertIn("4-2", result)
        self.assertIn("7.61", result)
        self.assertIn("7.75", result)

if __name__ == '__main__':
    unittest.main()
