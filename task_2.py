# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep


@pytest.fixture
def driver():
    dv = webdriver.Chrome()
    yield dv
    dv.quit()


def test(driver):
    url = "https://test-online.sbis.ru/"
    driver.get(url)
    driver.maximize_window()
    sleep(2)
    login, password = driver.find_elements(By.CSS_SELECTOR, '[name="ws-input_2024-10-08"]')

    login.send_keys("Демо_тензор", Keys.ENTER)
    password.send_keys("Демо123", Keys.ENTER)
    sleep(10)

    action = ActionChains(driver)

    c = driver.find_elements(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')

    action.move_to_element(c[0])
    action.perform()
    sleep(2)

    a = driver.find_elements(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion-AddButton__button"]')
    action.click(a[0])
    action.perform()
    sleep(2)

    contact = driver.find_elements(By.CSS_SELECTOR, '.controls-TileView__item_roundBorder_topLeft_s .msg-addressee-selector__addressee')
    contact[0].click()
    sleep(2)

    text = driver.find_element(By.CSS_SELECTOR, ".textEditor_Viewer__Paragraph")
    text.send_keys("message")
    sleep(2)

    but = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    but.click()
    sleep(2)

    txt = driver.find_element(By.CSS_SELECTOR, '.msg-entity-layout__message-content')
    assert txt.is_displayed()
    action.context_click(txt)
    action.perform()
    sleep(2)

    dell = driver.find_elements(By.CSS_SELECTOR, ".controls-Menu__content-wrapper_width")[-1]
    dell.click()
    sleep(2)

    yes = driver.find_elements(By.CSS_SELECTOR, ".controls-Button__text_viewMode-outlined")[0]
    yes.click()
    sleep(2)

    check = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationTemplate__main"]')
    assert check.is_displayed()
