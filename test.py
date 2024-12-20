from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)


@app.route('/')
def home():
    return "petit apollon"


app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    app.run(debug=True)