from requests import session
from bs4 import BeautifulSoup as bs
import configparser

config = configparser.RawConfigParser()
config.read("config.conf")

USERNAME = config.get("better-moodle", "username")
PASSWORD = config.get("better-moodle", "password")
LOGIN_URL = config.get("better-moodle", "login_url")

with session() as ses:
    site = ses.get(LOGIN_URL)
    
    content = bs(site.content, "html.parser")
    
    token = content.find("input", {"name": "logintoken"})["value"]

    data = {"username": USERNAME, "password": PASSWORD, "logintoken": token}

    ses.post(LOGIN_URL, data)

    dashboard = ses.get("https://moodle.gla.ac.uk/my/")

    print(dashboard.content)
