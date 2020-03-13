import unittest, logging, time, sys, data, driver, page, os
import platform, base64, configparser

class CommonTestCase(unittest.TestCase):
    pipeline = "local"
    def setUp(self):
        self.testcase = "setup"
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')

        logging.info('Starting Driver') 
        if self.pipeline =="local":
            self.driver = driver.Driver_Chrome()
            self.driver.set_window_size(1920, 1080)
        elif self.pipeline =="jenkins":
            self.driver = driver.Driver_FF_headless()
            self.driver.set_window_size(1920, 1080) 
        
        logging.info('Adding Cleanup Steps')
        self.addCleanup(self.driver.quit)
        self.addCleanup(self.screenshot)

    def screenshot(self):
        for error in self._outcome.errors:
            if error[1]:
                naam = self.testcase
                if not os.path.isdir("./workspace"):
                    os.mkdir("./workspace")
                self.driver.get_screenshot_as_file(f"./workspace/{naam}.png")

    def tearDown(self):
        pass