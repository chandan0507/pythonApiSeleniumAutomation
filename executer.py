from flask import Flask
from flask_cors import CORS
from postUserInputApi import postUserInput

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:3000")

@app.route('/postUserInput', methods=['POST'])
def returnUserResponse():
    return postUserInput()

if __name__ == '__main__':
    app.run(debug=True, port=8080)