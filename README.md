# Nova — Rule-Based AI Chatbot 🤖

## Project Overview

Nova is a simple conversational chatbot developed using Python as part of the DecodeLabs Artificial Intelligence Internship — Project 1.

The chatbot uses predefined rules and conditional statements to respond to user messages. It demonstrates fundamental programming concepts used to build rule-based conversational systems.

## Features

* Responds to greetings and basic conversational messages.
* Provides information about its supported commands.
* Remembers the user's name during the current session.
* Displays the current date and time.
* Handles empty and unrecognized messages.
* Supports a continuous conversation loop.
* Exits gracefully when the user enters an exit command.
* Includes automated unit tests.

## Technologies Used

* Python 3
* Python conditional statements (`if`, `elif`, `else`)
* Functions
* Loops
* String handling
* `datetime` module
* `unittest` module

## Project Structure

```text
Project_1_Rule_Based_Chatbot/
├── chatbot.py
├── test_chatbot.py
└── README.md
```

## Installation and Usage

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Project_1_Rule_Based_Chatbot
```

### 3. Run the chatbot

```bash
python chatbot.py
```

### 4. Run the automated tests

```bash
python -m unittest test_chatbot.py -v
```

No third-party Python packages are required for the current implementation.

## Example Interaction

```text
WELCOME TO NOVA CHATBOT
Your Friendly Rule-Based Assistant

You: hello
Nova: Hello! What's your name?

You: my name is Poornima
Nova: Nice to meet you, Poornima! I'll remember your name during this chat.

You: what is my name
Nova: Your name is Poornima!

You: bye
Nova: Goodbye! It was lovely chatting with you.
```

*Note: The exact output depends on the messages entered and the current date and time.*

## Learning Outcomes

This project demonstrates the use of conditional logic, functions, loops, string processing, exception handling, and automated testing to create a basic rule-based chatbot.

## Internship

**Program:** DecodeLabs Artificial Intelligence Internship
**Project:** Project 1 — Rule-Based AI Chatbot

---

This project is intended for educational purposes and demonstrates a basic rule-based conversational system. It does not use machine learning or train an AI model.
