import json
from flask import Flask, redirect, request, render_template, jsonify
from youtube_transcriber import search_keywords

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search_keyword', methods=['POST'])
def searchKeyWord():
    """
    Expected receiving the keyWord and youtubeURL.
    :return: jonson time list back to javascript
    """
    url = request.form["url"]
    keyword = request.form["keyword"]

    result = search_keywords(url, keyword)

    if not result:
        return jsonify(dict())

    return jsonify(timeStamp(result))


def timeStamp(list_time):
    """
    Format time stam into `00h00m00s` into the dictionary
    :param list_time: float list of time stamp in second
    :return format_time: dictionary of format time
    """
    format_time = dict()
    i = 0
    for time in list_time:
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        format_time[str(i)] = {"%dh%02dm%02ds" % (h, m, s): time}
        i += 1
    return format_time


if __name__ == '__main__':
    app.run()
