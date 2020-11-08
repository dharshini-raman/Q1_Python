import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What city?"
        self.city_survey = city_Survey(question)
        self.city_responses = ['Cary', 'Raleigh', 'Morrisville', 'Wake Forest']

    def test_store_city_single_response(self):
        """Test that a single response is stored properly."""
        self.city_survey.store_response(self.city_responses[0])
        self.assertIn(self.city_responses[0], self.city_responses)
    def test_store_pop_single_response(self):
        """Test that a single response is stored properly."""
        self.pop_survey.store_response(self.responses[0])
        self.assertIn(self.pop_responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.city_responses.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.city_survey.responses)

if __name__ == '__main__':
    unittest.main()
