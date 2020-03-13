import base64
import logging
import subprocess
import sys
import time
import unittest
from datetime import datetime, timedelta

import data
import driver
import page
from Extra.commonUnitTest import CommonTestCase

class WerkenBijSysqaGUI (CommonTestCase):

    """"Tests voor de WerkenBijSysqa Home pagina"""

    def test_werkenbij_sysqa_home (self):


        self.testcase = "TC_werkenBij_WerkenBijSysqaGUI"

        link_home_URL = data.werkenBijSysqaPaginaHome
        link_vacatures_URL = data.werkenBijSysqaPaginaVacatures
        link_verhalen_URL = data.werkenBijSysqaPaginaVerhalen
        link_kennismaken_URL = data.werkenBijSysqaPaginaKennismaken
        link_kennismaken_URL2 = data.werkenBijSysqaPaginaKennismaken2
        tel_nummer = data.werkenBijSysqaTelefoonNummer
        link_verhalen_en_videos_URL = data.werkenBijSysqaPaginaVerhalenEnVideos
        link_quiz_URL = data.werkenBijSysqaPaginaQuiz


        sysqa = page.WerkenBijSysqa(self.driver)

        #Gebruiker opent de aangemaakt testpagina met resolutie 1920 1080
        sysqa.open_sysqa_pagina()
        self.driver.set_window_size(data.homepageDesktopWindowSizeWidth,data.homepageDesktopWindowSizeHeight)
        self.driver.set_window_position(0,0)
        size = self.driver.get_window_size()
        print (size)
        
        #Gebruiker controleert of het SYSQA logo correct werkt
        sysqa.check_navigatie_sysqa_logo(link_home_URL)

        #Gebruiker controleert of de Home button correct werkt 
        sysqa.check_navigatie_home_button(link_home_URL)

        #Gebruiker controleert of de Vacatures button correct werkt
        sysqa.check_navigatie_vacatures_button(link_vacatures_URL)

        #Gebruiker controleert of de Verhalen button correct werkt
        sysqa.check_navigatie_verhalen_button(link_verhalen_URL)

        #Gebruiker controleert of de Kennismaken button correct werkt
        sysqa.check_navigatie_kennismaken_button(link_kennismaken_URL)

        #Gebruiker controleert of het telefoonnummer correct werkt
        sysqa.check_navigatie_telefoon_button(tel_nummer)

        #Gebruiker controleert of de slogan correct is
        sysqa.check_sysqa_slogan_1()
        sysqa.check_sysqa_slogan_2()
        sysqa.check_sysqa_slogan_3()

        #Gebruiker controleert of de kennismaken button correct werkt
        sysqa.check_sysqa_kennismaken_button_boven(link_kennismaken_URL2)

        #Gebruiker controleert of de titel en textstuk correct is
        sysqa.check_sysqa_titel()
        sysqa.check_sysqa_text_1()
        sysqa.check_sysqa_kop_titel()
        sysqa.check_sysqa_text_2()

        #Gebruiker controleert of de Vactures titel correct is
        sysqa.check_sysqa_vacatures_titel() 

        #Gebruiker controleert of de uitgelichte vacatures aanwezig zijn
        sysqa.check_sysqa_uitgelichte_vacatures()
        sysqa.check_sysqa_uitgelichte_vacatures_bekijken_1()
        sysqa.check_sysqa_uitgelichte_vacatures_bekijken_2()
        sysqa.check_sysqa_uitgelichte_vacatures_bekijken_3()

        #Gebruiker controleert of de BEKIJK AL ONZE VACATURES button correct is/werkt
        sysqa.check_sysqa_bekijk_al_onze_vacatures_button()

        #Gebruiker controleert of de BEKIJK ALLE VERHALEN EN VIDEO'S button correct is
        sysqa.check_sysqa_bekijk_alle_verhalen_button(link_verhalen_en_videos_URL)

        #Gebruiker controleert of de kennismaken titel correct is
        sysqa.check_sysqa_kennismaken_titel()

        #Gebruiker controleert of de kennismaken button onder correct werkt/is
        sysqa.check_sysqa_kennismaken_button_onder(link_kennismaken_URL)

        #Gebruiker controleert of de Doe de Test button correct werkt/is
        sysqa.check_sysqa_quiz_button_footer(link_quiz_URL)

        #Gebruiker controleert of de navigatie buttons in de footer correct werken
        sysqa.check_sysqa_home_button_footer(link_home_URL)
        sysqa.check_sysqa_vacatures_button_footer(link_vacatures_URL)
        sysqa.check_sysqa_verhalen_en_videos_button_footer(link_verhalen_URL)
        sysqa.check_sysqa_kennismaken_button_footer(link_kennismaken_URL)











if __name__ == "__main__":
    if len(sys.argv) >1:
        WerkenBijSysqaGUI.pipeline = sys.argv.pop()
    unittest.main()