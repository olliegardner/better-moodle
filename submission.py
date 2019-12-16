from requests import Session
from bs4 import BeautifulSoup as bs

LOGIN_URL = "https://moodle.gla.ac.uk/login/index.php"

with Session() as s:
    site = s.get(LOGIN_URL)
    print(site.content)
