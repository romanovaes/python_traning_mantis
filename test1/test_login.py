
def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.get_logged_user() == "administrator"