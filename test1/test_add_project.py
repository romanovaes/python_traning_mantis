import string
import random
from model.project import Project


def test_add_project(app):
    project = Project(name=random_string('название', 7), description=random_string('описание', 7))
    old_project = app.soap.get_list_project("administrator", "test")
    app.project.add_project(project)
    new_project = app.soap.get_list_project("administrator", "test")
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])