from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html'), "Bonjour"


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f"Merci, {name}! Votre email ({email}) a été reçu."


if __name__ == '__main__':
    app.run(debug=True)
