from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app=app

    def add_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//button[contains(text(),'Создать новый проект')]")
        wd.find_element_by_id('project-name').click()
        wd.find_element_by_id('project-name').send_keys(project.name)
        wd.find_element_by_id('project-description').click()
        wd.find_element_by_id('project-description').send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
