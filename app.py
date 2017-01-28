from flask import Flask, render_template, request
print('test')
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello"


if __name__ == '__main__':
    app.run()
