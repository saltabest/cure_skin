from selenium import webdriver


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait

from features.app.application import Application
from selenium.webdriver.chrome.options import Options




def browser_init(context):


    service = Service(executable_path='C:/Users/Eugene/project/cure_skin/chromedriver.exe')
    # context.driver = webdriver.Chrome(service=service)
    #context.driver = webdriver.Firefox(executable_path= r'C:\Users\Eugene\project\cure_skin\geckodriver-v0.33.0-win64')
    # context.driver = webdriver.Safari()

    context.driver.maximize_window()
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


    #### HEADLESS MODE ####
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    Options = webdriver.ChromeOptions()
    Options.add_argument('--headless')
    context.driver = webdriver.Chrome(
        chrome_options=Options,
        service=service
    )
    ###FIRE HEADL###
    #firefox_options = webdriver.FirefoxOptions()
    #firefox_options.add_argument('--headless')
    #firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    #context.driver = webdriver.Firefox(executable_path=r'C:\Users\Eugene\project\cure_skin\geckodriver-v0.33.0-win64', options=firefox_options)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
