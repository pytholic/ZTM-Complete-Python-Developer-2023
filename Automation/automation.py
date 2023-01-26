from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    return chrome_options


def launchBrowser():
    service = Service(executable_path="./chromedriver")
    options = get_options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
    return driver


if __name__ == "__main__":
    driver = launchBrowser()
    assert "Selenium Easy Demo" in driver.title
    show_message_button = driver.find_element(By.CLASS_NAME, "btn-default")
    # show_message_button2 = driver.find_element(By.CSS_SELECTOR, "#get-input > .btn")
    # print(show_message_button.get_attribute("innerHTML"))
    # print(show_message_button2.get_attribute("innerHTML"))

    assert "Show Message" in driver.page_source

    # Write text in field
    user_message = driver.find_element(By.ID, "user-message")
    user_message.clear()
    user_message.send_keys("I am extra cool!")

    # Clicking on button
    show_message_button.click()

    output_message = driver.find_element(By.ID, "display")
    # print(output_message.text)
    assert "I am extra cool!" == output_message.text

    # driver.close()  # close current window
    driver.quit()  # close entire driver
