from flask import Flask, redirect, request, render_template

# from youtube_transcriber

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/searchWord',  methods=['POST'])
def searchWord():
    """
    Expected receiving the keyWord and youtubeURL.
    :return:
    """
    keyWord = request.form['keyword']
    yURL = request.form['url']


if __name__ == '__main__':
    app.run()
