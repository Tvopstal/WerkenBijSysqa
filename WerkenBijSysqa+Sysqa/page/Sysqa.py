from .BasePage import BasePage
from .locator import locator as loc
import subprocess, sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging, time
import driver
import data


class WerkenBijSysqa (BasePage):

    def open_sysqa_pagina (self):
        link = data.sysqaHomePagina
        logging.info(f"Startpagina Sysqa wordt geopend:{link}")
        self.driver.get(link) 

    def check_navigatie_sysqa_logo (self, link_URL):
        logging.info("Er wordt gecontroleerd of het Sysqa logo correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NAV_LOGO))
        if element == True:
            print("CORRECT: Sysqa Logo is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_LOGO) == True:
                print ("CORRECT: Sysqa Logo is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_LOGO) == False:
                print ("ERROR: Sysqa Logo is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa Logo is niet aanwezig op pagina")
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NAV_LOGO))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")

            