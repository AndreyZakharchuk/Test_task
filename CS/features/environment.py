from selene import config
from selene.browsers import BrowserName
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import os
import sys
from selene import browser

sys.path.append(os.path.dirname(__file__) + '/..')

from features.steps.scripts import script_click_view

webdriver.Chrome(ChromeDriverManager().install())


def before_scenario(context, scenario):
    config.browser_name = BrowserName.CHROME


def before_step(context, step):
    script_click_view(context)


def after_scenario(context, scenario):
    browser.driver().delete_all_cookies()
    browser.driver().execute_script('window.localStorage.clear();')
    browser.driver().quit()
