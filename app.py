import time


from flask import Flask, redirect, request, render_template, jsonify

from youtube_transcriber import search_keywords

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search_keyword',  methods=['POST'])
def searchKeyWord():
    """
    Expected receiving the keyWord and youtubeURL.
    :return:
    """

    url = request.form["url"]
    keyword = request.form["keyword"]

    time_stamps = timeStamp(search_keywords(url, keyword))
    print(time_stamps)
    return "duma"


def timeStamp(list_time):
    format_time = list()
    for time in list_time:
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        format_time.append("%d:%02d:%02d" % (h, m, s))
    return format_time

if __name__ == '__main__':
    app.run()



