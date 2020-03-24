from selenium import webdriver
from selenium.webdriver import Ie, IeOptions
from selenium.webdriver.ie.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import logging, data

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# class Driver (webdriver.Firefox):
#     def __init__(self, waittime=60, firefox_binary="C:\\Program Files\\Mozilla Firefox66\\firefox.exe"):
#         opts = Options()
#         # opts.add_experimental_option("detach", True)
#         # opts.add_extension("C:\\Users\\ADM-AD-VOSM04\\Desktop\\MARS2MV\\TOPDeskRepo\\ChroPath_v5.0.3.crx")
#         super().__init__(options=opts)
#         self.wait = WebDriverWait(self, waittime)
#         self.actions = ActionChains(self)

# if __name__ == "__main__":
#     driver = webdriver.Firefox()

# class Driver_FF_screen (webdriver.Firefox):
#     def __init__(self):
#         logging.info("Setting Driver Options")
#         opts = Options()
#         # opts.add_experimental_option("detach", True)
#         # opts.add_extension("C:\\Users\\ADM-AD-VOSM04\\Desktop\\MARS2MV\\TOPDeskRepo\\ChroPath_v5.0.3.crx")
#         super().__init__(options=opts, service_log_path='nul', timeout = 90, firefox_binary="C:\\Program Files\\Mozilla Firefox66\\firefox.exe")
#         #ignored_exceptions=data.ignored_exceptions
#         waittime=60
#         self.wait = WebDriverWait(self, waittime)
#         self.actions = ActionChains(self)
    
class Driver_FF_headless (webdriver.Firefox):
    def __init__(self):
        logging.info("Setting Driver Options")
        opts = Options()
        opts.headless = False
        # opts.log.level = "info"
        # opts.add_experimental_option("detach", True)
        # opts.add_extension("C:\\Users\\ADM-AD-VOSM04\\Desktop\\MARS2MV\\TOPDeskRepo\\ChroPath_v5.0.3.crx")
        super().__init__()
        #,ignored_exceptions=data.ignored_exceptions
        waittime=20
        self.wait = WebDriverWait(self, waittime)
        self.wait_short = WebDriverWait(self, 5)
        self.actions = ActionChains(self)

class Driver_Chrome (webdriver.Chrome):
    def __init__(self):
        logging.info("Setting Driver Options")
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless")
        opts.headless = True
        # opts.add_extension("C:\\Users\\Michiel\\Desktop\\testInlog\\testInlog.crx")
        # opts.log.level = "info"
        # opts.add_experimental_option("detach", True)
        # opts.add_extension("C:\\Users\\mvos\\Desktop\\Drivers etc\\Drivers\\ChroPath.crx")
        super().__init__(options=opts)
        #,ignored_exceptions=data.ignored_exceptions
        waittime=20
        self.wait = WebDriverWait(self, waittime)
        self.wait_short = WebDriverWait(self, 5)
        self.actions = ActionChains(self)


# class Driver_Ie (webdriver.Ie):
#     def __init__(self, waittime=10):
#         opts = Options()
#         # opts.add_experimental_option("detach", true)
#         # opts.add_extension("c:\\users\\adm-ad-vosm04\\desktop\\mars2mv\\topdeskrepo\\chropath_v5.0.3.crx")
#         #opts.acceptInsecureCerts = True
#         #opts.introduce_flakiness_by_ignoring_security_domains = True
#         super().__init__(options=opts)
#         self.wait = WebDriverWait(self, waittime)
#         self.actions = ActionChains(self)

# class Driver_Chrome (webdriver.Chrome):
#     def __init__(self, waittime=50):
#         opts = ChromeOptions()
#         opts.add_experimental_option("detach", False)
#         opts.add_extension("C:\\Users\\Michiel\\Desktop\\testInlog\\testInlog.crx")
#         # opts.add_extension("C:\\Users\\ADM-AD-VOSM04\\Desktop\\MARS2MV\\TOPDeskRepo\\ChroPath_v5.0.3.crx")
#         super().__init__(options=opts)
#         self.wait = WebDriverWait(self, waittime)
#         self.actions = ActionChains(self)