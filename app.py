import configparser
import markdown
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    """
    Get a response based on the user input and optional file from OpenAI.
    """
    user_input: str | None = request.form.get('message')
    file = request.files.get('file')

    structured_input: str = ""

    if file:
        file_name: str = file.filename
        file_content: str = file.read().decode('utf-8')

        structured_input += f"[File Uploaded: '{file_name}']"
        structured_input += f"[File Contents Start]{file_content}[File Contents End]"

    if user_input:
        structured_input += f"[User Message Start]{user_input}[User Message End]"

    messages.append({'role': "user", 'content': structured_input})

    response = client.chat.completions.create(
        model=config['openai']['model'],
        messages=messages
    )

    ai_response: str = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_response})

    if config['general']['markdown_conversion']:
        html_response: str = markdown.markdown(ai_response)
        return jsonify({'response': html_response})
    else:
        return jsonify({'response': ai_response})

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    messages: list[dict[str, str]] = [
        {"role": "system",
         "content": config['openai']['initial_message']}
    ]

    # Initialize OpenAI client
    client = openai.OpenAI(
        api_key=config['openai']['api_key'],
        organization=config['openai']['organization'],
        project=config['openai']['project']
    )

    app.run()
