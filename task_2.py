# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    url = "https://fix-online.sbis.ru/"
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    action = ActionChains(driver)

    driver.get(url)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.controls-Render__placeholder')))

    login, password = driver.find_elements(By.CSS_SELECTOR, '.controls-Field')
    login.send_keys("sync_test_auto_1", Keys.ENTER)
    password.send_keys("Авто123", Keys.ENTER)

    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.highcharts-series.highcharts-tracker')))
    contacts = driver.find_elements(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')
    action.double_click(contacts[0])
    action.perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')))

    ms1 = int(driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-folders-counter_unread"').text)

    new_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    new_message.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.controls-StackTemplate__content-area [data-qa="FilterView__icon"]')))
    serch = driver.find_element(By.CSS_SELECTOR, '.controls-Field')
    serch.send_keys("Розница1 Автотестер Продавец")

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.controls-BaseControl .ws-flexbox.person-BaseInfo__content')))
    contact = driver.find_element(By.CSS_SELECTOR, '.controls-BaseControl .ws-flexbox.person-BaseInfo__content')
    contact.click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')))
    fild = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    fild.send_keys("message")

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')))
    send = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    action.click(send)
    action.perform()

    sleep(1)
    ms2 = int(driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-folders-counter_unread"').text)
    assert ms2 > ms1

    ms = driver.find_elements(By.CSS_SELECTOR, '[data-qa="items-container"] [data-qa="item"]')
    action.context_click(ms[1])
    action.perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.controls-Menu__content-wrapper_width')))
    delete = driver.find_elements(By.CSS_SELECTOR, ".controls-Menu__content-wrapper_width")
    delete[-1].click()

    sleep(1)
    ms3 = int(driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-folders-counter_unread"').text)
    assert ms3 == ms1

