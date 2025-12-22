from selene import have, by, be, query
from pathlib import Path
from selene import command
import os
from selene.support.shared import browser
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.devtools.v140.debugger import pause


def test_1_todo():
    browser.open('https://app.qa.guru/automation-practice-form')
    browser.element("[data-testid=ClearIcon]").click()
    browser.element("input[data-testid=firstName]").set_value("Alex")
    browser.element("input[data-testid=lastName]").set_value("Gladov")
    browser.element("input[data-testid=email]").should(be.visible).type('alex123456@gmail.com')
    browser.element("input[data-testid=phone]").type("99999997878")

    browser.element("input[data-testid=language]").element('..').click()
    browser.element("li[data-value=Russian]").click()
    browser.element('input[type="radio"][value="Female"]').click()
    browser.all('[data-testid=hobbies]').element_by(have.value('Reading')).click()
    browser.all('[data-testid=hobbies]').element_by(have.value('Music')).click()
    browser.element("[data-testid=dateOfBirth]").click().type("12122000")
    #browser.element(["button[type=submit]").perform(command.js.scroll_into_view)

    browser.element(".MuiSelect-multiple").element('..').click()
    browser.element("li[data-value=Science]").click()
    browser.element("li[data-value=Sports]").click()
    ActionChains(browser.driver).send_keys(Keys.TAB).perform()

    browser.element('button[type=submit]').perform(command.js.scroll_into_view)

    browser.element("input[data-testid=stateCity]").element('..').click()
    browser.all(".MuiMenuItem-root:not(.MuiDisabled)").element_by(have.attribute('data-value').value('Idaho')).click()
    #browser.element("select[data-testid=stateCity]").element('..').click()
    #time.sleep(1)
    #rowser.all("select[data-testid=stateCity]>option").element_by(have.value('Nampa')).click()
    #time.sleep(2)
    browser.element("select[data-testid=stateCity]").type('Boise')
    time.sleep(2)
    ActionChains(browser.driver).send_keys(Keys.TAB).perform()
    browser.element('textarea[data-testid="address"]'
                    ).type("str.Grenoble 161/1\nChisinau, Moldova")
    #browser.element('//label[text()="Slider"]/..//*[@type="range"]')
    time.sleep(2)
    ActionChains(browser.driver).send_keys(Keys.END).perform()
    time.sleep(2)
    browser.element('input[type=range]').press_enter()
    for _ in range(10):
         ActionChains(browser.driver).send_keys(Keys.RIGHT).perform()
    #xl.element_by (have.value()"option[value='Nampa']").click().press_enter()
    time.sleep(6)


    browser.element('button[type=submit]').perform(command.js.scroll_into_view
                ).click() #press_enter()

    '''
    
    xl = browser.element('input')
    xl.click()
    elements = browser.all('label')
    for e in elements:
        print(e.get(query.text))
    #print(xl.get_attribute('value'))


    .element_by(have.value('Female')).
    browser.element('#hobbies-checkbox-2').with_(clickable=True)
    xl = browser.element('.custom-control-label').click()
    browser.element('[name=gender][value=Female]+label').click()
    browser.element("#gender-radio-2").type('a').press_enter()
    browser.element("#p").type('b').press_enter()
    browser.element("#p").type('c').press_enter()
    '''
    pass


test_1_todo()




