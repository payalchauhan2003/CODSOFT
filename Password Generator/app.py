from flask import Flask, request, render_template_string
import random
import string

app = Flask(__name__)

# HTML template for the form
form_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Password Generator</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 50px; }
      input[type=number] { width: 50px; }
      input[type=submit] { padding: 5px 15px; }
    </style>
  </head>
  <body>
    <h1>Password Generator</h1>
    <form method="post" action="/">
      <label for="length">Password Length:</label>
      <input type="number" id="length" name="length" min="1" required>
      <input type="submit" value="Generate">
    </form>
    {% if password %}
      <h2>Your Generated Password:</h2>
      <p>{{ password }}</p>
    {% endif %}
  </body>
</html>
'''

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        length = int(request.form['length'])
        password = generate_password(length)
    return render_template_string(form_template, password=password)

if __name__ == '__main__':
    app.run(debug=True)
