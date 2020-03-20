from .BasePage import BasePage
from .locator import locator as loc
import subprocess, sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging, time
import driver
import data

class WerkenBijSysqaVacatures (BasePage):

    def open_sysqa_vacature_pagina (self):
        link = data.werkenBijSysqaPaginaVacatures
        logging.info(f"Startpagina WerkenbijSysqa wordt geopend:{link}")
        self.driver.get(link) 

    def check_slogan_1 (self):
        logging.info("Er wordt gecontroleerd of de Vacatures slogan 1 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_SLOGAN_1))
        if element == True:
            print("CORRECT: Vacatures slogan 1 is aanwezig op pagina")
            element3 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_SLOGAN_1))
            print(element3.text)
            if element3.text == data.vacatureSlogan1:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        elif element == False:
            print ("ERROR: Vacatures slogan 1 is niet aanwezig op pagina")
        
    def check_slogan_2 (self):
        logging.info("Er wordt gecontroleerd of de Vacatures slogan 2 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_SLOGAN_2))
        if element == True:
            print("CORRECT: Vacatures slogan 2 is aanwezig op pagina")
            element3 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_SLOGAN_2))
            print(element3.text)
            if element3.text == data.vacatureSlogan2:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        elif element == False:
            print ("ERROR: Vacatures slogan 2 is niet aanwezig op pagina")

    def check_bekijk_vacature_button_1 (self):
        logging.info("Er wordt gecontroleerd of de Bekijk vacature button 1 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_1))
        if element == True:
            print("CORRECT: Bekijk vacature button 1 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_1) == True:
                print ("CORRECT: Bekijk vacature button 1 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_1) == False:
                print ("ERROR: Bekijk vacature button 1 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Bekijk vacature button 1 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_1))
        print(element3.text)
        if element3.text == data.bekijkDezeVactureButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_bekijk_vacature_button_2 (self):
        logging.info("Er wordt gecontroleerd of de Bekijk vacature button 2 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_2))
        if element == True:
            print("CORRECT: Bekijk vacature button 2 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_2) == True:
                print ("CORRECT: Bekijk vacature button 2 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_2) == False:
                print ("ERROR: Bekijk vacature button 2 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Bekijk vacature button 2 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_2))
        print(element3.text)
        if element3.text == data.bekijkDezeVactureButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_bekijk_vacature_button_3 (self):
        logging.info("Er wordt gecontroleerd of de Bekijk vacature button 3 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_3))
        if element == True:
            print("CORRECT: Bekijk vacature button 3 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_3) == True:
                print ("CORRECT: Bekijk vacature button 3 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_3) == False:
                print ("ERROR: Bekijk vacature button 3 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Bekijk vacature button 3 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_3))
        print(element3.text)
        if element3.text == data.bekijkDezeVactureButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_bekijk_vacature_button_4 (self):
        logging.info("Er wordt gecontroleerd of de Bekijk vacature button 4 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_4))
        if element == True:
            print("CORRECT: Bekijk vacature button 4 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_4) == True:
                print ("CORRECT: Bekijk vacature button 4 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_4) == False:
                print ("ERROR: Bekijk vacature button 4 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Bekijk vacature button 4 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_4))
        print(element3.text)
        if element3.text == data.bekijkDezeVactureButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_bekijk_vacature_button_5 (self):
        logging.info("Er wordt gecontroleerd of de Bekijk vacature button 5 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_5))
        if element == True:
            print("CORRECT: Bekijk vacature button 5 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_5) == True:
                print ("CORRECT: Bekijk vacature button 5 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_5) == False:
                print ("ERROR: Bekijk vacature button 5 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Bekijk vacature button 5 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_5))
        print(element3.text)
        if element3.text == data.bekijkDezeVactureButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_bekijk_vacature_button_6 (self):
        logging.info("Er wordt gecontroleerd of de Bekijk vacature button 6 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_6))
        if element == True:
            print("CORRECT: Bekijk vacature button 6 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_6) == True:
                print ("CORRECT: Bekijk vacature button 6 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_6) == False:
                print ("ERROR: Bekijk vacature button 6 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Bekijk vacature button 6 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_BEKIJK_VACATURE_6))
        print(element3.text)
        if element3.text == data.bekijkDezeVactureButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_kennismaken_slogan (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken slogan correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_KENNISMAKEN_SLOGAN))
        if element == True:
            print("CORRECT: Kennismaken slogan is aanwezig op pagina")
            element3 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_KENNISMAKEN_SLOGAN))
            print(element3.text)
            if element3.text == data.kennismakenSlogan:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        elif element == False:
            print ("ERROR: Kennismaken slogan is niet aanwezig op pagina")

    def check_kennismaken_button_midden (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Kennismaken midden button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_KENNISMAKEN_BUTTON_MIDDEN))
        if element == True:
            print("CORRECT: Kennismaken midden button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_KENNISMAKEN_BUTTON_MIDDEN) == True:
                print ("CORRECT: Kennismaken midden button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_KENNISMAKEN_BUTTON_MIDDEN) == False:
                print ("ERROR: Kennismaken midden button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Kennismaken midden button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_KENNISMAKEN_BUTTON_MIDDEN))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaVacaturesGUI.SYSQA_VACATURES_KENNISMAKEN_BUTTON_MIDDEN))
        text = element3.text
        if text == data.kennismakenVacaturesMiddenButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    
