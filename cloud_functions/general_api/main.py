from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World from cloud functiondsdss!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
