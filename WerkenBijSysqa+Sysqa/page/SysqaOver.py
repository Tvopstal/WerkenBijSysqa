from .BasePage import BasePage
from .locator import locator as loc
import subprocess, sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging, time
import driver
import data


class SysqaOver (BasePage):

    def open_sysqa_pagina (self):
        link = data.sysqaOverOnsPagina
        logging.info(f"Startpagina Sysqa wordt geopend:{link}")
        self.driver.get(link) 