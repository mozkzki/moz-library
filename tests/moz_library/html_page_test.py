import os
import pytest
from moz_library.user import User
from moz_library.html_page import HtmlPage
from moz_library.library import Library


class TestHtmlPages:
    def setup(self):
        pass

    @pytest.fixture()
    def html_page1(self):
        return HtmlPage()

    @pytest.mark.slow
    def test_fetch_login_page(self, html_page1):
        user = User(os.environ["USER1"])
        html_page1.fetch_login_page(Library.LIBRALY_HOME_URL, user)
