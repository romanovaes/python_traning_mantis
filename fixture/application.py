from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.commonDef import ContactGroupHelper

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
        self.group=GroupHelper(self)
        self.contact=ContactHelper(self)
        self.baseUrl=baseUrl
        self.commonDef=ContactGroupHelper(self)

    def is_valid(self):
        try:
           self.wd.current_url
           return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("MainForm"))>0):
           wd.get(self.baseUrl)

    def destroy(self):
        self.wd.quit()


