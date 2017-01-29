import time


from flask import Flask, redirect, request, render_template, jsonify

from youtube_transcriber import search_keywords

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/searchKeyWord',  methods=['POST'])
def searchKeyWord():
    """
    Expected receiving the keyWord and youtubeURL.
    :return:
    """
    keyWord = request.form['keyword']
    yURL = request.form['url']
    timeStamp(search_keywords(keyWord, yURL))


def timeStamp(list_time):
    format_time = list()
    for time in list_time:
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        format_time.append("%d:%02d:%02d" % (h, m, s))


if __name__ == '__main__':
    app.run()



