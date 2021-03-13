class WorkBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://app.daily.dev/")
        self.WebDriverWait(self.driver).until(document_initialised)
        el = self.driver.find_element_by_xpath("/html/body/div/main/div/article/a")
        # names = [name.text for name in el if name != '']
        for e in el:
            print(el)
  
        

WorkBot()

class WorkBot:
    def __init__(self, timeout=None):
        options = Options()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://app.daily.dev/')

        elements = WebDriverWait(self.driver).until(lambda d: d.find_element_by_tag_name("article"))

        for e in elements:
            print(e.text)
  
        # WebDriverWait(self.driver).until(self.document_initialised)
        # self.wait = WebDriverWait(self.driver, 10)
        # self.driver.implicitly_wait(60)
        # divElement = self.driver.find_element_by_css_selector("#cards_title__1SQYH")
        # str = divElement.getText()
        # self.System.out.println(str)
        
  
        

WorkBot()