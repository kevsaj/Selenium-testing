from selenium import webdriver



class WorkBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://app.daily.dev/")
        self.driver.find_element_by_css_selector("#cheese #cheddar")
  
        sleep(2)

WorkBot()