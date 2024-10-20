# AI-Powered Flask Chatbot

This project is an AI-powered Flask application that interacts with OpenAI's API to provide responses based on user input and optionally uploaded files. It includes a basic web interface and demonstrates how to integrate OpenAI's capabilities into a Flask application.

## Project Overview

- **Flask**: The web framework used to build the application.
- **OpenAI API**: Utilized to generate responses based on user input.
- **configparser**: Manages configuration settings for the OpenAI API.

## Features

- **Interactive Chat Interface**: Users can input messages and upload files to receive AI-generated responses.
- **Dynamic File Handling**: The application can read the contents of uploaded files and incorporate them into the request sent to the AI.
- **Personalized Messages**: The AI retains context by storing a conversation history.
- **Markdown Conversion**: The application can convert Markdown to HTML. Simply aneble it in `config.ini` by turning `markdown_conversion` to `True`. *(Disabled by default as the creator doesn't quite like how it looks; not removed as they knew others might prefer how it looks.)*

## Additional Files

- **`config.ini`**: Configuration file containing the necessary OpenAI API credentials:
```ini
[openai]
api_key = YOUR_API_KEY
organization = YOUR_ORGANIZATION
project = YOUR_PROJECT
model = gpt-4o-mini
initial_message = You are a Monty Python expert, here to provide humours insights, witty banter and ...
```
Make sure to fill in your own OpenAI API key and organization details.

- **`requirements.txt`**: Lists the required packages for the application:
```plaintext
configparser~=7.1.0
openai~=1.51.2
Flask~=3.0.3
```
Use this file to install the necessary dependencies.
``` shell
pip install -r requirements.txt
```

- **`index.html`**: The HTML template for the main user interface of the application. Customize this file to change the appearance and layout.

## Written By

This entire README was written by an AI! Yes, you read that correctly. The creator was too lazy to write it themselves, so they let the chatbot do the work. Just like a Monty Python sketch, this raises the age-old question: If an AI can write a README, why should I bother?

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/5mikachu/pAIthon.git
cd pAIthon
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Fill in your OpenAI API credentials in `config.ini`.

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Acknowledgements

- **Monty Python** for inspiring the idea that even AI can have a sense of humor!
- **The AI** for writing an incredible README, I only needed to remove one killer rabbit! 