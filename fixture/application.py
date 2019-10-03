from selenium import webdriver
from fixture.session import SessionHelper
from model.project import Project
from fixture.project import ProjectHelper

class Application:

    def __init__(self, browser, baseUrl):
        if browser=="firefox":
          self.wd = webdriver.Firefox()
        elif browser=="chrome":
          self.wd = webdriver.Chrome()
        elif browser=="ie":
          self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session=SessionHelper(self)
        self.baseUrl=baseUrl
        self.project=ProjectHelper(self)


    def is_valid(self):
        try:
           self.wd.current_url
           return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/mantisbt-2.22.1/") and len(wd.find_elements_by_css_selector("div.login-container")) > 0):
           wd.get(self.baseUrl)

    def destroy(self):
        self.wd.quit()


