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

class SysqaOverGUI (CommonTestCase):

    """"Tests voor de Sysqa Over pagina"""

    def test_sysqa_over (self):


        self.testcase = "TC_SysqaOverGUI"


        sysqa = page.Sysqa(self.driver)
        over = page.SysqaOver(self.driver)

        #Gebruiker opent de aangemaakt testpagina met resolutie 1920 1080
        over.open_sysqa_pagina()
        self.driver.set_window_size(data.homepageDesktopWindowSizeWidth,data.homepageDesktopWindowSizeHeight)
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

        #Gebruiker controleert slogan + contact boven of de correct is
        over.check_sysqa_over_slogan()
        over.check_sysqa_over_contact_button_boven()
        
        #Gebruiker controleert of de text correct is
        over.check_sysqa_over_text()

        #Gebruiker controleert of de improving + specialisatie correct is
        over.check_sysqa_over_improving_slogan()
        over.check_sysqa_over_improving_text_1()
        over.check_sysqa_over_improving_text_2()
        over.check_sysqa_over_specialisatie_1()
        over.check_sysqa_over_specialisatie_2()
        over.check_sysqa_over_specialisatie_3()
        over.check_sysqa_over_specialisatie_4()
        over.check_sysqa_over_specialisatie_5()
        over.check_sysqa_over_specialisatie_text()

        #Gebruiker controleert of de video correct is
        over.check_sysqa_over_video_text()
        over.check_sysqa_over_video()

        #Gebruiker controleert of de vakgebieden correct is
        over.check_sysqa_over_vakgebieden_titel()
        over.check_sysqa_over_vakgebieden_text_1()
        over.check_sysqa_over_vakgebieden_text_lijst_1()
        over.check_sysqa_over_vakgebieden_text_lijst_2()
        over.check_sysqa_over_vakgebieden_text_lijst_3()
        over.check_sysqa_over_vakgebieden_text_2()
        over.check_sysqa_over_professionals_titel()
        over.check_sysqa_over_professionals_text()

        #Gebruiker controleert of de dna correct is
        over.check_sysqa_over_dna_titel()
        over.check_sysqa_over_dna_text()

        #Gebruiker controleert of de 3 kolommen correct is
        over.check_sysqa_over_betekenis_titel()
        over.check_sysqa_over_betekenis_text_1()
        over.check_sysqa_over_betekenis_text_2()
        over.check_sysqa_over_verbinding_titel()
        over.check_sysqa_over_verbinding_text_1()
        over.check_sysqa_over_verbinding_text_2()
        over.check_sysqa_over_ontwikkeling_titel()
        over.check_sysqa_over_ontwikkeling_text_1()
        over.check_sysqa_over_ontwikkeling_text_2()
        over.check_sysqa_over_contact_onder()

        #Gebruiker controleert of de blog correct is
        over.check_sysqa_over_blog_titel()
        over.check_sysqa_over_blog_artikelen()
        
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
        
        #Gebruiker controleert of de socials correct zijn
        sysqa.check_sysqa_instagram_button_footer()
        sysqa.check_sysqa_linkedin_button_footer()
        sysqa.check_sysqa_twitter_button_footer()
        sysqa.check_sysqa_facebook_button_footer()





if __name__ == "__main__":
    if len(sys.argv) >1:
        SysqaOverGUI.pipeline = sys.argv.pop()
    unittest.main()