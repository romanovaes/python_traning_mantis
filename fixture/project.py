from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app=app

    def add_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//button[contains(text(),'Создать новый проект')]").click()
        wd.find_element_by_name('name').click()
        wd.find_element_by_name('name').send_keys(project.name)
        wd.find_element_by_name('description').click()
        wd.find_element_by_name('description').send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()



    def get_project_list(self):
        project_cache = []
        wd = self.app.wd
        self.open_project_page()
        for element in wd.find_elements_by_xpath("//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"):
            name = element.find_element_by_tag_name("a").text
            description = element.find_element_by_css_selector("td:nth-child(5)").text
            id = (element.find_element_by_tag_name("a").get_attribute('href')).split('=')[1]
            project_cache.append(Project(name=name, description=description, id=id))
        return list(project_cache)

    def open_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_css_selector("i.menu-icon.fa.fa-gears").click()
            wd.find_element_by_xpath("//a[contains(text(),'Управление проектами')]").click()

    def delete_project(self, id):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % str(id)).click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        self.open_project_page()