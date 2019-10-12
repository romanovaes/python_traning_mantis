

class SessionHelper:

    def __init__(self, app):
        self.app=app

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//i[2]").click()
        wd.find_element_by_link_text("Logout").click()

    def login(self,user_name, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("%s" % user_name)
        wd.find_element_by_css_selector("input[type='submit']").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("%s" % password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def is_logged_in_as(self, user_name):
        wd = self.app.wd
        return wd.find_element_by_css_selector("span.user-info").text == user_name

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("span.user-info").text

    def ensue_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("span.user-info")) > 0

    def ensue_login(self, user_name, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(user_name):
                return
            else:
                self.logout()
        self.login(user_name, password)
