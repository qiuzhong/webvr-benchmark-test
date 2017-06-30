import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions
chrome_options.binary_location = 'C:\Users\test\Desktop\chromium_webvr1.1_20170628\chrome.exe'
driver = webdriver.Chrome(executable_path='C:\Users\haoyunfe\Documents\chromedriver.exe', chrome_options=chrome_options)  # Optional argument, if not specified will search path.
driver.get('http://wp-27.sh.intel.com/workspace/project/readonly/webbench/webgl/webglsamples/aquarium/aquarium-mod.html');
time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
