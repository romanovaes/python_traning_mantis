from model.project import Project


def test_add_project(app, json_project):
    project = json_project
    old_project = app.project.get_progect_list()
    app.project.add_progect(project)
    new_project = app.project.get_progect_list()
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
