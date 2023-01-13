from flask import Flask
import os 

app = Flask(__name__)

@app.route('/')
def home():
    return "hello"

# @app.route('/user<id>') # with specfic field
# def searchuser():
#     return "hello"

# @app.route('/')
# def listalluser():
#     return "hello"

# @app.route('/')
# def deleteuser():
#     return "hello"

# @app.route('/')
# def updateuser():
#     return "hello"

# @app.route('/')
# def adduser():
#     return "hello"

if __name__ == '__main__':
    app.run(debug=True , port=int (os.environ.get('PORT','5000')),host='0.0.0.0')