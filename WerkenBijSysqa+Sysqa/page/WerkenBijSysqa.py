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
        link = data.werkenBijSysqaPaginaHome
        logging.info(f"Startpagina WerkenbijSysqa wordt geopend:{link}")
        self.driver.get(link) 

    def accept_cookies (self):
        logging.info("Cookies worden geaccepteerd")
        element = self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_COOKIES_ACCEPT)
        if element == True:
            print("CORRECT: Cookie banner is aanwezig, cookies worden geaccepteerd")
            element2 = self.find(loc.WerkenBijSysqaGUI.SYSQA_COOKIES_ACCEPT)
            element2.click()
        else:
            print("Cookies niet aanwezig, test gaat door")
            pass

    def check_navigatie_sysqa_logo (self, link_URL):
        logging.info("Er wordt gecontroleerd of het Sysqa logo correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NAV_LOGO))
        if element == True:
            print("CORRECT: Sysqa Logo is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_LOGO) == True:
                print ("CORRECT: Sysqa Logo is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_LOGO) == False:
                print ("ERROR: Sysqa Logo is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Sysqa Logo is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NAV_LOGO))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")

    def check_navigatie_home_button (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Home button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NAV_HOME_BUTTON))
        if element == True:
            print("CORRECT: Home button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_HOME_BUTTON) == True:
                print ("CORRECT: Home button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_HOME_BUTTON) == False:
                print ("ERROR: Home button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Home button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NAV_HOME_BUTTON))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")

    def check_navigatie_vacatures_button (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Vacatures button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NAV_VACATURES_BUTTON))
        if element == True:
            print("CORRECT: Vacatures button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_VACATURES_BUTTON) == True:
                print ("CORRECT: Vacatures button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_VACATURES_BUTTON) == False:
                print ("ERROR: Vacatures button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Vacatures button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NAV_VACATURES_BUTTON))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")

    def check_navigatie_verhalen_button (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Verhalen button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NAV_VERHALEN_BUTTON))
        if element == True:
            print("CORRECT: Verhalen button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_VERHALEN_BUTTON) == True:
                print ("CORRECT: Verhalen button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_VERHALEN_BUTTON) == False:
                print ("ERROR: Verhalen button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Verhalen button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NAV_VERHALEN_BUTTON))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        
    def check_navigatie_kennismaken_button (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Kennismaken button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NAV_KENNISMAKEN_BUTTON))
        if element == True:
            print("CORRECT: Kennismaken button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_KENNISMAKEN_BUTTON) == True:
                print ("CORRECT: Kennismaken button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_KENNISMAKEN_BUTTON) == False:
                print ("ERROR: Kennismaken button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Kennismaken button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NAV_KENNISMAKEN_BUTTON))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")

    def check_navigatie_telefoon_button (self, tel_nummer):
        logging.info("Er wordt gecontroleerd of de Telefoon button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NAV_TELEFOON_BUTTON))
        if element == True:
            print("CORRECT: Telefoon button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_TELEFOON_BUTTON) == True:
                print ("CORRECT: Telefoon button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NAV_TELEFOON_BUTTON) == False:
                print ("ERROR: Telefoon button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Telefoon button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NAV_TELEFOON_BUTTON))
        telnummer = element2.get_attribute("href")
        print (telnummer)
        if telnummer == tel_nummer:
            print ("CORRECT: Telefoon nummer is correct")
        else:
            print ("ERROR: Telefoon nummer is niet correct")

    def check_kennismaken_zijkant_button (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Kennismaken zijkant button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_ZIJKANT_KENNISMAKEN_BUTTON))
        if element == True:
            print("CORRECT: Kennismaken zijkant button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_ZIJKANT_KENNISMAKEN_BUTTON) == True:
                print ("CORRECT: Kennismaken zijkant button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_ZIJKANT_KENNISMAKEN_BUTTON) == False:
                print ("ERROR: Kennismaken zijkant button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Kennismaken zijkant button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_ZIJKANT_KENNISMAKEN_BUTTON))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_ZIJKANT_KENNISMAKEN_BUTTON))
        print(element3.text)
        if element3.text == data.kennismakenButtonZijkant:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")


    def check_sysqa_slogan_1 (self):
        logging.info("Er wordt gecontroleerd of de Slogan 1 correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_SLOGAN_1))
        if element == True:
            print("CORRECT: Slogan 1 is aanwezig op pagina")
            element = (self.find(loc.WerkenBijSysqaGUI.SYSQA_SLOGAN_1))
            print(element.text)
            if element.text == data.sysqaSlogan1:
                print("CORRECT: Slogan 1 is correct")
            else:
                print("ERROR: Slogan 1 is niet correct")
        elif element == False:
            print("ERROR: Slogan 1 is niet aanwezig")

    def check_sysqa_slogan_2 (self):
        logging.info("Er wordt gecontroleerd of de Slogan 2 correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_SLOGAN_2))
        if element == True:
            print("CORRECT: Slogan 2 is aanwezig op pagina")
            element = (self.find(loc.WerkenBijSysqaGUI.SYSQA_SLOGAN_2))
            print(element.text)
            if element.text == data.sysqaSlogan2:
                print("CORRECT: Slogan 2 is correct")
            else:
                print("ERROR: Slogan 2 is niet correct")
        elif element == False:
            print("ERROR: Slogan 2 is niet aanwezig")

    def check_sysqa_slogan_3 (self):
        logging.info("Er wordt gecontroleerd of de Slogan 3 correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_SLOGAN_3))
        if element == True:
            print("CORRECT: Slogan 3 is aanwezig op pagina")
            element = (self.find(loc.WerkenBijSysqaGUI.SYSQA_SLOGAN_3))
            print(element.text)
            if element.text == data.sysqaSlogan3:
                print("CORRECT: Slogan 3 is correct")
            else:
                print("ERROR: Slogan 3 is niet correct")
        elif element == False:
            print("ERROR: Slogan 3 is niet aanwezig")

    def check_sysqa_kennismaken_button_boven (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Kennismaken button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON))
        if element == True:
            print("CORRECT: Kennismaken button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON) == True:
                print ("CORRECT: Kennismaken button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON) == False:
                print ("ERROR: Kennismaken button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Kennismaken button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON))
        text = element3.text
        if text == data.kennismakenButtonBoven:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_titel (self):
        logging.info("Er wordt gecontroleerd of de titel correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_TITEL))
        if element == True:
            print("CORRECT: Titel is aanwezig op pagina")
            element = (self.find(loc.WerkenBijSysqaGUI.SYSQA_TITEL))
            print(element.text)
            if element.text == data.sysqaTitel:
                print("CORRECT: Titel is correct")
            else:
                print("ERROR: Titel is niet correct")
        elif element == False:
            print("ERROR: Titel is niet aanwezig")

    def check_sysqa_text_1 (self):
        logging.info("Er wordt gecontroleerd of de text 1 correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_TEXT_1))
        if element == True:
            print("CORRECT: Text 1 is aanwezig op pagina")
            element = (self.find(loc.WerkenBijSysqaGUI.SYSQA_TEXT_1))
            print(element.text)
            if element.text == data.sysqaText1:
                print("CORRECT: Text 1 is correct")
            else:
                print("ERROR: Text 1 is niet correct")
        elif element == False:
            print("ERROR: Text 1 is niet aanwezig")

    def check_sysqa_kop_titel (self):
        logging.info("Er wordt gecontroleerd of de koptitel correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_KOP_TITEL))
        if element == True:
            print("CORRECT: Koptitel is aanwezig op pagina")
            element = (self.find(loc.WerkenBijSysqaGUI.SYSQA_KOP_TITEL))
            print(element.text)
            if element.text == data.sysqaKopTitel:
                print("CORRECT: Koptitel is correct")
            else:
                print("ERROR: Koptitel is niet correct")
        elif element == False:
            print("ERROR: Koptitel is niet aanwezig")

    def check_sysqa_text_2 (self):
        logging.info("Er wordt gecontroleerd of de text 2 correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_TEXT_2))
        if element == True:
            print("CORRECT: Text 2 is aanwezig op pagina")
            element = (self.find(loc.WerkenBijSysqaGUI.SYSQA_TEXT_2))
            print(element.text)
            if element.text == data.sysqaText2:
                print("CORRECT: Text 2 is correct")
            else:
                print("ERROR: Text 2 is niet correct")
        elif element == False:
            print("ERROR: Text 2 is niet aanwezig")

    def check_sysqa_vacatures_titel (self):
        logging.info("Er wordt gecontroleerd of de Vacatures titel correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_VACATURES_TITEL))
        if element == True:
            print("CORRECT: Vacatures titel is aanwezig op pagina")
            element = (self.find(loc.WerkenBijSysqaGUI.SYSQA_VACATURES_TITEL))
            print(element.text)
            if element.text == data.sysqaVacaturesTitel:
                print("CORRECT: Vacatures titel is correct")
            else:
                print("ERROR: Vacatures titel is niet correct")
        elif element == False:
            print("ERROR: Vacatures titel is niet aanwezig")

    def check_sysqa_uitgelichte_vacatures (self):
        logging.info("Er wordt gecontroleerd of de uitgelichte vacatures correct zijn")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURES))
        if element == True:
            print("CORRECT: Uitgelichte vacatures is aanwezig op pagina")
        elif element == False:
            print("ERROR: Uitgelichte vacatures is niet aanwezig")

    def check_sysqa_uitgelichte_vacatures_bekijken_1 (self):
        logging.info("Er wordt gecontroleerd of de button Bekijk deze vacature 1 correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_1))
        if element == True:
            print("CORRECT: Bekijk deze vacature button 1 is aanwezig")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_1) == True:
                print("CORRECT: Bekijk deze vacature button 1 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_1) == False:
                print("ERROR: Bekijk deze vacature button 1 is niet aanklikbaar")
        else:
            print("ERROR: Bekijk deze vacature button 1 is niet aanwezig")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_1))
        print(element2.text)
        if element2.text == data.bekijkDezeVactureButton:
            print("CORRECT: Bekijk deze vacature button 1 text is correct")
        else:
            print("ERROR: Bekijk deze vacature button 1 text is niet correct")

    def check_sysqa_uitgelichte_vacatures_bekijken_2 (self):
        logging.info("Er wordt gecontroleerd of de button Bekijk deze vacature 2 correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_2))
        if element == True:
            print("CORRECT: Bekijk deze vacature button 2 is aanwezig")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_2) == True:
                print("CORRECT: Bekijk deze vacature button 2 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_2) == False:
                print("ERROR: Bekijk deze vacature button 2 is niet aanklikbaar")
        else:
            print("ERROR: Bekijk deze vacature button 2 is niet aanwezig")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_2))
        print(element2.text)
        if element2.text == data.bekijkDezeVactureButton:
            print("CORRECT: Bekijk deze vacature button 2 text is correct")
        else:
            print("ERROR: Bekijk deze vacature button 2 text is niet correct")

    def check_sysqa_uitgelichte_vacatures_bekijken_3 (self):
        logging.info("Er wordt gecontroleerd of de button Bekijk deze vacature 3 correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_3))
        if element == True:
            print("CORRECT: Bekijk deze vacature button 3 is aanwezig")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_3) == True:
                print("CORRECT: Bekijk deze vacature button 3 is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_3) == False:
                print("ERROR: Bekijk deze vacature button 3 is niet aanklikbaar")
        else:
            print("ERROR: Bekijk deze vacature button 3 is niet aanwezig")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_3))
        print(element2.text)
        if element2.text == data.bekijkDezeVactureButton:
            print("CORRECT: Bekijk deze vacature button 3 text is correct")
        else:
            print("ERROR: Bekijk deze vacature button 3 text is niet correct")

    def check_sysqa_bekijk_al_onze_vacatures_button (self):
        logging.info("Er wordt gecontroleerd of de button Bekijk al onze vacatures correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_BEKIJK_AL_ONZE_VACATURES_BUTTON))
        if element == True:
            print("CORRECT: Bekijk al onze vacatures button is aanwezig")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_BEKIJK_AL_ONZE_VACATURES_BUTTON) == True:
                print("CORRECT: Bekijk al onze vacatures is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_BEKIJK_AL_ONZE_VACATURES_BUTTON) == False:
                print("ERROR: Bekijk al onze vacatures is niet aanklikbaar")
        else:
            print("ERROR: Bekijk al onze vacatures is niet aanwezig")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_BEKIJK_AL_ONZE_VACATURES_BUTTON))
        print(element2.text)
        if element2.text == data.bekijkAlOnzeVacaturesButton:
            print("CORRECT: Bekijk al onze vacatures text is correct")
        else:
            print("ERROR: Bekijk al onze vacatures text is niet correct")

    def check_sysqa_bekijk_alle_verhalen_button (self, link_URL):
        logging.info("Er wordt gecontroleerd of de bekijken alle verhalen button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_BEKIJK_ALLE_VERHALEN_EN_VIDEOS))
        if element == True:
            print("CORRECT: bekijken alle verhalen button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_BEKIJK_ALLE_VERHALEN_EN_VIDEOS) == True:
                print ("CORRECT: bekijken alle verhalen button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_BEKIJK_ALLE_VERHALEN_EN_VIDEOS) == False:
                print ("ERROR: bekijken alle verhalen button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: bekijken alle verhalen button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_BEKIJK_ALLE_VERHALEN_EN_VIDEOS))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_BEKIJK_ALLE_VERHALEN_EN_VIDEOS))
        text = element3.text
        print(text)
        if text == data.bekijkAlleVerhalenEnVideos:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_kennismaken_titel (self):
        logging.info("Er wordt gecontroleerd of de kennismaken titel correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_TITEL))
        if element == True:
            print("CORRECT: kennismaken titel is aanwezig op pagina")
            element = (self.find(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_TITEL))
            print(element.text)
            if element.text == data.kennisMakenTitel:
                print("CORRECT: kennismaken titel is correct")
            else:
                print("ERROR: kennismaken titel niet correct")
        elif element == False:
            print("ERROR: kennismaken titel is niet aanwezig")

    def check_sysqa_kennismaken_button_onder (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Kennismaken button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON_ONDER))
        if element == True:
            print("CORRECT: Kennismaken button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON_ONDER) == True:
                print ("CORRECT: Kennismaken button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON_ONDER) == False:
                print ("ERROR: Kennismaken button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Kennismaken button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON_ONDER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON_ONDER))
        text = element3.text
        if text == data.kennismakenButtonOnder:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_quiz_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Doe de Test button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_DOE_DE_TEST_BUTTON_FOOTER))
        if element == True:
            print("CORRECT: Doe de Test button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_DOE_DE_TEST_BUTTON_FOOTER) == True:
                print ("CORRECT: Doe de Test button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_DOE_DE_TEST_BUTTON_FOOTER) == False:
                print ("ERROR: Doe de Test button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Doe de Test button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_DOE_DE_TEST_BUTTON_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_DOE_DE_TEST_BUTTON_FOOTER))
        text = element3.text
        if text == data.doeDeTestButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_home_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Home button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_HOME_BUTTON_FOOTER))
        if element == True:
            print("CORRECT: Home button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_HOME_BUTTON_FOOTER) == True:
                print ("CORRECT: Home button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_HOME_BUTTON_FOOTER) == False:
                print ("ERROR: Home button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Home button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_HOME_BUTTON_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_HOME_BUTTON_FOOTER))
        text = element3.text
        if text == data.homeButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_vacatures_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Vacatures button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_VACATURES_BUTTON_FOOTER))
        if element == True:
            print("CORRECT: Vacatures button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_VACATURES_BUTTON_FOOTER) == True:
                print ("CORRECT: Vacatures button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_VACATURES_BUTTON_FOOTER) == False:
                print ("ERROR: Vacatures button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Vacatures button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_VACATURES_BUTTON_FOOTER_TEKST))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_VACATURES_BUTTON_FOOTER_TEKST))
        text = element3.text
        if text == data.vacaturesButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_verhalen_en_videos_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Verhalen en Video's button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_VERHALEN_EN_VIDEOS_BUTTON_FOOTER))
        if element == True:
            print("CORRECT: Verhalen en Video's button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_VERHALEN_EN_VIDEOS_BUTTON_FOOTER) == True:
                print ("CORRECT: Verhalen en Video's button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_VERHALEN_EN_VIDEOS_BUTTON_FOOTER) == False:
                print ("ERROR: Verhalen en Video's is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Verhalen en Video's is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_VERHALEN_EN_VIDEOS_BUTTON_FOOTER_TEKST))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_VERHALEN_EN_VIDEOS_BUTTON_FOOTER_TEKST))
        text = element3.text
        if text == data.verhalenEnVideosButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_kennismaken_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Kennismaken button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON_FOOTER))
        if element == True:
            print("CORRECT: Kennismaken button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON_FOOTER) == True:
                print ("CORRECT: Kennismaken button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON_FOOTER) == False:
                print ("ERROR: Kennismaken is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Kennismaken is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON_FOOTER_TEKST))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_KENNISMAKEN_BUTTON_FOOTER_TEKST))
        text = element3.text
        if text == data.kennismakenButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_adres_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de adres button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_CONTACT_ADRES_FOOTER))
        if element == True:
            print("CORRECT: Adres button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_CONTACT_ADRES_FOOTER) == True:
                print ("CORRECT: Adres button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_CONTACT_ADRES_FOOTER) == False:
                print ("ERROR: Adres is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Adres is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_CONTACT_ADRES_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_CONTACT_ADRES_FOOTER))
        text = element3.text
        print(text)
        if text == data.adresButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_corporate_website_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Corporate website button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_CORPORATE_WEBSITE_BUTTON_FOOTER))
        if element == True:
            print("CORRECT: Corporate website button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_CORPORATE_WEBSITE_BUTTON_FOOTER) == True:
                print ("CORRECT: Corporate website button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_CORPORATE_WEBSITE_BUTTON_FOOTER) == False:
                print ("ERROR: Corporate website is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Corporate website is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_CORPORATE_WEBSITE_BUTTON_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_CORPORATE_WEBSITE_BUTTON_FOOTER))
        text = element3.text
        if text == data.corporateWebsiteButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_google_maps_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Google Maps button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_GOOGLE_MAPS_BUTTON_FOOTER))
        if element == True:
            print("CORRECT: Google Maps button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_GOOGLE_MAPS_BUTTON_FOOTER) == True:
                print ("CORRECT: Google Maps button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_GOOGLE_MAPS_BUTTON_FOOTER) == False:
                print ("ERROR: Google Maps button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Google Maps button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_GOOGLE_MAPS_BUTTON_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_GOOGLE_MAPS_BUTTON_FOOTER))
        text = element3.text
        if text == data.googleMapsButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_telefoon_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Telefoon button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_TELEFOON_NUMMER_BUTTON_FOOTER))
        if element == True:
            print("CORRECT: Telefoon button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_TELEFOON_NUMMER_BUTTON_FOOTER) == True:
                print ("CORRECT: Telefoon button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_TELEFOON_NUMMER_BUTTON_FOOTER) == False:
                print ("ERROR: Telefoon button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Telefoon button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_TELEFOON_NUMMER_BUTTON_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_TELEFOON_NUMMER_BUTTON_FOOTER))
        text = element3.text
        if text == data.telefoonNummerButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_mail_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Mail button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_MAIL_BUTTON_FOOTER))
        if element == True:
            print("CORRECT: Mail button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_MAIL_BUTTON_FOOTER) == True:
                print ("CORRECT: Mail button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_MAIL_BUTTON_FOOTER) == False:
                print ("ERROR: Mail button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Mail button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_MAIL_BUTTON_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_MAIL_BUTTON_FOOTER))
        text = element3.text
        if text == data.mailButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_nieuwsbrief_button_footer (self):
        logging.info("Er wordt gecontroleerd of de Nieuwsbrief button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_AANMELDEN_NIEUWSBRIEF_BUTTON_FOOTER))
        if element == True:
            print("CORRECT: Nieuwsbrief button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_AANMELDEN_NIEUWSBRIEF_BUTTON_FOOTER) == True:
                print ("CORRECT: Nieuwsbrief button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_AANMELDEN_NIEUWSBRIEF_BUTTON_FOOTER) == False:
                print ("ERROR: Nieuwsbrief button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Nieuwsbrief button is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_AANMELDEN_NIEUWSBRIEF_BUTTON_FOOTER))
        text = element3.text
        if text == data.aanmeldenNieuwsBriefButtonFooter:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")

    def check_sysqa_nieuwsbrief_aanmelden_popup_zichtbaar (self):
        logging.info("Er wordt gecontroleerd of de Nieuwsbrief aanmelden popup correct werkt")
        element = (self.find(loc.WerkenBijSysqaGUI.SYSQA_AANMELDEN_NIEUWSBRIEF_BUTTON_FOOTER))
        element.click()
        popup = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP))
        visible = popup.get_attribute("class")
        print(visible)
        if visible == data.nieuwsbriefPopupVisible:
            print("CORRECT: Popup is zichtbaar")
        else:
            print("ERROR: Popup is niet zichtbaar")

    def check_sysqa_nieuwsbrief_aanmelden_popup_text (self):
        logging.info("Er wordt gecontroleerd of de Nieuwsbrief aanmelden popup text correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_TEXT))
        if element == True:
            print("CORRECT: Nieuwsbrief aanmelden popup text is aanwezig")
            element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_TEXT))
            print(element2.text)
            if element2.text == data.nieuwsbriefPopupText:
                print("CORRECT: Nieuwsbrief aanmelden popup text is correct")
            elif element2.text != data.nieuwsbriefPopupText:
                print("ERROR: Nieuwsbrief aanmelden popup text is niet correct")
        elif element == False:
            print("ERROR: Nieuwsbrief aanmelden popup text is niet aanwezig")

    def check_sysqa_nieuwsbrief_aanmelden_naam_box (self):
        logging.info("Er wordt gecontroleerd of de Nieuwsbrief aanmelden popup naam box correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_NAAM))
        if element == True:
            print("CORRECT: Nieuwsbrief aanmelden popup naam box is aanwezig")
            element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_NAAM))
            text = element2.get_attribute("placeholder")
            if text == data.nieuwsbriefPopupNaamText:
                print("CORRECT: Nieuwsbrief aanmelden popup naam text is correct")
            elif text != data.nieuwsbriefPopupNaamText:
                print("ERROR: Nieuwsbrief aanmelden popup naam text is niet correct")
        elif element == False:
            print("ERROR: Nieuwsbrief aanmelden popup naam is niet aanwezig")
        self.schrijf(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_NAAM, "Thijs van Opstal")

    def check_sysqa_nieuwsbrief_aanmelden_email_box (self):
        logging.info("Er wordt gecontroleerd of de Nieuwsbrief aanmelden popup email box correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_EMAIL))
        if element == True:
            print("CORRECT: Nieuwsbrief aanmelden popup email box is aanwezig")
            element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_EMAIL))
            text = element2.get_attribute("placeholder")
            if text == data.nieuwsbriefPopupEmailText:
                print("CORRECT: Nieuwsbrief aanmelden popup email text is correct")
            elif text != data.nieuwsbriefPopupEmailText:
                print("ERROR: Nieuwsbrief aanmelden popup email text is niet correct")
        elif element == False:
            print("ERROR: Nieuwsbrief aanmelden popup email is niet aanwezig")
        self.schrijf(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_EMAIL, "tvanopstal@sysqa.nl")

    def check_sysqa_nieuwsbrief_aanmelden_accept_box (self):
        logging.info("Er wordt gecontroleerd of de Nieuwsbrief aanmelden popup accept box correct is")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_ACCEPTEER))
        if element == True:
            print("CORRECT: Nieuwsbrief popup accept box is aanwezig")
        elif element == False:
            print("ERROR: Nieuwsbrief aanmelden popup accept is niet aanwezig")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_ACCEPTEER))
        element2.click()
    
    def check_sysqa_nieuwsbrief_aanmelden_verstuur_box (self):
        logging.info("Er wordt gecontroleerd of de Nieuwsbrief aanmelden popup verstuur button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_VERSTUUR))
        if element == True:
            print("CORRECT: Nieuwsbrief aanmelden popup verstuur button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_VERSTUUR) == True:
                print ("CORRECT: Nieuwsbrief aanmelden popup verstuur button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_VERSTUUR) == False:
                print ("ERROR: Nieuwsbrief aanmelden popup verstuur button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Nieuwsbrief aanmelden popup verstuur button is niet aanwezig op pagina")
        element3 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_VERSTUUR))
        text = element3.text
        if text == data.nieuwsbriefPopupVerstuurText:
            print("CORRECT: Text is correct")
        else:
            print("ERROR: Text is niet correct")
        element3.click()

    def check_sysqa_nieuwsbrief_aanmelden_verificatie_text (self):
        logging.info("Er wordt gecontroleerd of de Nieuwsbrief aanmelden popup verificatie correct is")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_VERIFICATIE))
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_VERIFICATIE))
        if element == True:
            print("CORRECT: Nieuwsbrief popup verificatie is aanwezig")
            element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_NIEUWSBRIEF_POPUP_VERIFICATIE))
            if element2.text == data.nieuwsbriefPopupVerificatieText:
                print("CORRECT: Nieuwsbrief popup verificatie text is correct")
            elif element2.text != data.nieuwsbriefPopupVerificatieText:
                print("ERROR: Nieuwsbrief aanmelden popup verificatie is niet correct")
        elif element == False:
            print("ERROR: Nieuwsbrief aanmelden popup verificatie is niet aanwezig")
        
    def check_sysqa_instagram_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Instagram button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_INSTAGRAM_FOOTER))
        if element == True:
            print("CORRECT: Instagram button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_INSTAGRAM_FOOTER) == True:
                print ("CORRECT: Instagram button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_INSTAGRAM_FOOTER) == False:
                print ("ERROR: Instagram button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Instagram button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_INSTAGRAM_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")

    def check_sysqa_linkedin_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Linkedin button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_LINKEDIN_FOOTER))
        if element == True:
            print("CORRECT: Linkedin button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_LINKEDIN_FOOTER) == True:
                print ("CORRECT: Linkedin button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_LINKEDIN_FOOTER) == False:
                print ("ERROR: Linkedin button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Linkedin button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_LINKEDIN_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")

    def check_sysqa_twitter_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Twitter button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_TWITTER_FOOTER))
        if element == True:
            print("CORRECT: Twitter button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_TWITTER_FOOTER) == True:
                print ("CORRECT: Twitter button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_TWITTER_FOOTER) == False:
                print ("ERROR: Twitter button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Twitter button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_TWITTER_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")

    def check_sysqa_facebook_button_footer (self, link_URL):
        logging.info("Er wordt gecontroleerd of de Facebook button correct werkt")
        element = (self.find_element_boolean(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_FACEBOOK_FOOTER))
        if element == True:
            print("CORRECT: Facebook button is aanwezig op pagina")
            if self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_FACEBOOK_FOOTER) == True:
                print ("CORRECT: Facebook button is aanklikbaar")
            elif self.return_clickable(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_FACEBOOK_FOOTER) == False:
                print ("ERROR: Facebook button is niet aanklikbaar")
        elif element == False:
            print ("ERROR: Facebook button is niet aanwezig op pagina")
        element2 = (self.find(loc.WerkenBijSysqaGUI.SYSQA_SOCIAL_MEDIA_FACEBOOK_FOOTER))
        link = element2.get_attribute("href")
        print (link)
        if link == link_URL:
            print ("CORRECT: Link is correct")
        else:
            print ("ERROR: Link is niet correct")




