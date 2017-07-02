import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# enable browser logging
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }

#chrome_options = webdriver.ChromeOptions
webdriver.chrome.options.binary_location = r'C:\Users\test\Desktop\chromium_webvr1.1_20170628\chrome.exe'

#driver = webdriver.Chrome(executable_path=r'C:\dev\chromedriver\2.29\chromedriver.exe', chrome_options=chrome_options, desired_capabilities=d)
driver = webdriver.Chrome(executable_path=r'C:\dev\chromedriver\2.29\chromedriver.exe', desired_capabilities=d)
driver.get('http://wp-27.sh.intel.com/workspace/project/readonly/webbench/webgl/webglsamples/aquarium/aquarium-mod.html');
#for entry in driver.get_log('browser'):
#    print entry
time.sleep(5) # Let the user actually see something!
while True:
    fps = driver.find_element_by_id('fps').get_attribute('innerText')
    print fps
    time.sleep(1)
    

#time.sleep(5) # Let the user actually see something!
#driver.quit()
