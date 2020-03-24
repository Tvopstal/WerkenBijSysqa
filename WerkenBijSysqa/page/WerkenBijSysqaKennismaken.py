from .BasePage import BasePage
from .locator import locator as loc
import subprocess, sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging, time
import driver
import data

class WerkenBijSysqaKennismaken (BasePage):

    def open_sysqa_kennismaken_pagina (self):
        link = data.werkenBijSysqaPaginaKennismakenFooter
        logging.info(f"Startpagina WerkenbijSysqa wordt geopend:{link}")
        self.driver.get(link) 

    def check_kennismaken_slogan (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken slogan correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_SLOGAN))
        element3 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_SLOGAN))
        if element == True:
            print("CORRECT: Kennismaken slogan is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.kennismakenSlogan:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Kennismaken slogan is niet aanwezig op pagina")

    def check_kennismaken_naam_text (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken naam text correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_NAAM_TEXT))
        element3 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_NAAM_TEXT))
        if element == True:
            print("CORRECT: Kennismaken naam text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.kennismakenFormulierNaam:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Kennismaken naam text is niet aanwezig op pagina")

    def check_kennismaken_naam_box (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken naam box correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_NAAM_BOX))
        element2 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_NAAM_BOX))
        if element == True:
            print("CORRECT: Kennismaken naam box is aanwezig op pagina")
            self.schrijf(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_NAAM_BOX, "Thijs van Opstal")
            naam = element2.get_attribute("value")
            print(naam)
            if naam == ("Thijs van Opstal"):
                print("CORRECT: Kennismaken naam box werkt correct")
            else:
                print("ERROR: Kennismaken naam box werkt niet correct")
        else:
            print("ERROR: Kennismaken naam box is niet aanwezig op pagina")
            
    def check_kennismaken_email_text (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken email text correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_EMAIL_TEXT))
        element3 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_EMAIL_TEXT))
        if element == True:
            print("CORRECT: Kennismaken email text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.kennismakenFormulierEmail:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Kennismaken email text is niet aanwezig op pagina")

    def check_kennismaken_email_box (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken email box correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_EMAIL_BOX))
        element2 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_EMAIL_BOX))
        if element == True:
            print("CORRECT: Kennismaken email box is aanwezig op pagina")
            self.schrijf(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_EMAIL_BOX, "tvanopstal@sysqa.nl")
            naam = element2.get_attribute("value")
            print(naam)
            if naam == ("tvanopstal@sysqa.nl"):
                print("CORRECT: Kennismaken email box werkt correct")
            else:
                print("ERROR: Kennismaken email box werkt niet correct")
        else:
            print("ERROR: Kennismaken email box is niet aanwezig op pagina")

    def check_kennismaken_bericht_text (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken Bericht text correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_BERICHT_TEXT))
        element3 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_BERICHT_TEXT))
        if element == True:
            print("CORRECT: Kennismaken Bericht text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.kennismakenFormulierBericht:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Kennismaken Bericht text is niet aanwezig op pagina")

    def check_kennismaken_bericht_box (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken bericht box correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_BERICHT_BOX))
        element2 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_BERICHT_BOX))
        if element == True:
            print("CORRECT: Kennismaken bericht box is aanwezig op pagina")
            self.schrijf(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_BERICHT_BOX, "Test bericht")
            naam = element2.get_attribute("value")
            print(naam)
            if naam == ("Test bericht"):
                print("CORRECT: Kennismaken bericht box werkt correct")
            else:
                print("ERROR: Kennismaken bericht box werkt niet correct")
        else:
            print("ERROR: Kennismaken bericht box is niet aanwezig op pagina")

    def check_kennismaken_voorwaarden_text (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Kennismaken voorwaarden correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_VOORWAARDEN_CHECKBOX))
        element2 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_VOORWAARDEN_LINK))
        element3 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_VOORWAARDEN_TEXT))
        if element == True:
            print("CORRECT: Kennismaken voorwaarden checkbox is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_VOORWAARDEN_CHECKBOX) == True:
                print ("CORRECT: Kennismaken voorwaarden checkbox is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_VOORWAARDEN_CHECKBOX) == False:
                print ("ERROR: Kennismaken voorwaarden checkbox is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Kennismaken voorwaarden checkbox is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_VOORWAARDEN_TEXT))
        text = element3.text
        if text == data.kennismakenFormulierVoorwaarden:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_kennismaken_updates_slogan (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken updates slogan correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_UPDATES_SLOGAN))
        element3 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_UPDATES_SLOGAN))
        if element == True:
            print("CORRECT: Kennismaken updates slogan is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.kennismakenUpdatesSlogan:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Kennismaken updates slogan is niet aanwezig op pagina")

    def check_kennismaken_updates_text (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken updates text correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_UPDATES_TEXT))
        element3 = (self.find(loc.WerkenBijSysqaKennismakenGUI.SYSQA_KENNISMAKEN_UPDATES_TEXT))
        if element == True:
            print("CORRECT: Kennismaken updates text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.kennismakenUpdatesText:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Kennismaken updates text is niet aanwezig op pagina")

    




























































