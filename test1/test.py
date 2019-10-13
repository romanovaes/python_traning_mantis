from model.project import Project
from suds.client import Client
from suds import WebFault


def test():
    client = Client("http://localhost/mantisbt-2.22.1/api/soap/mantisconnect.php?wsdl")
    try:
        all_project = client.service.mc_projects_get_user_accessible("administrator", "test")
        #b=list1.split("{")
        i=0
        list_project=[]
        for element in all_project:
            list_project.append(Project(name=element['name'], description=element['description'], id=element['id']))

        print(list_project)
        print(list_project)

    except WebFault:
        return False


