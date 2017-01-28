from flask import Flask, redirect, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/searchWord')
# def searchWord():
#     if LOGIN:
#         return render_template('contactprofile.html')
#     return render_template('contact.html')

if __name__ == '__main__':
    app.run()
