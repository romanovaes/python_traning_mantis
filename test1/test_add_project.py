from model.project import Project


def test_add_project(app, json_project):
    project = json_project
    old_project = app.project.get_project_list()
    app.project.add_project(project)
    new_project = app.project.get_project_list()
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)