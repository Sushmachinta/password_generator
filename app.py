from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12, use_digits=True, use_special_chars=True, use_uppercase=True, use_lowercase=True, all_uppercase=False, all_lowercase=False):
    char_set = ""
    
    # If "all uppercase" is selected, ignore other case settings
    if all_uppercase:
        char_set += string.ascii_uppercase  # Uppercase letters
    elif all_lowercase:
        char_set += string.ascii_lowercase  # Lowercase letters
    else:
        if use_uppercase:
            char_set += string.ascii_uppercase  # Uppercase letters

        if use_lowercase:
            char_set += string.ascii_lowercase  # Lowercase letters

    if use_digits:
        char_set += string.digits  # Digits

    if use_special_chars:
        char_set += string.punctuation  # Special characters

    if not char_set:
        raise ValueError("Password must include at least one character type (uppercase, lowercase, digits, or special characters).")

    # Generate password using selected character set
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        length = int(request.form['length'])
        use_digits = 'digits' in request.form
        use_special_chars = 'special_chars' in request.form
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        all_uppercase = 'all_uppercase' in request.form
        all_lowercase = 'all_lowercase' in request.form
        
        # Generate the password based on the selected options
        password = generate_password(length, use_digits, use_special_chars, use_uppercase, use_lowercase, all_uppercase, all_lowercase)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
