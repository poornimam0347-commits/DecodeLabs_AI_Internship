import unittest
from chatbot import get_response


class TestNovaChatbot(unittest.TestCase):

	def test_greeting(self):
		self.assertIn("Hello", get_response("hello", ""))

	def test_help_command(self):
		self.assertIn("Here's what I can do", get_response("help", ""))

	def test_how_are_you(self):
		self.assertIn("great", get_response("how are you", "").lower())

	def test_unknown_message(self):
		self.assertIn("not sure", get_response("random message", "").lower())

	def test_name_recognition(self):
		response = get_response("what is my name", "Poornima")
		self.assertIn("Poornima", response)

	def test_empty_message(self):
		self.assertIn("didn't receive", get_response("", "").lower())


if __name__ == "__main__":
	unittest.main()
