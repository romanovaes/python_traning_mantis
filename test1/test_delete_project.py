import random
from model.project import Project

def test_delete_project(app):
    old_project = app.soap.get_list_project("administrator", "test")
    if len(old_project) == 0:
        app.project.add_project(Project(name="удаление", description='удаление'))
        old_project = app.project.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project(project.id)
    new_project = app.soap.get_list_project("administrator", "test")
    old_project.remove(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)



