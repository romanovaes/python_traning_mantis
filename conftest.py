# -*- coding: utf-8 -*-
import json
import pytest
import os.path
from fixture.application import Application


fixture=None
target=None

def load_config(file):
    global target
    if target is None:
        config_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
           target=json.load(f)
    return target

@pytest.fixture(scope="session")
def app(request):
    global fixture
    browser=request.config.getoption("--browser")
    web_config=load_config(request.config.getoption("--target"))["web"]
    web_config2 = load_config(request.config.getoption("--target"))["webadmin"]
    if fixture is None or not fixture.is_valid():
        fixture=Application(browser=browser, baseUrl=web_config["baseUrl"])
    fixture.session.ensue_login(user_name=web_config2["username"], password=web_config2["password"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensue_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

