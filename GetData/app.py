from flask import Flask
import ParseWeb
import ParseTwitter

app = Flask(__name__)

@app.route('/')
def interact():
    ParseWeb.console()
    ParseTwitter.console()
    return "Successfully called"

if __name__ == '__main__':
    app.run(debug=True)