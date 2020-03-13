import logging, time, os, json

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, NoSuchAttributeException, ElementClickInterceptedException

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    verplichtveld = {}
    
    def __init__(self, driver):
        self.driver = driver

    def is_url_matches(self, url):
        """Verifies that the harcoded URL appears"""
        print (self.driver.current_url)
        assert self.driver.current_url == url, "Configuratiespagina URL niet correct"
        logging.info("ASSERTED: Pagina URL correct")
    
    def is_title_matches(self, title):
        assert self.driver.wait.until(lambda _: title in self.driver.title), "Paginatitel niet correct"
        logging.info("ASSERTED: Paginatitel correct")
    
    def is_in(self, value, to_match):
        assert value in to_match
        logging.info(f"ASSERTED: {value} is in {to_match}")

    def switch_to_first_frame (self, frame1):
        logging.info("Switch naar frame 1")
        self.driver.switch_to.default_content()
        self.switch_frame(frame1)

    def switch_to_second_frame (self, frame1, frame2):
        logging.info("Switch naar frame 2")
        self.driver.switch_to.default_content()
        self.switch_frame(frame1)
        self.switch_frame(frame2)

    def count_windows (self, expected_windows):
        for i in range (1000):
            lijst = 1 * expected_windows
            count = len(self.driver.window_handles)
            if lijst != count:
                continue
            elif lijst == count:      #Moet dit geen elif zijn?
                print (f'Verwachte geopende vensters: "{lijst}" zijn gelijk aan werkelijke geopende vensters: "{count}"')
                break

    def page_has_loaded_id(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def find(self, locator):
        return self.driver.wait.until(EC.visibility_of_element_located(locator))

    def find_short(self, locator):
        return self.driver.wait_short.until(EC.visibility_of_element_located(locator))

    def find_div(self, element):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'%s')]" % element)))

    def find_page_publication_status (self, pagina):
        locator = (By.XPATH, "//div[contains(text(),'%s')]/../../td" % pagina) #Locator zoekt element op naam pagina, dan 2 elementen hoger en 1 td lager vandaar de '/../../td'
        element = self.find(locator)
        attribute = element.get_attribute('value')
        return attribute

    def vind(self, locator):
        return self.driver.wait.until(EC.presence_of_element_located(locator))

    def clickable(self, locator):
        return self.driver.wait.until(EC.element_to_be_clickable(locator))

    def return_clickable (self, locator):
        try:
            self.driver.wait_short.until(EC.element_to_be_clickable(locator))
            return True
        except NoSuchElementException:
            print ("ERROR: Element is niet gevonden, er kon niet worden bepaald of het element aan te klikken is")

    def return_clickable_element (self, element):
        if element.is_enabled():
            return True
        else:
            return False

    def clickable_div (self, element):
        return self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'%s')]" % element)))
    
    def not_find(self, locator):
        return self.driver.wait.until(EC.invisibility_of_element(locator))

    def can_find(self, locator):
        try:
            self.find(locator)
            return True
        except:
            return False

    def get_table_list (self, locator, tagname):
        elements = self.driver.find_elements(By.TAG_NAME, (('%s') % tagname))
        return elements

    def find_publication (self, publication):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'%s')]" % publication)))
        # locator = self.find("//div[contains(text(),'%s')]" % publication)
        # element = self.driver.wait.until(EC.visibility_of_element_located(locator))
        # element = self.find("//div[contains(text(),'%s')]" % publication)
        # return element

    def find_schema (self, schema):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'%s')]" % schema)))
        # element = self.driver.find_element_by_xpath("//div[contains(text(),'%s')]" % schema)
        # return element

    def find_dashboard_button (self, button):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(),'%s')]" % button)))
        # element = self.driver.find_element_by_xpath("//td[contains(text(),'%s')]" % button)
        # return element

    def find_folder (self, folder):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'%s')]" % folder)))
        # element = self.driver.find_element_by_xpath("//div[contains(text(),'%s')]" % folder)
        # return element

    def find_menu_item (self, menu_item):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'%s')]" % menu_item)))

    def move_to_and_open (self, folder):
        a = ActionChains(self.driver)
        element = self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'%s')]" % folder)))
        a.move_to_element(element)
        a.double_click(on_element=element)
        a.perform()

    def find_folder_span (self, folder):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'%s')]" % folder)))

    def find_icon (self, icon_name):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'%s')]" % icon_name)))
        # element = self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % icon_name)
        # return element

    def find_building_block (self, folder):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'%s')]" % folder)))
        # element = self.driver.find_element_by_xpath("//span[contains(text(),'%s')]" % folder)
        # return element

    def find_component (self, component):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='%s']" % component)))
        # element = self.driver.find_element_by_xpath("//div[text()='%s']" % component)
        # return element

    def find_component_span (self, component):
        return self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'%s')]" % component)))
        # element = self.driver.find_element_by_xpath("//div[text()='%s']" % component)
        # return element

    def kan_vinden(self, to_find_locator):
        assert self.driver.wait.until(EC.visibility_of_element_located(to_find_locator))

    def kan_niet_vinden(self, to_find_locator):
        assert self.driver.wait.until(EC.invisibility_of_element(to_find_locator))

    def can_not_find(self, locator):
        try:
            self.not_find(locator)
            return True
        except:
            return False

    def switch_to_alert (self):
        self.driver.switch_to.alert()

    def alert_wait (self):
        return self.driver.wait.until(EC.alert_is_present())

    def alert_login (self, username, password):
        return self.driver.switch_to.alert.send_keys(username + Keys.TAB + password + Keys.ENTER)

    def matches(self, value, to_match_loc):
        for _ in range(20):
            element = self.find(to_match_loc)
            attribute = element.get_attribute('value')
            to_match =  attribute if attribute else element.text
            if to_match and (value in to_match or value == to_match):
                return
            time.sleep(0.5)
        assert False
        
    def not_matches(self, value, to_match_loc):
        for _ in range(20):
            element = self.find(to_match_loc)
            value = element.get_attribute('value')
            to_match =  value if value else element.text
            if value and (value not in to_match and value != to_match):
                return
            time.sleep(0.5)
        assert False
    
    def switch_frame(self, locator):
        time.sleep(0.2)
        frame = self.find(locator)
        self.driver.switch_to.frame(frame)
    
    def click(self, locator):
        element = self.find(locator)
        element.click()

    def right_click (self, locator):
        a = ActionChains(self.driver)
        element = self.find(locator)
        a.context_click(on_element=element)
        a.perform()

    def right_click_element (self, element):
        a = ActionChains(self.driver)
        a.context_click(on_element=element)
        a.perform()

    def schrijf(self, locator, text):
        element = self.driver.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element = self.driver.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(text)

    def get_location_element (self, locator):
        element = self.find(locator)
        location = element.location
        size = element.size
        return location, size

    def drag_and_drop (self, nummer, destinationLocator, xoffset, yoffset):
        actions = ActionChains(self.driver) 
        sourceLocator = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % nummer) 
        actions.move_to_element(sourceLocator)
        actions.click_and_hold(sourceLocator) 
        actions.move_to_element_with_offset(destinationLocator, xoffset, yoffset)
        actions.release()
        actions.perform()

    def move_to_element (self, locator):
        a = ActionChains(self.driver)
        element = self.find(locator)
        a.move_to_element(element)
        a.click(element)
        a.perform()

    def drag_and_drop_2 (self, nummer, destinationLocator):
        actions = ActionChains(self.driver) 
        sourceLocator = self.driver.find_element_by_xpath("//a[contains(text(),'%s')]" % nummer) 
        actions.move_to_element(sourceLocator)        
        actions.click_and_hold(sourceLocator)
        actions.move_to_element(destinationLocator)   
        actions.release(sourceLocator)     
        actions.perform()
    
    def button_is_active(self, locator):
        return self.driver.wait.until(lambda _: self.find(locator).get_attribute("aria-selected") == "true")

    def opslaan_nummer(self, locator):
        element = self.find(locator).text
        return element

    def opslaan_nummer_1(self, locator):
        nummer = self.find(locator).get_attribute("value")
        wegteschrijven = {"configuratie_nummer":nummer}
        self.schrijfweg(wegteschrijven, True)
        
    def klikbaar_ja(self, locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()
 
    def find_text(self, text):
        self.driver.find_element_by_xpath('//html/body/div/div[4]/div[2]/div[2]/div[2]/div[4]/div/*[text()="%s"]' % text).click()

    def vind_tekst (self, tekst):
        element = self.driver.find_element_by_xpath("//*[text()='%s']" % tekst)
        return element

    def vind_tekst_2 (self, tekst):
        element = self.driver.find_element_by_xpath("/html/body/div[9]/ul/li[3]/div/table/tbody/tr/td[text()='%s']" % tekst)
        return element

    def vind_perceelschip (self, tekst):
        element = self.driver.find_element_by_xpath("//html/body/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/form/table/tbody/tr/td/span[text()='%s']" % tekst)
        return element

    def find_ship(self, schip):
        actions = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath("/html/body/div[9]/ul/*/div/table/tbody/tr/td[text()='%s']" % schip) 
        actions.move_to_element(element)   
        actions.perform()     
        actions.click(element)
        actions.send_keys(Keys.ENTER) 
        actions.perform()
        
    def ship_find_configuration (self, number):
        element = self.driver.find_element_by_xpath("//span[@class = 'table'][text()='%s']" % number) 
        return element

    def select (self, text, locator):
        select_element = self.driver.wait.until(EC.visibility_of_element_located(locator))
        select = Select(select_element)
        select.select_by_visible_text(text)

    def action_tab (self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        time.sleep(0.5)
        actions.perform()

    def action_enter (self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        time.sleep(0.5)
        actions.perform()

    def action_ctrl (self, element):
        actions = ActionChains(self.driver) 
        actions.key_down(Keys.CONTROL) 
        actions.click(element)   
        actions.key_up(Keys.CONTROL)    
        actions.perform()

    def action_arrow_right (self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        time.sleep(0.5)
        actions.perform()

    def action_arrow_down (self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        actions.perform()

    def double_click (self, element):
        a = ActionChains(self.driver)
        a.double_click(on_element=element)
        a.perform()

    def action_double_click (self):
        actions = ActionChains(self.driver)
        actions.double_click().perform()

    def action_click (self, locator):
        a = ActionChains(self.driver)
        element = self.find(locator)
        a.move_to_element(element)
        a.perform()
        a.click(on_element=element)
        a.perform()

    def upload_file (self, locator, pathToFile):
        element = self.driver.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(pathToFile)

    def action_send_keys (self, keys):
        actions = ActionChains(self.driver)
        actions.send_keys(keys + Keys.ENTER)
        actions.perform()

    def is_element_clickable(self, element):
        # element = self.find(locator)
        if element.is_enabled():
            return True
        else :
            return False

    def schrijfweg(self, wegteschrijven, eerstekeer):
        #Stap 1 check of de file momenteel bestaat
        #Stap 2 als de file al bestaat, gooi deze dan weg
        #Stap 3 maak een nieuwe file aan 
        current_data = []
        if eerstekeer:
            if not os.path.isdir("./workspace"):
                os.mkdir("./workspace")
            if not os.path.isfile("./workspace/passable_data.json"):
                with open("./workspace/passable_data.json", "w") as f:
                    json.dump([], f)
            else:
                logging.info("De oude data file wordt eerst weggegooid")
                os.remove("./workspace/passable_data.json")
                with open("./workspace/passable_data.json", "w") as f:
                    json.dump([], f)
        else:
            logging.info("Niet de eerste keer")
            with open("./workspace/passable_data.json", "r") as currentdata:
                current_data = json.load(currentdata)
            
        with open("./workspace/passable_data.json", "w") as outputfile:
            current_data.append(wegteschrijven)
            json.dump(current_data,outputfile)
        
    def leesuit(self, index):
        with open("./workspace/passable_data.json", "r") as jsonfile:
            self.gegevens = json.load(jsonfile)
            self.data = self.gegevens[index]

    def find_element_boolean (self, locator):
        try:
            elements = self.driver.find_elements(*locator)
            if len (elements) == 1:                
                return True
            elif len (elements) == 0:
                return False
            elif len (elements) > 1:
                print ('ERROR: Element meerdere malen op pagina gevonden. Returning False')
                return False
        except NoSuchElementException:
            return False

    def count_elements (self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def stale_intercepted (self, locator):        
        for i in range (100):            
            try:
                element = self.find(locator)
                element.click() 
                print ('Element gevonden en succesvol aangeklikt')
                break                
            except (ElementClickInterceptedException,StaleElementReferenceException):
                print ('Er heeft een ElementClickInterceptedException of StaleElementReferenceException plaatsgevonden, er wordt opnieuw gekeken of de knop klikbaar is')
                continue

    def stale_element (self, element):        
        for i in range (50):            
            try :
                # self.driver.wait(20).until(EC.staleness_of(element)) == False
                # self.driver.wait.until(EC.visibility_of_element_located(locator))
                if self.is_element_clickable(element) == True:
                    print ('Element gevonden en actief')
                    break      
                elif self.is_element_clickable(element) == False:
                    print ('Er wordt 2 seconden gewacht en opnieuw gekeken of element klikbaar is')
                    time.sleep(2)
                    continue          
            except (ElementClickInterceptedException,StaleElementReferenceException):
                #hier moet de pagina worden ververst
                print ('test')
                # time.sleep(2)
                # for _ in range (50):
                a = ActionChains(self.driver)
                a.send_keys(Keys.F5)
                a.perform()
                # self.driver.wait.until(EC.staleness_of(element))
                # self.driver.implicitly_wait(20).until(EC.staleness_of(element)) == False
                    # print (check)
                    # if check == True:
                    #     continue
                    # elif check != False:
                    #     break                
                print ('Er heeft een ElementClickInterceptedException of StaleElementReferenceException plaatsgevonden, er wordt opnieuw gekeken of de knop klikbaar is')
                continue
            