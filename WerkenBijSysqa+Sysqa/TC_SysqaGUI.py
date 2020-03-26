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

class SysqaGUI (CommonTestCase):

    """"Tests voor de Sysqa Home pagina"""

    def test_sysqa_home (self):


        self.testcase = "TC_SysqaGUI"


        sysqa = page.Sysqa(self.driver)

        #Gebruiker opent de aangemaakt testpagina met resolutie 1920 1080
        sysqa.open_sysqa_pagina()
        self.driver.set_window_size(data.homepageTabletWindowSizeWidth,data.homepageTabletWindowSizeHeight)
        self.driver.set_window_position(0,0)
        size = self.driver.get_window_size()
        print (size)

        #Gebruiker accepteert cookies
        sysqa.accept_sysqa_cookies()

        #Gebruiker controleert of het Sysqa logo correct is
        sysqa.check_navigatie_sysqa_logo()

        #Gebruiker controleert of de top Navigatie correct is
        sysqa.check_navigatie_sysqa_home()
        sysqa.check_navigatie_sysqa_over()
        sysqa.check_navigatie_sysqa_dienst()
        sysqa.check_navigatie_sysqa_blog()
        sysqa.check_navigatie_sysqa_contact()
        
        #Gebruiker controleert of de Sysqa slogan + text correct is
        sysqa.check_sysqa_home_slogan()
        sysqa.check_sysqa_home_slogan_text()
        sysqa.check_sysqa_home_contact_button_boven()
        
        #Gebruiker controleert of de Improving slogan + text correct is
        sysqa.check_sysqa_home_improving_slogan()
        sysqa.check_sysqa_home_improving_slogan_text()
        sysqa.check_sysqa_home_improving_slogan_help()

        #Gebruiker controleert of de Sysqa specialisaties correct is
        sysqa.check_sysqa_home_specialisatie_1()
        sysqa.check_sysqa_home_specialisatie_2()
        sysqa.check_sysqa_home_specialisatie_3()
        sysqa.check_sysqa_home_specialisatie_4()
        sysqa.check_sysqa_home_specialisatie_5()
        sysqa.check_sysqa_home_meer_over_button()
        
        #Gebruiker controleert of de alle artikelen button correct is
        sysqa.check_sysqa_home_alle_artikelen_button()
        
        #Gebruiker controleert of de footer navigatie correct is
        sysqa.check_sysqa_home_footer_sysqa()
        sysqa.check_sysqa_home_footer_home()
        sysqa.check_sysqa_home_footer_over()
        sysqa.check_sysqa_home_footer_diensten()
        sysqa.check_sysqa_home_footer_blog()
        sysqa.check_sysqa_home_footer_contact()
        sysqa.check_sysqa_home_footer_werken()

        #Gebruiker controleert of de footer blog onderwerpen correct zijn
        sysqa.check_sysqa_home_footer_blog_thema()
        sysqa.check_sysqa_home_footer_onderwerp_1()
        sysqa.check_sysqa_home_footer_onderwerp_2()
        sysqa.check_sysqa_home_footer_onderwerp_3()
        sysqa.check_sysqa_home_footer_onderwerp_4()
        sysqa.check_sysqa_home_footer_onderwerp_5()
        sysqa.check_sysqa_home_footer_onderwerp_6()
        sysqa.check_sysqa_home_footer_onderwerp_7()
        sysqa.check_sysqa_home_footer_onderwerp_8()
        sysqa.check_sysqa_home_footer_onderwerp_9()
        sysqa.check_sysqa_home_footer_onderwerp_10()
        
        #Gerbruiker controleert of de footer adres + contact correct is
        sysqa.check_sysqa_home_footer_contact_text()
        sysqa.check_sysqa_home_footer_contact_adres()
        sysqa.check_sysqa_home_footer_contact_maps()
        sysqa.check_sysqa_home_footer_contact_telefoon()
        sysqa.check_sysqa_home_footer_contact_email()
        sysqa.check_sysqa_home_footer_contact_nieuwsbrief()

        #Gebruiker controleert of de nieuwsbrief popup correct is
        sysqa.check_sysqa_home_nieuwsbrief_popup_text()
        sysqa.check_sysqa_home_nieuwsbrief_popup_naam()
        sysqa.check_sysqa_home_nieuwsbrief_popup_email()
        sysqa.check_sysqa_home_nieuwsbrief_popup_voorwaarden()
        sysqa.check_sysqa_home_nieuwsbrief_popup_versturen()
        sysqa.check_sysqa_home_nieuwsbrief_popup_error()
        






if __name__ == "__main__":
    if len(sys.argv) >1:
        SysqaGUI.pipeline = sys.argv.pop()
    unittest.main()