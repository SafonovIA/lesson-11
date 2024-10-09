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
    url = "https://test-online.sbis.ru/"
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    action = ActionChains(driver)

    driver.get(url)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.controls-Render__placeholder')))

    login, password = driver.find_elements(By.CSS_SELECTOR, '.controls-Field')
    login.send_keys("Демо_тензор", Keys.ENTER)
    password.send_keys("Демо123", Keys.ENTER)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')))
    sleep(2)
    contacts = driver.find_elements(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')
    action.double_click(contacts[0])
    action.perform()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.controls-padding_left-m.tw-w-full.msg-person-tile-new')))

    contact = driver.find_element(By.CSS_SELECTOR, '.controls-padding_left-m.tw-w-full.msg-person-tile-new')
    action.context_click(contact)
    action.perform()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.controls-Menu__content.controls-Menu__content_align_right')))
    message = driver.find_element(By.CSS_SELECTOR, '.controls-Menu__content.controls-Menu__content_align_right')

    message.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')))
    text_fild = driver.find_element(By.CSS_SELECTOR, ".textEditor_Viewer__Paragraph")
    text_fild.send_keys("message")

    send = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')))
    action.click(send)
    action.perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.msg-entity-layout__message-content')))
    text = driver.find_element(By.CSS_SELECTOR, '.msg-entity-layout__message-content')
    assert text.is_displayed()
    sleep(1)
    action.context_click(text)
    action.perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.controls-Menu__content-wrapper_width')))
    delete = driver.find_elements(By.CSS_SELECTOR, ".controls-Menu__content-wrapper_width")[-1]
    sleep(1)
    delete.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.controls-Button__text_viewMode-outlined')))
    yes = driver.find_elements(By.CSS_SELECTOR, ".controls-Button__text_viewMode-outlined")[0]
    sleep(1)
    yes.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="controls-ConfirmationTemplate__main"]')))
    check = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationTemplate__main"]')
    assert check.is_displayed()
    sleep(1)

