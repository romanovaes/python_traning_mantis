import quopri
import re

class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        wd=self.app.wd
        wd.get(self.app.baseUrl+"/signup_page.php")
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_css_selector("input[type='submit']").click()

        mail=self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url=self.extract_confirmation_url(mail)

        wd.get(url)
        #wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("%s" % password)
        wd.find_element_by_name("password_confirm").send_keys("%s" % password)
        wd.find_element_by_css_selector("span.bigger-110").click()


    def extract_confirmation_url(self, text):
        str_all = text[text.find("http://localhost") :]
        str_url = str_all.split("\n\n")[0]
        str_url_end = quopri.decodestring(str_url)
        return str_url_end.decode('utf-8')