from .BasePage import BasePage
from .locator import locator as loc
import subprocess, sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import logging, time
import driver
import data


class Sysqa (BasePage):

    def open_sysqa_pagina (self):
        link = data.sysqaHomePagina
        logging.info(f"Startpagina Sysqa wordt geopend:{link}")
        self.driver.get(link) 

    def accept_sysqa_cookies (self):
        logging.info("Er wordt gecontroleerd of Cookies geaccepteerd worden")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_COOKIES))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_COOKIES))
        if element == True:
            print("CORRECT: Cookies is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_COOKIES) == True:
                print ("CORRECT: Cookies is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_COOKIES) == False:
                print ("ERROR: Cookies is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Cookies is niet aanwezig op pagina")
        time.sleep(1)
        element2.click()

    def check_navigatie_sysqa_logo (self):
        logging.info("Er wordt gecontroleerd of het Sysqa logo correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NAV_LOGO))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NAV_LOGO))
        if element == True:
            print("CORRECT: Sysqa Logo is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_LOGO) == True:
                print ("CORRECT: Sysqa Logo is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_LOGO) == False:
                print ("ERROR: Sysqa Logo is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa Logo is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaHomePagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")

    def check_navigatie_sysqa_home (self):
        logging.info("Er wordt gecontroleerd of de Sysqa home button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NAV_HOME))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NAV_HOME))
        if element == True:
            print("CORRECT: Sysqa home button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_HOME) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_HOME) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa home button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaHomePagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNavHome:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_navigatie_sysqa_over (self):
        logging.info("Er wordt gecontroleerd of de Sysqa over button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NAV_OVER))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NAV_OVER))
        if element == True:
            print("CORRECT: Sysqa over button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_OVER) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_OVER) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa over button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaOverOnsPaginaZonder:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNavOver:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")
            
    def check_navigatie_sysqa_dienst (self):
        logging.info("Er wordt gecontroleerd of de Sysqa dienst button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NAV_DIENSTEN))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NAV_DIENSTEN))
        if element == True:
            print("CORRECT: Sysqa dienst button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_DIENSTEN) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_DIENSTEN) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa dienst button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaDienstenPaginaZonder:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNavDiensten:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_navigatie_sysqa_blog (self):
        logging.info("Er wordt gecontroleerd of de Sysqa blog button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NAV_BLOG))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NAV_BLOG))
        if element == True:
            print("CORRECT: Sysqa blog button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_BLOG) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_BLOG) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa blog button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogPaginaZonder:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNavBlog:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_navigatie_sysqa_contact (self):
        logging.info("Er wordt gecontroleerd of de Sysqa contact button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NAV_CONTACT))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NAV_CONTACT))
        if element == True:
            print("CORRECT: Sysqa contact button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_CONTACT) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NAV_CONTACT) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa contact button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaContactPaginaZonder:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNavContact:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_slogan (self):
        logging.info("Er wordt gecontroleerd of de Sysqa slogan correct is")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_TITEL))
        element3 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_TITEL))
        if element == True:
            print("CORRECT: Sysqa slogan is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaHomeSlogan:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa slogan is niet aanwezig op pagina")

    def check_sysqa_home_slogan_text (self):
        logging.info("Er wordt gecontroleerd of de Sysqa slogan text correct is")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_TEXT))
        element3 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_TEXT))
        if element == True:
            print("CORRECT: Sysqa slogan text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaHomeSloganText:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa slogan text is niet aanwezig op pagina")

    def check_sysqa_home_contact_button_boven (self):
        logging.info("Er wordt gecontroleerd of de Sysqa contact boven button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_CONTACT_BUTTON_BOVEN))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_CONTACT_BUTTON_BOVEN))
        if element == True:
            print("CORRECT: Sysqa contact boven button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_CONTACT_BUTTON_BOVEN) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_CONTACT_BUTTON_BOVEN) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa contact boven button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaContactPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeContactButtonBoven:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_improving_slogan (self):
        logging.info("Er wordt gecontroleerd of de Sysqa improving slogan correct is")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_IMPROVING_SLOGAN))
        element3 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_IMPROVING_SLOGAN))
        if element == True:
            print("CORRECT: Sysqa improving slogan is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaHomeImprovingSlogan:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa improving slogan is niet aanwezig op pagina")

    def check_sysqa_home_improving_slogan_text (self):
        logging.info("Er wordt gecontroleerd of de Sysqa improving slogan text correct is")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_IMPROVING_TEXT))
        element3 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_IMPROVING_TEXT))
        if element == True:
            print("CORRECT: Sysqa improving slogan text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaHomeImprovingText:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa improving slogan text is niet aanwezig op pagina")

    def check_sysqa_home_improving_slogan_help (self):
        logging.info("Er wordt gecontroleerd of de Sysqa improving slogan help correct is")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_IMPROVING_HELP))
        element3 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_IMPROVING_HELP))
        if element == True:
            print("CORRECT: Sysqa improving slogan help is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaHomeImprovingHelp:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa improving slogan help is niet aanwezig op pagina")

    def check_sysqa_home_specialisatie_1 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa specialisatie 1 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_1))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_1))
        if element == True:
            print("CORRECT: Sysqa specialisatie 1 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_1) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_1) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa specialisatie 1 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaRequirementsPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeSpecialisatie1:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_specialisatie_2 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa specialisatie 2 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_2))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_2))
        if element == True:
            print("CORRECT: Sysqa specialisatie 2 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_2) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_2) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa specialisatie 2 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaTestenPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeSpecialisatie2:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_specialisatie_3 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa specialisatie 3 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_3))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_3))
        if element == True:
            print("CORRECT: Sysqa specialisatie 3 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_3) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_3) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa specialisatie 3 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaTestautomatiseringPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeSpecialisatie3:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_specialisatie_4 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa specialisatie 4 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_4))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_4))
        if element == True:
            print("CORRECT: Sysqa specialisatie 4 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_4) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_4) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa specialisatie 4 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaAgilePagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeSpecialisatie4:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_specialisatie_5 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa specialisatie 5 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_5))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_5))
        if element == True:
            print("CORRECT: Sysqa specialisatie 5 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_5) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_SPECIALISATIE_5) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa specialisatie 5 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaSecurityPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeSpecialisatie5:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_meer_over_button (self):
        logging.info("Er wordt gecontroleerd of de Sysqa meer over button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_MEER_OVER_BUTTON))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_MEER_OVER_BUTTON))
        if element == True:
            print("CORRECT: Sysqa meer over button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_MEER_OVER_BUTTON) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_MEER_OVER_BUTTON) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa meer over button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaOverOnsPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeMeerOverButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_alle_artikelen_button (self):
        logging.info("Er wordt gecontroleerd of de Sysqa alle artikelen button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_ALLE_ARTIKELEN_BUTTON))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_ALLE_ARTIKELEN_BUTTON))
        if element == True:
            print("CORRECT: Sysqa alle artikelen button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_ALLE_ARTIKELEN_BUTTON) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_ALLE_ARTIKELEN_BUTTON) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa alle artikelen button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogPaginaZonder:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeAlleArtikelenButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_sysqa (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer sysqa correct is")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_SYSQA))
        element3 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_SYSQA))
        if element == True:
            print("CORRECT: Sysqa footer sysqa is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaHomeFooterSysqa:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa footer sysqa is niet aanwezig op pagina")

    def check_sysqa_home_footer_home (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer home button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_HOME))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_HOME))
        if element == True:
            print("CORRECT: Sysqa footer home button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_HOME) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_HOME) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer home button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaHomePagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNavHome:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_over (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer over button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_OVER))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_OVER))
        if element == True:
            print("CORRECT: Sysqa footer over button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_OVER) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_OVER) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer over button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaOverOnsPaginaZonder:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNavOver:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_diensten (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer diensten button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_DIENSTEN))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_DIENSTEN))
        if element == True:
            print("CORRECT: Sysqa footer diensten button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_DIENSTEN) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_DIENSTEN) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer diensten button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaDienstenPaginaZonder:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNavDiensten:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_blog (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer blog button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG))
        if element == True:
            print("CORRECT: Sysqa footer blog button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer blog button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogPaginaZonder:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNavBlog:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_contact (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer contact button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT))
        if element == True:
            print("CORRECT: Sysqa footer contact button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer contact button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaContactPaginaZonder:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNavContact:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_werken (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer werken button correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_WERKEN_BUTTON))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_WERKEN_BUTTON))
        if element == True:
            print("CORRECT: Sysqa footer werken button is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_WERKEN_BUTTON) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_WERKEN_BUTTON) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer werken button is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaWerkenBijPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterWerkenButton:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_blog_thema (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer blog thema correct is")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_THEMA))
        element3 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_THEMA))
        if element == True:
            print("CORRECT: Sysqa footer blog thema is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaHomeFooterBlogThema:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa footer blog thema is niet aanwezig op pagina")

    def check_sysqa_home_footer_onderwerp_1 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer onderwerp 1 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_1))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_1))
        if element == True:
            print("CORRECT: Sysqa footer onderwerp 1 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_1) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_1) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer onderwerp 1 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogOnderwerpPagina1:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterBlogOnderwerp1:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_onderwerp_2 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer onderwerp 2 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_2))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_2))
        if element == True:
            print("CORRECT: Sysqa footer onderwerp 2 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_2) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_2) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer onderwerp 2 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogOnderwerpPagina2:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterBlogOnderwerp2:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_onderwerp_3 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer onderwerp 3 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_3))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_3))
        if element == True:
            print("CORRECT: Sysqa footer onderwerp 3 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_3) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_3) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer onderwerp 3 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogOnderwerpPagina3:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterBlogOnderwerp3:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_onderwerp_4 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer onderwerp 4 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_4))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_4))
        if element == True:
            print("CORRECT: Sysqa footer onderwerp 4 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_4) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_4) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer onderwerp 4 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogOnderwerpPagina4:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterBlogOnderwerp4:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_onderwerp_5 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer onderwerp 5 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_5))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_5))
        if element == True:
            print("CORRECT: Sysqa footer onderwerp 5 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_5) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_5) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer onderwerp 5 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogOnderwerpPagina5:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterBlogOnderwerp5:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_onderwerp_6 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer onderwerp 6 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_6))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_6))
        if element == True:
            print("CORRECT: Sysqa footer onderwerp 6 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_6) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_6) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer onderwerp 6 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogOnderwerpPagina6:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterBlogOnderwerp6:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_onderwerp_7 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer onderwerp 7 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_7))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_7))
        if element == True:
            print("CORRECT: Sysqa footer onderwerp 7 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_7) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_7) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer onderwerp 7 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogOnderwerpPagina7:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterBlogOnderwerp7:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_onderwerp_8 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer onderwerp 8 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_8))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_8))
        if element == True:
            print("CORRECT: Sysqa footer onderwerp 8 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_8) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_8) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer onderwerp 8 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogOnderwerpPagina8:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterBlogOnderwerp8:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_onderwerp_9 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer onderwerp 9 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_9))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_9))
        if element == True:
            print("CORRECT: Sysqa footer onderwerp 9 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_9) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_9) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer onderwerp 9 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogOnderwerpPagina9:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterBlogOnderwerp9:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_onderwerp_10 (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer onderwerp 10 correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_10))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_10))
        if element == True:
            print("CORRECT: Sysqa footer onderwerp 10 is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_10) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_BLOG_ONDERWERP_10) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer onderwerp 10 is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaBlogOnderwerpPagina10:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterBlogOnderwerp10:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_contact_text (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer contact text correct is")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT))
        element3 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT))
        if element == True:
            print("CORRECT: Sysqa footer contact text is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaHomeFooterContact:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa footer contact text is niet aanwezig op pagina")

    def check_sysqa_home_footer_contact_adres (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer adres correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_ADRES))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_ADRES))
        if element == True:
            print("CORRECT: Sysqa footer adres is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_ADRES) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_ADRES) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer adres is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaAdresLink:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterContactAdres:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_contact_maps (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer maps correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_MAPS))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_MAPS))
        if element == True:
            print("CORRECT: Sysqa footer maps is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_MAPS) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_MAPS) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer maps is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaGoogleMapsLink:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterContactMaps:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_contact_telefoon (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer telefoon correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_TELEFOON))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_TELEFOON))
        if element == True:
            print("CORRECT: Sysqa footer telefoon is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_TELEFOON) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_TELEFOON) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer telefoon is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaTelefoonLink:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterContactTel:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_contact_email (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer email correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_EMAIL))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_EMAIL))
        if element == True:
            print("CORRECT: Sysqa footer email is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_EMAIL) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_EMAIL) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer email is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaEmailLink:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaHomeFooterContactEmail:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_footer_contact_nieuwsbrief (self):
        logging.info("Er wordt gecontroleerd of de Sysqa footer nieuwsbrief correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_NIEUWSBRIEF))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_NIEUWSBRIEF))
        if element == True:
            print("CORRECT: Sysqa footer nieuwsbrief is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_NIEUWSBRIEF) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_NIEUWSBRIEF) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa footer nieuwsbrief is niet aanwezig op pagina")
        text = element2.text
        if text == data.sysqaHomeFooterContactNieuwsbrief:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_nieuwsbrief_popup_text (self):
        logging.info("Er wordt gecontroleerd of de Sysqa nieuwsbrief popup correct werkt")
        klik = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_FOOTER_CONTACT_NIEUWSBRIEF))
        klik.click()
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_TEXT))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_TEXT))
        if element == True:
            print("CORRECT: Sysqa nieuwsbrief popup is aanwezig op pagina")
        elif element == False:
            print ("ERROR: Sysqa nieuwsbrief popup is niet aanwezig op pagina")
        text = element2.text
        if text == data.sysqaNieuwsbriefPopupText:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_nieuwsbrief_popup_naam (self):
        logging.info("Er wordt gecontroleerd of de Sysqa nieuwsbrief popup naam correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_NAAM))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_NAAM))
        if element == True:
            print("CORRECT: Sysqa nieuwsbrief popup naam  is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_NAAM) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_NAAM) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa nieuwsbrief popup naam is niet aanwezig op pagina")
        text = element2.get_attribute("placeholder")
        print (text)
        if text == data.sysqaNieuwsbriefPopupNaam:
            print ("CORRECT: Text is correct")
        else:
            print ("ERROR: Text is niet correct")
        self.schrijf(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_NAAM, "Thijs van Opstal")
        value = element2.get_attribute("value")
        print(value)
        if value == "Thijs van Opstal":
            print("CORRECT: Value is correct")
        else:
            print("ERROR: Value is niet correct")

    def check_sysqa_home_nieuwsbrief_popup_email (self):
        logging.info("Er wordt gecontroleerd of de Sysqa nieuwsbrief popup email correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_EMAIL))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_EMAIL))
        if element == True:
            print("CORRECT: Sysqa nieuwsbrief popup email  is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_EMAIL) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_EMAIL) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa nieuwsbrief popup email is niet aanwezig op pagina")
        text = element2.get_attribute("placeholder")
        print (text)
        if text == data.sysqaNieuwsbriefPopupEmail:
            print ("CORRECT: Text is correct")
        else:
            print ("ERROR: Text is niet correct")
        self.schrijf(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_EMAIL, "tvanopstal@sysqa.nl")
        value = element2.get_attribute("value")
        print(value)
        if value == "tvanopstal@sysqa.nl":
            print("CORRECT: Value is correct")
        else:
            print("ERROR: Value is niet correct")

    def check_sysqa_home_nieuwsbrief_popup_voorwaarden (self):
        logging.info("Er wordt gecontroleerd of de Sysqa nieuwsbrief popup voorwaarden correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_VOORWAARDEN))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_VOORWAARDEN))
        if element == True:
            print("CORRECT: Sysqa nieuwsbrief popup voorwaarden is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_VOORWAARDEN) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_VOORWAARDEN) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa nieuwsbrief popup voorwaarden is niet aanwezig op pagina")
        link = element2.get_attribute("href")
        print (link)
        if link == data.sysqaPrivacyPagina:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        text = element2.text
        if text == data.sysqaNieuwsbriefPopupVoorwaarden:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")
        checkbox = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_CHECKBOX))
        checkbox.click()

    def check_sysqa_home_nieuwsbrief_popup_versturen (self):
        logging.info("Er wordt gecontroleerd of de Sysqa nieuwsbrief popup versturen correct werkt")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_VERSTUREN))
        element2 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_VERSTUREN))
        if element == True:
            print("CORRECT: Sysqa nieuwsbrief popup versturen is aanwezig op pagina")
            if self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_VERSTUREN) == True:
                print ("CORRECT: Element is aanklikbaar")
            elif self.return_clickable(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_VERSTUREN) == False:
                print ("ERROR: Element is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa nieuwsbrief popup versturen is niet aanwezig op pagina")
        text = element2.text
        if text == data.sysqaNieuwsbriefPopupVersturen:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")
        versturen = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_VERSTUREN))
        versturen.click()

    def check_sysqa_home_nieuwsbrief_popup_error (self):
        logging.info("Er wordt gecontroleerd of de Sysqa nieuwsbrief popup error correct is")
        element = (self.find_element_boolean(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_ERROR))
        element3 = (self.find(loc.SysqaHomeGUI.SYSQA_HOME_NIEUWSBRIEF_POPUP_ERROR))
        if element == True:
            print("CORRECT: Sysqa nieuwsbrief popup error is aanwezig op pagina")
            print(element3.text)
            if element3.text == data.sysqaNieuwsbriefPopupError:
                print("CORRECT: Text is correct")
            else:
                print("ERROR: Text is niet correct")
        else:
            print("ERROR: Sysqa nieuwsbrief popup error is niet aanwezig op pagina")

































