import os
import logging
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from moz_library.user import User


class HtmlPage:
    def __init__(self) -> None:
        logging.debug("driver.create/start")
        options = ChromeOptions()
        binary_location = os.environ.get("CHROME_BINARY_LOCATION", None)
        if not (binary_location is None):
            options.binary_location = binary_location
        # 必須
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--single-process")
        # options.add_argument("--disable-setuid-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # エラーの許容
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-web-security")
        # headlessでは不要そうな機能
        options.add_argument("--disable-desktop-notifications")
        options.add_argument("--disable-extensions")
        # UA
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"  # noqa
        options.add_argument("--user-agent=" + user_agent)
        # 言語
        options.add_argument("--lang=ja")
        # 画像を読み込まないで軽くする
        options.add_argument("--blink-settings=imagesEnabled=false")

        # chromedriver生成
        executable_path = os.environ.get("CHROME_DRIVER_LOCATION", None)
        self.driver = Chrome(options=options, executable_path=executable_path)
        logging.debug("driver.create/end")

    def _wait(self) -> None:
        WebDriverWait(self.driver, 10, poll_frequency=0.05).until(
            ec.presence_of_all_elements_located
        )

    def _wait_element(self, target):
        element = WebDriverWait(self.driver, 10, poll_frequency=0.05).until(
            ec.presence_of_element_located(target)
        )

        return element

    def _login(self, login_url: str, user: User) -> None:
        logging.debug("[0] login start. : user.name={}, url={}".format(user.name, login_url))

        self.driver.get(login_url)
        logging.debug("[1] driver.get done.")

        self._wait()
        logging.debug("[2] wait done.")

        # ログインボタン押下
        uid = self._wait_element((By.NAME, "usercardno"))
        password = self._wait_element((By.NAME, "userpasswd"))
        uid.send_keys(user.id)
        password.send_keys(user.password)
        logging.debug("[3] send keys done.")
        button = self._wait_element((By.NAME, "Login"))
        logging.debug("[4] button element located done.")
        button.click()
        logging.debug("[5] button click done.")

        # ロードされたかを確認
        self._wait_element((By.NAME, "FormLEND"))
        logging.debug("[6] load all wait done.")
        logging.debug("[7] login end.")

    def fetch_login_page(self, login_url: str, user: User) -> str:
        self._login(login_url, user)
        logging.debug("driver.page_source.encode/start")
        html = self.driver.page_source.encode("utf-8")
        logging.debug("driver.page_source.encode/end")
        return html

    def release_resource(self) -> None:
        logging.debug("driver.quit/start")
        self.driver.quit()
        logging.debug("driver.quit/end")
