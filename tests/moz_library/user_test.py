import os
import pytest
from dotenv import load_dotenv
from moz_library.user import User


class TestUser:
    def setup(self):
        load_dotenv(verbose=True)

    @pytest.mark.skip(reason="環境変数USER1のフォーマット変更が終わるまでとりあえず")
    def test_user(self):
        data_json = os.environ["USER1"]
        user = User(data_json)
        assert user.name == "Foo"
        assert user.disp_name == "foo"
