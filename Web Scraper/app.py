from flask import Flask
import ParseWeb
import ParseTwitter
import os

app = Flask(__name__)

@app.route('/')
def interact():
    ParseWeb.console()
    ParseTwitter.console()
    return "Operation Completed"

if __name__ == "__main__":
    environment_port = os.getenv("PORT", 5000)
    app.run(debug=True, host='0.0.0.0', port=environment_port)    