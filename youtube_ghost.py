import os
import requests 
from selenium import webdriver
from sys import platform
from xml.etree import ElementTree

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRIVER_NAME = "chromedriver.exe" if platform == "win32" else "chromedriver"
DRIVER_DIR = os.path.join(BASE_DIR, "plugins", DRIVER_NAME)

JS_SCRIPT = 'if(yt.config_.TTS_URL.length) window.location.href=yt.config_.TTS_URL+"&kind=asr&fmt=srv1&lang=en"'


def get_transcribe_url(youtube_url):
    """ Get transcribe URL.

    Args:
        youtube_url (str): YouTube URL.
    """

    driver = webdriver.Chrome(DRIVER_DIR)
    driver.get(youtube_url)
    driver.execute_script(JS_SCRIPT)
    transcribe_url = driver.current_url
    driver.quit()
    return transcribe_url
