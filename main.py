from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import json
import pickle
f = open("testdata.json", "w")
i = open("images.json", "w")

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get('https://app.daily.dev/')

elements = WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements_by_tag_name("h3"))
images = WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements_by_tag_name("img"))

for e in elements:
    txt = e.text
    f.write("%s\n" % txt)

for e in images:
    source = e.get_attribute("src")
    with open('edit.json', 'wb') as fp:
        pickle.dump(source, fp)
    i.write("%s\n" % source)


# with open('edit.json', 'w') as dest_file:
#     with open('images.json', 'r') as source_file:
#         for line in source_file:
#             element = json.loads(line.strip())
#             if 'None' in element:
#                 del element['None']
#             dest_file.write(json.dumps(element))


f.close()