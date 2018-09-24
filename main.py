from flask import Flask, request
from caesar import encrypt
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>

        <style>

            form {

                background-color: #eee;

                padding: 20px;

                margin: 0 auto;

                width: 540px;

                font: 16px sans-serif;

                border-radius: 10px;

            }

            textarea {

                margin: 10px 0;

                width: 540px;

                height: 120px;

            }

        </style>

    </head>

    <body>

      <form method='POST'>
        <label for="rot">Rotate by:</label>
        <input name="rot" type="text" value="0"/>
        <textarea name="text"></textarea>
        <input type="submit"/>
      </form>

    </body>

</html>
"""

#initial site
@app.route("/")
def index():
    return form

#Use request to grab user info from form and then pass to caesar.py
@app.route("/", methods=['POST'])
def web_encrypt():
    rotation = request.form['rot']
    user_text = request.form['text']
    encrypted_str = encrypt(user_text, int(rotation))
    return '<h1>Your encrypted string is: {0}'.format(encrypted_str)

app.run()