from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Generate a random captcha string


def generate_captcha_string(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Route to serve the captcha page


@app.route('/')
def index():
    captcha_string = generate_captcha_string()
    return render_template('captcha.html', captcha_string=captcha_string)

# Route to check the captcha response


@app.route('/check_captcha', methods=['POST'])
def check_captcha():
    user_input = request.form.get('captcha_input')
    captcha_string = request.form.get('captcha_string')

    # Check if the user input matches the captcha string
    if user_input == captcha_string:
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'failure'})


if __name__ == '__main__':
    app.run(debug=True)
