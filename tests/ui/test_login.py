from pages.login_page import LoginPage


def test_valid_login(page, test_data):

    login_page = LoginPage(page)

    login_page.load()

    login_page.login(
        test_data["username"],
        test_data["password"]
    )

    assert "inventory" in page.url