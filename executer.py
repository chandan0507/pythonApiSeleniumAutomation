from flask import Flask
from postUserInputApi import postUserInput

app = Flask(__name__)

@app.route('/postUserInput', methods=['POST'])
def returnUserResponse():
    return postUserInput()

if __name__ == '__main__':
    app.run(debug=True, port=8080)