'''Webdriver settings for the fps tool.
'''
import os


WEBDRIVER_TYPE = 'chromedriver'
WEBDRIVER_VER = '2.29'
WEBDRIVER_PREFIX = r'C:\dev\chromedriver'
WEBDRIVER_BINARY = 'chromedriver.exe'
WEBDRIVER_PATH = os.path.join(WEBDRIVER_PREFIX,  WEBDRIVER_VER, WEBDRIVER_BINARY)

WEBGL_SAMPLE_URL = r'http://wp-27.sh.intel.com/workspace/project/readonly/webbench/webgl/webglsamples/aquarium/aquarium-mod.html'
SAMPLE_INITIALIZATION_TIME = 5