# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
import time
import pytest

path = "C:\\Users\\safon\\Downloads"


def get_files(folder_path=path):
    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
        ]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
    return files


def wait_for_dowload(timeout=20):
    start_time = time.time()

    while time.time() - start_time < timeout:
        files = get_files()
        extension_file = files[-1].split(".")[-1]
        if extension_file != "crdownload" and extension_file != "tmp":
            return True
        sleep(1)

    return False


def get_size():
    file = get_files()[-1]
    size = os.path.getsize(f"{path}\\{file}")
    return f"{size // (1024 * 1024)}МБ"


@pytest.fixture
def driver():
    dv = webdriver.Chrome()
    yield dv
    dv.quit()


def test(driver):
    url = "https://sbis.ru/"
    driver.get(url)
    sleep(2)

    local_versions = driver.find_element(By.CSS_SELECTOR, '[href="/download"]')
    local_versions.click()

    dowload = driver.find_elements(By.CSS_SELECTOR, '.sbis_ru-DownloadNew-loadLink__link')[0]
    dowload.click()

    assert wait_for_dowload(30)

    print("\n" + get_size())

