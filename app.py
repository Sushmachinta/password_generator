from flask import Flask, render_template, request
import random
import string
app = Flask(__name__, template_folder='../templates', static_folder='../static')

def generate_password(length=12, password_type='both'):
    if password_type == 'numbers':
        characters = string.digits
    elif password_type == 'alphabets':
        characters = string.ascii_letters
    else:
        characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        password_type = request.form.get('password_type', 'both')
        length_str = request.form.get('length', '12')
        try:
            length = int(length_str)
            if length < 1:
                length = 1
            elif length > 128:
                length = 128
        except ValueError:
            length = 12
        password = generate_password(length=length, password_type=password_type)
    return render_template('index.html', password=password)

if __name__ == "__main__":
    app.run(debug=True)
