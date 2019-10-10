# -*- coding: utf-8 -*-
import json

import ftputil
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
def app(request, config):
    global fixture
    browser=request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture=Application(browser=browser, config=config)
    fixture.session.ensue_login(user_name=config["webadmin"]["username"], password=config["webadmin"]["password"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensue_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture(scope="session", autouse=True)
def configure_server(request, config):
    install_server_configuration(config["ftp"]['host'], config["ftp"]['username'], config["ftp"]['password'])
    def fin():
        restore_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    request.addfinalizer(fin)

def install_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_defaults_inc.php.bak"):
            remote.remove("config_defaults_inc.php.bak")
        if remote.path.isfile("config_defaults_inc.php"):
            remote.rename("config_defaults_inc.php", "config_defaults_inc.php.bak")
        remote.upload(os.path.join(os.path.dirname(__file__), "resources/config_defaults_inc.php"), "config_defaults_inc.php")

def restore_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_defaults_inc.php.bak"):
            if remote.path.isfile("config_defaults_inc.php"):
                remote.remove("config_defaults_inc.php")
            remote.rename("config_defaults_inc.php.bak", "config_defaults_inc.php")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

