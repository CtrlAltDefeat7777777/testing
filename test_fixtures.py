import pytest

@pytest.fixture
def user():
    print("Юзер")
    return "username","password"


@pytest.fixture
def login_page(browser):
    print("Логин пейдж")

def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"

def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
