from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# OpenAI API 키를 설정합니다.
openai.api_key = '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'

def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    prompt = f"사용자: {user_input}\n챗봇:"
    bot_response = get_openai_response(prompt)
    return {'bot_response': bot_response}

if __name__ == '__main__':
    app.run(debug=True)