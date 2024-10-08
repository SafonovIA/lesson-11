# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture
def driver():
    dv = webdriver.Chrome()
    yield dv
    dv.quit()


def test(driver):
    url = "https://sbis.ru/"
    driver.get(url)
    assert driver.current_url == url

    contacts = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    assert contacts.is_displayed()

    contacts.click()
    tensor = driver.find_element(By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")
    assert tensor.is_displayed()

    tensor.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == "https://tensor.ru/"

    block = driver.find_elements(By.CSS_SELECTOR, ".tensor_ru-Index__card-title")[1]
    assert block.is_displayed()

    about = driver.find_elements(By.CSS_SELECTOR, ".tensor_ru-link")[1]
    assert about.is_displayed()

    about.click()
    assert driver.current_url == "https://tensor.ru/about"
