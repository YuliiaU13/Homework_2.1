import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = Chrome()
driver.get("http://localhost:8000/dz.html")


def verify_frame(frame_id, input_id, secret_text):
    driver.switch_to.frame(frame_id)
    time.sleep(1)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    driver.find_element(By.ID, input_id).send_keys(secret_text)
    time.sleep(1)

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    alert = Alert(driver)
    alert_text = alert.text
    if "Верифікація пройшла успішно!" in alert_text:
        print(f"{frame_id}: Успішна верифікація")
    else:
        print(f"{frame_id}: Верифікацію не пройдено")
    alert.accept()
    driver.switch_to.default_content()


verify_frame("frame1", "input1", "Frame1_Secret")
verify_frame("frame2", "input2", "Frame2_Secret")
verify_frame("frame2", "input2", "+")

driver.quit()
