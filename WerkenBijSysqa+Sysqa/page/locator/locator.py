from selenium.webdriver.common.by import By


                            
class WerkenBijSysqaGUI ():
    SYSQA_NAV_LOGO = (By.XPATH, "/html/body/div/div/nav/div/div/a")
    SYSQA_NAV_HOME_BUTTON = (By.XPATH, "//ul[@class='navbar-items d-none d-lg-flex']//a[contains(text(),'Home')]")
    SYSQA_NAV_VACATURES_BUTTON = (By.XPATH, "/html/body/div/div/nav/div/ul/li[2]/a")
    SYSQA_NAV_VERHALEN_BUTTON = (By.XPATH, "/html/body/div/div/nav/div/ul/li[3]/a")
    SYSQA_NAV_KENNISMAKEN_BUTTON = (By.XPATH, "/html/body/div/div/nav/div/ul/li[4]/a")
    SYSQA_NAV_TELEFOON_BUTTON = (By.XPATH, "/html/body/div/div/nav/div/ul/li[5]/a")
    SYSQA_COOKIES_ACCEPT = (By.ID, "CybotCookiebotDialogBodyLevelButtonAccept")


    SYSQA_ZIJKANT_KENNISMAKEN_BUTTON = (By.XPATH, "/html/body/div/div/a[1]")
    SYSQA_KENNISMAKEN_BUTTON = (By.XPATH, "//a[@class='button button-alt mt-5']")
    SYSQA_KENNISMAKEN_TITEL = (By.XPATH, "/html/body/div/div/div/div[6]/div/div/div/div/h2/div/h2")
    SYSQA_KENNISMAKEN_BUTTON_ONDER = (By.XPATH, "/html/body/div/div/div/div[6]/div/div/div/div[2]/a")
    SYSQA_KENNISMAKEN_BUTTON_FOOTER = (By.XPATH, "//ul[@class='mt-4']//div[contains(text(),'Kennismaken')]")
    SYSQA_KENNISMAKEN_BUTTON_FOOTER_TEKST = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div/ul/li[4]/a")

    SYSQA_SLOGAN_1 = (By.XPATH, "//strong[contains(text(),'Werken in')]")
    SYSQA_SLOGAN_2 = (By.XPATH, "//strong[contains(text(),'Business en IT')]")
    SYSQA_SLOGAN_3 = (By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/h3")
    
 
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
    
    SYSQA_DOE_DE_TEST_BUTTON_FOOTER = (By.XPATH, "//a[@class='button button-line-default mt-4']")
    SYSQA_HOME_BUTTON_FOOTER = (By.XPATH, "//ul[@class='mt-4']//a[contains(text(),'Home')]")
    SYSQA_VACATURES_BUTTON_FOOTER = (By.XPATH, "//ul[@class='mt-4']//div[contains(text(),'Vacatures')]")
    SYSQA_VACATURES_BUTTON_FOOTER_TEKST = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div/ul/li[2]/a")
    SYSQA_VERHALEN_EN_VIDEOS_BUTTON_FOOTER = (By.XPATH, "//ul[@class='mt-4']//div[contains(text(),'Verhalen en Video')]")
    SYSQA_VERHALEN_EN_VIDEOS_BUTTON_FOOTER_TEKST = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div/ul/li[3]/a")
    
    SYSQA_CONTACT_ADRES_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div/div[2]/a")
    SYSQA_CORPORATE_WEBSITE_BUTTON_FOOTER = (By.XPATH, "//a[contains(text(),'Corporate website')]")
    SYSQA_GOOGLE_MAPS_BUTTON_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div/div[3]/div[2]/a")
    SYSQA_TELEFOON_NUMMER_BUTTON_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div/div[3]/div[3]/a")
    SYSQA_MAIL_BUTTON_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/div/div[3]/div[4]/a")
    
    SYSQA_AANMELDEN_NIEUWSBRIEF_BUTTON_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/button")
    SYSQA_NIEUWSBRIEF_POPUP = (By.XPATH, "//div[@class='box news-letter color-background-main color-text-light py-3 px-4']")
    SYSQA_NIEUWSBRIEF_POPUP_TEXT = (By.XPATH, "//div[@class='pr-5']")
    SYSQA_NIEUWSBRIEF_POPUP_NAAM = (By.XPATH, "/html/body/div/div/div[3]/div[2]/form/div/div[1]/div/div/input")
    SYSQA_NIEUWSBRIEF_POPUP_EMAIL = (By.XPATH, "/html/body/div/div/div[3]/div[2]/form/div/div[2]/div/div/input")
    SYSQA_NIEUWSBRIEF_POPUP_ACCEPTEER = (By.ID, "input_accept")
    SYSQA_NIEUWSBRIEF_POPUP_VERSTUUR = (By.XPATH, "//form[@class='form form_4']//button[@class='button form-submit'][contains(text(),'Versturen')]")
    SYSQA_NIEUWSBRIEF_POPUP_VERIFICATIE = (By.XPATH, "/html/body/div/div/div[3]/div[2]/div")
    
    SYSQA_SOCIAL_MEDIA_INSTAGRAM_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div/a[1]")
    SYSQA_SOCIAL_MEDIA_LINKEDIN_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div/a[2]")
    SYSQA_SOCIAL_MEDIA_TWITTER_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div/a[3]")
    SYSQA_SOCIAL_MEDIA_FACEBOOK_FOOTER = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div/a[4]")

    SYSQA_EMAIL_ICON = (By.ID, "maximizeChat")

class WerkenBijSysqaVacaturesGUI ():
    SYSQA_VACATURES_SLOGAN_1 = (By.XPATH, "//strong[contains(text(),'ONZE VACATURES')]")
    SYSQA_VACATURES_SLOGAN_2 = (By.XPATH, "//h3[@class='banner-home-slogan mt-2 font-weight-s font-size-xl']")
    
    SYSQA_VACATURES_BEKIJK_VACATURE_1 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/a/div[2]/div[2]/div")
    SYSQA_VACATURES_BEKIJK_VACATURE_2 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/a/div[2]/div[2]/div")
    SYSQA_VACATURES_BEKIJK_VACATURE_3 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[3]/a/div[2]/div[2]/div")
    SYSQA_VACATURES_BEKIJK_VACATURE_4 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[4]/a/div[2]/div[2]/div")
    SYSQA_VACATURES_BEKIJK_VACATURE_5 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[5]/a/div[2]/div[2]/div")
    SYSQA_VACATURES_BEKIJK_VACATURE_6 = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[6]/a/div[2]/div[2]/div")
    
    SYSQA_VACATURES_KENNISMAKEN_SLOGAN = (By.XPATH, "//p[contains(text(),'Klaar voor je volgende stap?')]")
    SYSQA_VACATURES_KENNISMAKEN_BUTTON_MIDDEN = (By.XPATH, "/html/body/div/div/div/div[3]/div/div/div/div[2]/a")
    
    SYSQA_VACATURES_STORIES_TITEL = (By.XPATH, "//h2[@class='title title-upper title-default']")
    SYSQA_VACATURES_STORIES_BEKIJK_1 = (By.XPATH, "/html/body/div/div/div/div[4]/div/div/a[1]/div/div[2]/div[2]/span")
    SYSQA_VACATURES_STORIES_BEKIJK_2 = (By.XPATH, "/html/body/div/div/div/div[4]/div/div/a[2]/div/div[2]/div[2]/span")
    SYSQA_VACATURES_STORIES_BEKIJK_3 = (By.XPATH, "/html/body/div/div/div/div[4]/div/div/a[3]/div/div[2]/div[2]/span")
    SYSQA_VACATURES_ALLE_STORIES = (By.XPATH, "/html/body/div/div/div/div[4]/div[2]/a")

class WerkenBijSysqaVerhalenGUI ():
    SYSQA_VERHALEN_SLOGAN_1 = (By.XPATH, "//strong[contains(text(),'Verhalen en Video')]")
    SYSQA_VERHALEN_SLOGAN_2 = (By.XPATH, "//h3[@class='banner-home-slogan mt-2 font-weight-s font-size-xm pr-lg-4 w-100']")
    
    SYSQA_VERHALEN_SEARCH_BOX = (By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/form/input")
    SYSQA_VERHALEN_SEARCH_BUTTON = (By.XPATH, "//button[@class='field-search-submit']")
    SYSQA_VERHALEN_RESET_BUTTON = (By.XPATH, "/html/body/div/div/div/div[2]/div/button")

    SYSQA_VERHALEN_ONDERWERP_TITEL = (By.XPATH, "//span[@class='color-text-secondary']")
    SYSQA_VERHALEN_ONDERWERP_1 = (By.XPATH, "/html/body/div/div/div/div[2]/div[2]/button[1]")
    SYSQA_VERHALEN_ONDERWERP_2 = (By.XPATH, "/html/body/div/div/div/div[2]/div[2]/button[2]")
    SYSQA_VERHALEN_ONDERWERP_3 = (By.XPATH, "/html/body/div/div/div/div[2]/div[2]/button[3]")
    SYSQA_VERHALEN_ONDERWERP_4 = (By.XPATH, "/html/body/div/div/div/div[2]/div[2]/button[4]")
    SYSQA_VERHALEN_ONDERWERP_5 = (By.XPATH, "/html/body/div/div/div/div[2]/div[2]/button[5]")
    SYSQA_VERHALEN_ONDERWERP_6 = (By.XPATH, "/html/body/div/div/div/div[2]/div[2]/button[6]")
    SYSQA_VERHALEN_LAAD_MEER_BUTTON = (By.XPATH, "//button[@class='button button-line-default button-line-default-more']")

    SYSQA_VERHALEN_KENNISMAKEN_SLOGAN = (By.XPATH, "//h2[contains(text(),'Are you ready for your next big step?')]")
    SYSQA_VERHALEN_KENNISMAKEN_BUTTON_MIDDEN = (By.LINK_TEXT, "KOM KENNISMAKEN!")

    SYSQA_VERHALEN_VACATURE_SLOGAN = (By.XPATH, "//h2[@class='title title-upper title-default']")
    SYSQA_VERHALEN_VACATURE_1 = (By.XPATH, "/html/body/div/div/div/div[5]/div/div/div[1]/a/div[2]/div[2]/div")
    SYSQA_VERHALEN_VACATURE_2 = (By.XPATH, "/html/body/div/div/div/div[5]/div/div/div[2]/a/div[2]/div[2]/div")
    SYSQA_VERHALEN_VACATURE_3 = (By.XPATH, "/html/body/div/div/div/div[5]/div/div/div[3]/a/div[2]/div[2]/div")
    SYSQA_VERHALEN_VACATURE_LAAD_MEER = (By.XPATH, "//a[@class='button button-line-default']")

class WerkenBijSysqaKennismakenGUI ():
    SYSQA_KENNISMAKEN_SLOGAN = (By.XPATH, "//h2[@class='title title-upper title-alt']")
    
    SYSQA_KENNISMAKEN_NAAM_TEXT = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div/div[1]/div/div/label")
    SYSQA_KENNISMAKEN_NAAM_BOX = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div/div[1]/div/div/input")
    SYSQA_KENNISMAKEN_EMAIL_TEXT = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div/div[2]/div/div/label")
    SYSQA_KENNISMAKEN_EMAIL_BOX = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div/div[2]/div/div/input")
    SYSQA_KENNISMAKEN_BERICHT_TEXT = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div/div[3]/div/label")
    SYSQA_KENNISMAKEN_BERICHT_BOX = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div/div[3]/div/textarea")
    SYSQA_KENNISMAKEN_VOORWAARDEN_TEXT = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div/div[4]/div/div/div/label")
    SYSQA_KENNISMAKEN_VOORWAARDEN_LINK = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div/div[4]/div/div/div/label/a")
    SYSQA_KENNISMAKEN_VOORWAARDEN_CHECKBOX = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div/div[4]/div/div/div/input")

    SYSQA_KENNISMAKEN_UPDATES_SLOGAN = (By.XPATH, "//div[@class='title title-upper title-sub-alt']")
    SYSQA_KENNISMAKEN_UPDATES_TEXT = (By.XPATH, "//div[@class='content mt-4']")
    SYSQA_KENNISMAKEN_AANMELDEN_NIEUWSBRIEF = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button/span")

    SYSQA_RECAPTCHA_IFRAME = (By.XPATH, "//iframe[@name='a-5g5gpv3752qq']")
    SYSQA_RECAPTCHA_ACCEPT = (By.ID, "recaptcha-anchor")
    SYSQA_RECAPTCHA_VERSTUREN = (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div/div[4]/div[3]/button")
    
class SysqaHomeGUI ():
    SYSQA_HOME_NAV_LOGO = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/a[1]")
    SYSQA_HOME_NAV_HOME = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]")
    SYSQA_HOME_NAV_OVER = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")
    SYSQA_HOME_NAV_DIENSTEN = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]")
    SYSQA_HOME_NAV_BLOG = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]")
    SYSQA_HOME_NAV_CONTACT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]")

    SYSQA_HOME_TITEL = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]")
    SYSQA_HOME_TEXT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h3[1]/div[1]/p[1]")
    SYSQA_HOME_CONTACT_BUTTON_BOVEN = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
    














