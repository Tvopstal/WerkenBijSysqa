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

    def check_sysqa_over_slogan (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over slogan correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_TITEL))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_TITEL))
        if element == True:
            print("CORRECT: Sysqa over slogan is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over slogan is niet aanwezig op pagina")

    def check_sysqa_over_contact_button_boven (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over contact boven button correct werkt")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_CONTACT_BOVEN))
        element2 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_CONTACT_BOVEN))
        if element == True:
            print("CORRECT: Sysqa over contact boven button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_CONTACT_BOVEN) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_CONTACT_BOVEN) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa over contact boven button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaContactPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaOverContactBoven:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_over_text (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over text correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_TEXT))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_TEXT))
        if element == True:
            print("CORRECT: Sysqa over text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverText:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over text is niet aanwezig op pagina")

    def check_sysqa_over_improving_slogan (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over improving slogan correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_IMPROVING_SLOGAN))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_IMPROVING_SLOGAN))
        if element == True:
            print("CORRECT: Sysqa over improving slogan is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverImprovingTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over improving slogan is niet aanwezig op pagina")

    def check_sysqa_over_improving_text_1 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over improving text 1 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_IMPROVING_TEXT_1))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_IMPROVING_TEXT_1))
        if element == True:
            print("CORRECT: Sysqa over improving text 1 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverImprovingText1:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over improving text 1 is niet aanwezig op pagina")

    def check_sysqa_over_improving_text_2 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over improving text 2 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_IMPROVING_TEXT_2))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_IMPROVING_TEXT_2))
        if element == True:
            print("CORRECT: Sysqa over improving text 2 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverImprovingText2:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over improving text 2 is niet aanwezig op pagina")

    def check_sysqa_over_specialisatie_1 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over specialisatie 1 correct werkt")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_1))
        element2 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_1))
        if element == True:
            print("CORRECT: Sysqa over specialisatie 1 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_1) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_1) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa over specialisatie 1 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaRequirementsPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaOverSpecialisatie1:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_over_specialisatie_2 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over specialisatie 2 correct werkt")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_2))
        element2 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_2))
        if element == True:
            print("CORRECT: Sysqa over specialisatie 2 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_2) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_2) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa over specialisatie 2 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaTestenPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaOverSpecialisatie2:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_over_specialisatie_3 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over specialisatie 3 correct werkt")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_3))
        element2 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_3))
        if element == True:
            print("CORRECT: Sysqa over specialisatie 3 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_3) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_3) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa over specialisatie 3 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaTestautomatiseringPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaOverSpecialisatie3:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_over_specialisatie_4 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over specialisatie 4 correct werkt")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_4))
        element2 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_4))
        if element == True:
            print("CORRECT: Sysqa over specialisatie 4 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_4) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_4) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa over specialisatie 4 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaAgilePagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaOverSpecialisatie4:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_over_specialisatie_5 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over specialisatie 5 correct werkt")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_5))
        element2 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_5))
        if element == True:
            print("CORRECT: Sysqa over specialisatie 5 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_5) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_5) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa over specialisatie 5 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaSecurityPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaOverSpecialisatie5:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_over_specialisatie_text (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over specialisatie text correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_TEXT))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_SPECIALISATIE_TEXT))
        if element == True:
            print("CORRECT: Sysqa over specialisatie text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverSpecialisatieText:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over specialisatie text is niet aanwezig op pagina")

    def check_sysqa_over_video_text (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over video text correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VIDEO_TEXT))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_VIDEO_TEXT))
        if element == True:
            print("CORRECT: Sysqa over video text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverVideoText:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over video text is niet aanwezig op pagina")

    def check_sysqa_over_video (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over video correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VIDEO))
        if element == True:
            print("CORRECT: Sysqa over video is aanwezig op pagina")
        else:
            print("ERROR: Sysqa over video is niet aanwezig op pagina")

    def check_sysqa_over_vakgebieden_titel (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over vakgebieden titel correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TITEL))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TITEL))
        if element == True:
            print("CORRECT: Sysqa over vakgebieden titel is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverVakgebiedenTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over vakgebieden titel is niet aanwezig op pagina")

    def check_sysqa_over_vakgebieden_text_1 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over vakgebieden text 1 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TEXT_1))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TEXT_1))
        if element == True:
            print("CORRECT: Sysqa over vakgebieden text 1 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverVakgebiedenText1:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over vakgebieden text 1 is niet aanwezig op pagina")
    
    def check_sysqa_over_vakgebieden_text_lijst_1 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over vakgebieden text lijst 1 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TEXT_LIJST_1))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TEXT_LIJST_1))
        if element == True:
            print("CORRECT: Sysqa over vakgebieden text lijst 1 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverVakgebiedenTextLijst1:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over vakgebieden text lijst 1 is niet aanwezig op pagina")

    def check_sysqa_over_vakgebieden_text_lijst_2 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over vakgebieden text lijst 2 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TEXT_LIJST_2))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TEXT_LIJST_2))
        if element == True:
            print("CORRECT: Sysqa over vakgebieden text lijst 2 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverVakgebiedenTextLijst2:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over vakgebieden text lijst 2 is niet aanwezig op pagina")
        
    def check_sysqa_over_vakgebieden_text_lijst_3 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over vakgebieden text lijst 3 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TEXT_LIJST_3))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TEXT_LIJST_3))
        if element == True:
            print("CORRECT: Sysqa over vakgebieden text lijst 3 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverVakgebiedenTextLijst3:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over vakgebieden text lijst 3 is niet aanwezig op pagina")

    def check_sysqa_over_vakgebieden_text_2 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over vakgebieden text 2 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TEXT_2))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_VAKGEBIEDEN_TEXT_2))
        if element == True:
            print("CORRECT: Sysqa over vakgebieden text 2 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverVakgebiedenText2:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over vakgebieden text 2 is niet aanwezig op pagina")

    def check_sysqa_over_professionals_titel (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over professionals titel correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_PROFESSIONALS_TITEL))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_PROFESSIONALS_TITEL))
        if element == True:
            print("CORRECT: Sysqa over professionals titel is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverProfessionalsTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over professionals titel is niet aanwezig op pagina")

    def check_sysqa_over_professionals_text (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over professionals text correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_PROFESSIONALS_TEXT))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_PROFESSIONALS_TEXT))
        if element == True:
            print("CORRECT: Sysqa over professionals text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverProfessionalsText:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over professionals text is niet aanwezig op pagina")

    def check_sysqa_over_dna_titel (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over dna titel correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_DNA_TITEL))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_DNA_TITEL))
        if element == True:
            print("CORRECT: Sysqa over dna titel is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverDnaTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over dna titel is niet aanwezig op pagina")

    def check_sysqa_over_dna_text (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over dna text correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_DNA_TEXT))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_DNA_TEXT))
        if element == True:
            print("CORRECT: Sysqa over dna text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverDnaText:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over dna text is niet aanwezig op pagina")

    def check_sysqa_over_betekenis_titel (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over betekenis titel correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_BETEKENIS_TITEL))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_BETEKENIS_TITEL))
        if element == True:
            print("CORRECT: Sysqa over betekenis titel is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverBetekenisTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over betekenis titel is niet aanwezig op pagina")

    def check_sysqa_over_betekenis_text_1 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over betekenis text 1 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_BETEKENIS_TEXT_1))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_BETEKENIS_TEXT_1))
        if element == True:
            print("CORRECT: Sysqa over betekenis text 1 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverBetekenisText1:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over betekenis text 1 is niet aanwezig op pagina")

    def check_sysqa_over_betekenis_text_2 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over betekenis text 2 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_BETEKENIS_TEXT_2))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_BETEKENIS_TEXT_2))
        if element == True:
            print("CORRECT: Sysqa over betekenis text 2 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverBetekenisText2:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over betekenis text 2 is niet aanwezig op pagina")

    def check_sysqa_over_verbinding_titel (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over verbinding titel correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VERBINDING_TITEL))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_VERBINDING_TITEL))
        if element == True:
            print("CORRECT: Sysqa over verbinding titel is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverVerbindingTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over verbinding titel is niet aanwezig op pagina")

    def check_sysqa_over_verbinding_text_1 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over verbinding text 1 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VERBINDING_TEXT_1))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_VERBINDING_TEXT_1))
        if element == True:
            print("CORRECT: Sysqa over verbinding text 1 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverVerbindingText1:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over verbinding text 1 is niet aanwezig op pagina")

    def check_sysqa_over_verbinding_text_2 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over verbinding text 2 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_VERBINDING_TEXT_2))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_VERBINDING_TEXT_2))
        if element == True:
            print("CORRECT: Sysqa over verbinding text 2 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverVerbindingText2:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over verbinding text 2 is niet aanwezig op pagina")

    def check_sysqa_over_ontwikkeling_titel (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over ontwikkeling titel correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_ONTWIKKELING_TITEL))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_ONTWIKKELING_TITEL))
        if element == True:
            print("CORRECT: Sysqa over ontwikkeling titel is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverOntwikkelingTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over ontwikkeling titel is niet aanwezig op pagina")

    def check_sysqa_over_ontwikkeling_text_1 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over ontwikkeling text 1 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_ONTWIKKELING_TEXT_1))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_ONTWIKKELING_TEXT_1))
        if element == True:
            print("CORRECT: Sysqa over ontwikkeling text 1 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverOntwikkelingText1:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over ontwikkeling text 1 is niet aanwezig op pagina")

    def check_sysqa_over_ontwikkeling_text_2 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over ontwikkeling text 2 correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_ONTWIKKELING_TEXT_2))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_ONTWIKKELING_TEXT_2))
        if element == True:
            print("CORRECT: Sysqa over ontwikkeling text 2 is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverOntwikkelingText2:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over ontwikkeling text 2 is niet aanwezig op pagina")

    def check_sysqa_over_contact_onder (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over contact onder correct werkt")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_CONTACT_ONDER))
        element2 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_CONTACT_ONDER))
        if element == True:
            print("CORRECT: Sysqa over contact onder is aanwezig op pagina")
            if self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_CONTACT_ONDER) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_CONTACT_ONDER) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa over contact onder is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaSecurityPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaContactPagina:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_over_blog_titel (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over blog titel correct is")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_BLOG_TITEL))
        element3 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_BLOG_TITEL))
        if element == True:
            print("CORRECT: Sysqa over blog titel is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaOverBlogTitel:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa over blog titel is niet aanwezig op pagina")

    def check_sysqa_over_blog_artikelen (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over blog artikelen correct werkt")
        element = (self.find_element_boolean(loc.SysqaOverGUI.SYSQA_OVER_BLOG_ALLE_ARTIKELEN))
        element2 = (self.find(loc.SysqaOverGUI.SYSQA_OVER_BLOG_ALLE_ARTIKELEN))
        if element == True:
            print("CORRECT: Sysqa over blog artikelen is aanwezig op pagina")
            if self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_BLOG_ALLE_ARTIKELEN) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaOverGUI.SYSQA_OVER_BLOG_ALLE_ARTIKELEN) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa over blog artikelen is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaOverBlogArtikelen:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")
    


    
    
























