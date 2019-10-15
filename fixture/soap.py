from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app=app

    def can_login(self, username, password):
        client = Client(self.app.baseUrl+"/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_project(self, username, password):
        client = Client(self.app.baseUrl+"/api/soap/mantisconnect.php?wsdl")
        try:
            all_project = client.service.mc_projects_get_user_accessible(username, password)
            list_project = []
            for element in all_project:
                list_project.append(Project(name=element['name'], description=element['description'], id=element['id']))
            return list_project
        except WebFault:
            return False

