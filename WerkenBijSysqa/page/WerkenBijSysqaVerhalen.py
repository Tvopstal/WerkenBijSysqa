from .BasePage import BasePage
from .locator import locator as loc
import subprocess, sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging, time
import driver
import data

class WerkenBijSysqaVerhalen (BasePage):

    def open_sysqa_verhalen_pagina (self):
        link = data.werkenBijSysqaPaginaVerhalenEnVideos
        logging.info(f"Startpagina WerkenbijSysqa wordt geopend:{link}")
        self.driver.get(link) 

    def check_verhalen_slogan_1 (self):
        logging.info("Er wordt gecontroleerd of de Verhalen slogan 1 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SLOGAN_1))
        if element == True:
            print("CORRECT: Verhalen slogan 1 is aanwezig op pagina")
            element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SLOGAN_1))
            print(element3.text)
            if element3.text == data.verhalenSlogan1:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        elif element == False:
            print ("ERROR: Verhalen slogan 1 is niet aanwezig op pagina")

    def check_verhalen_slogan_2 (self):
        logging.info("Er wordt gecontroleerd of de Verhalen slogan 2 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SLOGAN_2))
        if element == True:
            print("CORRECT: Verhalen slogan 2 is aanwezig op pagina")
            element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SLOGAN_2))
            print(element3.text)
            if element3.text == data.verhalenSlogan2:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        elif element == False:
            print ("ERROR: Verhalen slogan 2 is niet aanwezig op pagina")

    def check_verhalen_search_bar (self):
        logging.info("Er wordt gecontroleerd of de Verhalen Search Bar correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SEARCH_BOX))
        if element == True:
            print("CORRECT: Verhalen Search Bar is aanwezig op pagina")
        elif element == False:
            print ("ERROR: Verhalen Search Bar is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SEARCH_BOX))
        text = element2.get_attribute("placeholder")
        print (text)
        if text == data.verhalenSearchbarText:
            print ("CORRECT: Text is correct")
        else:
            print ("ERROR: Text is niet correct")

    def check_verhalen_search_button (self):
        logging.info("Er wordt gecontroleerd of de Verhalen Search button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SEARCH_BUTTON))
        if element == True:
            print("CORRECT: Verhalen Search button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SEARCH_BUTTON) == True:
                print ("CORRECT: Verhalen Search button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SEARCH_BUTTON) == False:
                print ("ERROR: Verhalen Search button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Verhalen Search button is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SEARCH_BUTTON))
        text = element3.text
        if text == data.verhalenSearchButtonText:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_verhalen_onderwerp_titel (self):
        logging.info("Er wordt gecontroleerd of de Onderwerp Titel correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_TITEL))
        if element == True:
            print("CORRECT: Onderwerp Titel is aanwezig op pagina")
            element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_TITEL))
            print(element3.text)
            if element3.text == data.verhalenOnderwerpTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        elif element == False:
            print ("ERROR: Onderwerp Titel is niet aanwezig op pagina")
        
    def check_verhalen_onderwerp_button_1 (self):
        logging.info("Er wordt gecontroleerd of de Onderwerp button 1 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_1))
        if element == True:
            print("CORRECT: Onderwerp button 1 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_1) == True:
                print ("CORRECT: Onderwerp button 1 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_1) == False:
                print ("ERROR: Onderwerp button 1 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Onderwerp button 1 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_1))
        text = element3.text
        if text == data.verhalenOnderwerp1:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")
    
    def check_verhalen_onderwerp_button_2 (self):
        logging.info("Er wordt gecontroleerd of de Onderwerp button 2 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_2))
        if element == True:
            print("CORRECT: Onderwerp button 2 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_2) == True:
                print ("CORRECT: Onderwerp button 2 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_2) == False:
                print ("ERROR: Onderwerp button 2 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Onderwerp button 2 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_2))
        text = element3.text
        if text == data.verhalenOnderwerp2:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")
        
    def check_verhalen_onderwerp_button_3 (self):
        logging.info("Er wordt gecontroleerd of de Onderwerp button 3 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_3))
        if element == True:
            print("CORRECT: Onderwerp button 3 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_3) == True:
                print ("CORRECT: Onderwerp button 3 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_3) == False:
                print ("ERROR: Onderwerp button 3 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Onderwerp button 3 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_3))
        text = element3.text
        if text == data.verhalenOnderwerp3:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_verhalen_onderwerp_button_4 (self):
        logging.info("Er wordt gecontroleerd of de Onderwerp button 4 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_4))
        if element == True:
            print("CORRECT: Onderwerp button 4 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_4) == True:
                print ("CORRECT: Onderwerp button 4 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_4) == False:
                print ("ERROR: Onderwerp button 4 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Onderwerp button 4 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_4))
        text = element3.text
        if text == data.verhalenOnderwerp4:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_verhalen_onderwerp_button_5 (self):
        logging.info("Er wordt gecontroleerd of de Onderwerp button 5 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_5))
        if element == True:
            print("CORRECT: Onderwerp button 5 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_5) == True:
                print ("CORRECT: Onderwerp button 5 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_5) == False:
                print ("ERROR: Onderwerp button 5 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Onderwerp button 5 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_5))
        text = element3.text
        if text == data.verhalenOnderwerp5:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_verhalen_onderwerp_button_6 (self):
        logging.info("Er wordt gecontroleerd of de Onderwerp button 6 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_6))
        if element == True:
            print("CORRECT: Onderwerp button 6 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_6) == True:
                print ("CORRECT: Onderwerp button 6 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_6) == False:
                print ("ERROR: Onderwerp button 6 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Onderwerp button 6 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_ONDERWERP_6))
        text = element3.text
        if text == data.verhalenOnderwerp6:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")
            
    def check_verhalen_onderwerp_laad_button (self):
        logging.info("Er wordt gecontroleerd of de Onderwerp laad meer button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_LAAD_MEER_BUTTON))
        if element == True:
            print("CORRECT: Onderwerp laad meer button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_LAAD_MEER_BUTTON) == True:
                print ("CORRECT: Onderwerp laad meer button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_LAAD_MEER_BUTTON) == False:
                print ("ERROR: Onderwerp laad meer button is niet aanklikbaar")
        elif element == False:
            print ("ERROR:Onderwerp laad meer button is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_LAAD_MEER_BUTTON))
        text = element3.text
        if text == data.verhalenOnderwerpLaadMeer:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")
    
    def check_verhalen_kennismaken_slogan_midden (self):
        logging.info("Er wordt gecontroleerd of de Kennismaken slogan correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SLOGAN_1))
        if element == True:
            print("CORRECT: Kennismaken slogan is aanwezig op pagina")
            element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_SLOGAN_1))
            print(element3.text)
            if element3.text == data.kennisMakenTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        elif element == False:
            print ("ERROR: Kennismaken slogan is niet aanwezig op pagina")

    def check_verhalen_kennismaken_button_midden (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Kennismaken midden button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_KENNISMAKEN_BUTTON_MIDDEN))
        if element == True:
            print("CORRECT: Kennismaken midden button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_KENNISMAKEN_BUTTON_MIDDEN) == True:
                print ("CORRECT: Kennismaken midden button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_KENNISMAKEN_BUTTON_MIDDEN) == False:
                print ("ERROR: Kennismaken midden button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Kennismaken midden button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_KENNISMAKEN_BUTTON_MIDDEN))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_KENNISMAKEN_BUTTON_MIDDEN))
        text = element3.text
        if text == data.kennismakenButtonZijkant:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_verhalen_vacature_slogan (self):
        logging.info("Er wordt gecontroleerd of de Vacature slogan correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_SLOGAN))
        if element == True:
            print("CORRECT: Vacature slogan is aanwezig op pagina")
            element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_SLOGAN))
            print(element3.text)
            if element3.text == data.verhalenVacatureSlogan:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        elif element == False:
            print ("ERROR: Vacature slogan is niet aanwezig op pagina")

    def check_verhalen_vacature_1 (self):
        logging.info("Er wordt gecontroleerd of de Vacature button 1 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_1))
        if element == True:
            print("CORRECT: Vacature button 1 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_1) == True:
                print ("CORRECT: Vacature button 1 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_1) == False:
                print ("ERROR: Vacature button 1 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Vacature button 1 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_1))
        text = element3.text
        if text == data.bekijkDezeVactureButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_verhalen_vacature_2 (self):
        logging.info("Er wordt gecontroleerd of de Vacature button 2 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_2))
        if element == True:
            print("CORRECT: Vacature button 2 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_2) == True:
                print ("CORRECT: Vacature button 2 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_2) == False:
                print ("ERROR: Vacature button 2 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Vacature button 2 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_2))
        text = element3.text
        if text == data.bekijkDezeVactureButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_verhalen_vacature_3 (self):
        logging.info("Er wordt gecontroleerd of de Vacature button 3 correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_3))
        if element == True:
            print("CORRECT: Vacature button 3 is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_3) == True:
                print ("CORRECT: Vacature button 3 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_3) == False:
                print ("ERROR: Vacature button 3 is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Vacature button 3 is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_3))
        text = element3.text
        if text == data.bekijkDezeVactureButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_verhalen_vacature_laad_meer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Vacature Laad meer button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_LAAD_MEER))
        element2 = (self.find(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_LAAD_MEER))
        if element == True:
            print("CORRECT: Vacature Laad meer button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_LAAD_MEER) == True:
                print ("CORRECT: Vacature Laad meer button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaVerhalenGUI.SYSQA_VERHALEN_VACATURE_LAAD_MEER) == False:
                print ("ERROR: Vacature Laad meer button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Vacature Laad meer button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.bekijkAlOnzeVacaturesButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")
















