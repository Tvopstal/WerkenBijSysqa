from selenium.webdriver.common.by import By


                            
class WerkenBijSysqaGUI ():
    SYSQA_NAV_LOGO = (By.XPATH, "/html/body/div/div/nav/div/div/a")
    SYSQA_NAV_HOME_BUTTON = (By.XPATH, "//ul[@class='navbar-items d-none d-lg-flex']//a[contains(text(),'Home')]")
    SYSQA_NAV_VACATURES_BUTTON = (By.XPATH, "/html/body/div/div/nav/div/ul/li[2]/a")
    SYSQA_NAV_VERHALEN_BUTTON = (By.XPATH, "/html/body/div/div/nav/div/ul/li[3]/a")
    SYSQA_NAV_KENNISMAKEN_BUTTON = (By.XPATH, "/html/body/div/div/nav/div/ul/li[4]/a")
    SYSQA_NAV_TELEFOON_BUTTON = (By.XPATH, "/html/body/div/div/nav/div/ul/li[5]/a")
    
    SYSQA_ZIJKANT_KENNISMAKEN_BUTTON = (By.XPATH, "/html/body/div/div/a[1]")
    SYSQA_SLOGAN_1 = (By.XPATH, "//strong[contains(text(),'Werken in')]")
    SYSQA_SLOGAN_2 = (By.XPATH, "//strong[contains(text(),'Business en IT')]")
    SYSQA_SLOGAN_3 = (By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/h3")
    SYSQA_KENNISMAKEN_BUTTON = (By.XPATH, "//a[@class='button button-alt mt-5']")
    SYSQA_TITEL = (By.XPATH, "/html/body/div/div/div/div[2]/div/h2")
    SYSQA_TEXT_1 = (By.XPATH, "//p[contains(text(),'Wij verbeteren de digitale wereld! Met slimme Youn')]")
    SYSQA_KOP_TITEL = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/h3")
    SYSQA_TEXT_2 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/p[2]")
    SYSQA_VACATURES_TITEL = (By.XPATH, "/html/body/div/div/div/div[3]/h2")
    SYSQA_UITGELICHTE_VACATURES = (By.XPATH, "//div[@class='container pb-5 mb-3']//div[@class='pt-2']")
    SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_1 = (By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[1]/a/div[2]/div[2]/div")
    SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_2 = (By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[2]/a/div[2]/div[2]/div")
    SYSQA_UITGELICHTE_VACATURE_BEKIJKEN_3 = (By.XPATH, "/html/body/div/div/div/div[3]/div/div/div[3]/a/div[2]/div[2]/div")
    SYSQA_BEKIJK_AL_ONZE_VACATURES_BUTTON = (By.XPATH, "/html/body/div/div/div/div[3]/div[2]/a")
    SYSQA_BEKIJK_ALLE_VERHALEN_EN_VIDEOS = (By.XPATH, "/html/body/div/div/div/div[5]/div[2]/a")
    SYSQA_KENNISMAKEN_TITEL = (By.XPATH, "/html/body/div/div/div/div[6]/div/div/div/div/h2/div/h2")
    SYSQA_KENNISMAKEN_BUTTON_ONDER = (By.XPATH, "/html/body/div/div/div/div[6]/div/div/div/div[2]/a")
    SYSQA_DOE_DE_TEST_BUTTON_FOOTER = (By.XPATH, "//a[@class='button button-line-default mt-4']")
    SYSQA_HOME_BUTTON_FOOTER = (By.XPATH, "//ul[@class='mt-4']//a[contains(text(),'Home')]")
    SYSQA_VACATURES_BUTTON_FOOTER = (By.XPATH, "//ul[@class='mt-4']//div[contains(text(),'Vacatures')]")
    SYSQA_VACATURES_BUTTON_FOOTER_TEKST = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div/ul/li[2]/a")
    SYSQA_VERHALEN_EN_VIDEOS_BUTTON_FOOTER = (By.XPATH, "//ul[@class='mt-4']//div[contains(text(),'Verhalen en Video')]")
    SYSQA_VERHALEN_EN_VIDEOS_BUTTON_FOOTER_TEKST = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div/ul/li[3]/a")
    SYSQA_KENNISMAKEN_BUTTON_FOOTER = (By.XPATH, "//ul[@class='mt-4']//div[contains(text(),'Kennismaken')]")
    SYSQA_KENNISMAKEN_BUTTON_FOOTER_TEKST = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div/ul/li[4]/a")
    SYSQA_CONTACT_ADRES_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div/div[2]/a")
    SYSQA_CORPORATE_WEBSITE_BUTTON_FOOTER = (By.XPATH, "//a[contains(text(),'Corporate website')]")
    SYSQA_GOOGLE_MAPS_BUTTON_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div/div[3]/div[2]/a")
    SYSQA_TELEFOON_NUMMER_BUTTON_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div/div[3]/div[3]/a")
    SYSQA_MAIL_BUTTON_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div/div[3]/div[4]/a")
    SYSQA_AANMELDEN_NIEUWSBRIEF_BUTTON_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/button/span")
    SYSQA_NIEUWSBRIEF_POPUP = (By.XPATH, "/html/body/div/div/div[3]")
    SYSQA_NIEUWSBRIEF_POPUP_TEXT = (By.XPATH, "//div[@class='pr-5']")
    SYSQA_NIEUWSBRIEF_POPUP_NAAM = (By.ID, "input_1")
    SYSQA_NIEUWSBRIEF_POPUP_EMAIL = (By.ID, "input_2")
    SYSQA_NIEUWSBRIEF_POPUP_ACCEPTEER = (By.ID, "input_accept")
    SYSQA_NIEUWSBRIEF_POPUP_VERSTUUR = (By.XPATH, "//button[@class='button form-submit']")
    SYSQA_NIEUWSBRIEF_POPUP_VERIFICATIE = (By.ID, "gform_confirmation_message_4")
    SYSQA_SOCIAL_MEDIA_INSTAGRAM_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div/a[1]")
    SYSQA_SOCIAL_MEDIA_LINKEDIN_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div/a[2]")
    SYSQA_SOCIAL_MEDIA_TWITTER_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div/a[3]")
    SYSQA_SOCIAL_MEDIA_FACEBOOK_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div/a[4]")

class WerkenBijSysqaVacaturesGUI ():
    









