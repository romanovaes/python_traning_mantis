from model.project import Project
from suds.client import Client
from suds import WebFault


def test():
    client = Client("http://localhost/mantisbt-2.22.1/api/soap/mantisconnect.php?wsdl")
    try:
        list1 = client.service.mc_projects_get_user_accessible("administrator", "test")
        #b=list1.split("{")
        pr1=list1[0]
        print(pr1)

    except WebFault:
        return False


