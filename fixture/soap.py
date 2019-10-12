from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app=app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.22.1/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_project(self, username, password):
        client = Client("http://localhost/mantisbt-2.22.1/api/soap/mantisconnect.php?wsdl")
        try:
            list1 = client.service.mc_projects_get_user_accessible(username, password)
            return list1
        except WebFault:
            return False

