import requests
from xml.etree import ElementTree

OK = 200


def transcribe_video(id):
    """ Transcribe YouTube video.

    Args:
        id (str): Video ID.

    Returns:
        tuple (HTTP response code, response content)
    """

    url = "http://video.google.com/timedtext?lang=en&v={}".format(id)
    response = requests.get(url)

    return response.status_code, response.content


def search_keywords(id, keyword):
    """ Search for keyword in a YouTube video.

    Args:
        id (str): Video ID.
        keyword (str): Keyword.

    Returns:
        list of timestamp in second(s).
    """

    timestamps = list()

    status_code, content = transcribe_video(id)

    if status_code == OK:

        tree = ElementTree.fromstring(content)

        for node in tree:

            if keyword in node.text:
                # print(node.text)
                # print(node.attrib)
                timestamps.append(float(node.attrib["start"]))

    return timestamps


if __name__ == '__main__':
    id = "EeQ8pwjQxTM"
    keyword = "sort"
    timestamps = search_keywords(id, keyword)
    print(timestamps)
