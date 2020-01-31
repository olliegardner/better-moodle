import time
import configparser
from selenium import webdriver

config = configparser.RawConfigParser()
config.read("config.conf")

username = config.get("better-moodle", "username")
password = config.get("better-moodle", "password")
url = config.get("better-moodle", "url")

driver = webdriver.Chrome()
courses = []

def login():
    driver.get(url + "/login/index.php")
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("btn").click()

def get_courses():
    cards = driver.find_elements_by_class_name("dashboard-card")

    for card in cards:
        id = card.get_attribute("data-course-id")
        if id != None and id not in courses:
            courses.append(id)
    
    for course in courses:
        driver.get(url + "/course/view.php?id=" + course)
        
    #print(driver.find_elements_by_class_name("page-link"))
    #get_courses()


def main():
    login()
    time.sleep(5) # sleep while dynamic page content loads in
    get_courses()

    driver.close()

if __name__ == "__main__":
    main()
