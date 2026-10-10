"""
Project: Rule-Based AI Chatbot
Internship: DecodeLabs - Artificial Intelligence Project 1

Description:
A beginner-friendly conversational chatbot built using Python
conditionals, functions, loops, and predefined rules.
"""

from datetime import datetime


def show_welcome():
	"""Display the chatbot's welcome screen."""
	print("\n" + "=" * 50)
	print("       WELCOME TO NOVA CHATBOT")
	print("       Your Friendly Rule-Based Assistant")
	print("=" * 50)
	print("Type 'help' to see what I can do.")
	print("Type 'exit', 'quit', or 'bye' to end our chat.")
	print("-" * 50)


def get_response(user_input, user_name):
	"""Generate a response using predefined conversational rules."""
	message = user_input.strip().lower()

	if not message:
		return "I didn't receive a message. Please type something!"

	if message in ("exit", "quit", "bye", "goodbye"):
		return "Goodbye! It was lovely chatting with you."

	elif message in ("hi", "hello", "hey", "hi nova", "hello nova"):
		if user_name:
			return f"Hello, {user_name}! 😊 How can I help you?"
		return "Hello! 😊 What's your name?"

	elif message in ("help", "commands", "what can you do"):
		return (
			"\nHere's what I can do:\n"
			"  • Say hello or introduce yourself\n"
			"  • Ask how I am\n"
			"  • Ask for the current time or date\n"
			"  • Ask about my capabilities\n"
			"  • Type 'help' to see these commands\n"
			"  • Type 'exit' or 'bye' to leave\n"
		)

	elif message.startswith("my name is "):
		name = user_input.strip()[11:].strip()
		if name:
			return f"Nice to meet you, {name}! I'll remember your name during this chat."
		return "Please tell me your name after 'my name is'."

	elif message == "what is my name":
		if user_name:
			return f"Your name is {user_name}!"
		return "You haven't told me your name yet. Try saying 'my name is Poornima'."

	elif message in ("how are you", "how are you?", "how are you doing"):
		return "I'm doing great! Thanks for asking. How are you?"

	elif message in ("what is your name", "who are you", "introduce yourself"):
		return (
			"I'm Nova, a rule-based chatbot built with Python. "
			"I use predefined rules to respond to your messages."
		)

	elif "time" in message:
		current_time = datetime.now().strftime("%I:%M %p")
		return f"The current time is {current_time}."

	elif "date" in message or "day is it" in message:
		current_date = datetime.now().strftime("%A, %d %B %Y")
		return f"Today's date is {current_date}."

	elif "thank" in message:
		return "You're welcome! 😊 Happy to help."

	elif "your features" in message or "your capabilities" in message:
		return (
			"I can respond to greetings, remember your name during this session, "
			"share the current date and time, and answer a few predefined questions."
		)

	elif message in ("i am fine", "i'm fine", "i am good", "i'm good"):
		return "That's great to hear! 😊 What would you like to talk about?"

	else:
		return (
			"I'm not sure how to respond to that yet. "
			"Type 'help' to explore my available commands."
		)


def chatbot():
	"""Run the chatbot conversation loop."""
	show_welcome()
	user_name = ""

	while True:
		try:
			user_input = input("\nYou: ").strip()

			# Save the user's name when provided.
			if user_input.lower().startswith("my name is "):
				entered_name = user_input[11:].strip()
				if entered_name:
					user_name = entered_name

			response = get_response(user_input, user_name)
			print(f"Nova: {response}")

			if user_input.lower() in ("exit", "quit", "bye", "goodbye"):
				break

		except (KeyboardInterrupt, EOFError):
			print("\nNova: Chat ended. Thank you for chatting with me!")
			break


if __name__ == "__main__":
	chatbot()
