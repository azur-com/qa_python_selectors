import time

from classes.resource import RegistrationPage, ProfilePage



# END CLASS RegistrationPage

def student_registrtion_form():
    reg_page = RegistrationPage()
    reg_page.open()
    reg_page.fill_name("Alex", "Gladov")
    reg_page.fill_email('alex123456@gmail.com')
    reg_page.fill_phone("99999997878")
    reg_page.fill_birthday("May", "1999", 27)
    reg_page.select_gender('Female')

    #print(xl)

    reg_page.fill_birthday("May", "1999", 27)
    reg_page.select_state_and_city('NCR', 'Noida')

    #print(resource.script_dir('a2.jpg'))
    reg_page.upload_picture('a2.jpg')
    reg_page.select_hobies('Reading')
    reg_page.fill_address("161, Magic str.")

    # press_enter()

    time.sleep(3)
    reg_page.submit()



    profile_page = ProfilePage()
    profile_page.should_profile_have_registered_user_data(reg_page)
    time.sleep(3)

    '''
    browser.element("li[data-value=Science]").click()
    browser.element("li[data-value=Sports]").click()
    ActionChains(browser.driver).send_keys(Keys.TAB).perform()

    browser.element('button[type=submit]').perform(command.js.scroll_into_view)

    browser.element("input[data-testid=stateCity]").element('..').click()
    browser.all(".MuiMenuItem-root:not(.MuiDisabled)").element_by(have.attribute('data-value').value('Idaho')).click()
    # browser.element("select[data-testid=stateCity]").element('..').click()
    # time.sleep(1)
    # rowser.all("select[data-testid=stateCity]>option").element_by(have.value('Nampa')).click()
    # time.sleep(2)
    browser.element("select[data-testid=stateCity]").type('Boise')
    time.sleep(2)
    ActionChains(browser.driver).send_keys(Keys.TAB).perform()
    browser.element('textarea[data-testid="address"]'
                    ).type("str.Grenoble 161/1\nChisinau, Moldova")
    # browser.element('//label[text()="Slider"]/..//*[@type="range"]')
    time.sleep(2)
    ActionChains(browser.driver).send_keys(Keys.END).perform()
    time.sleep(2)
    browser.element('input[type=range]').press_enter()
    for _ in range(10):
        ActionChains(browser.driver).send_keys(Keys.RIGHT).perform()
    # xl.element_by (have.value()"option[value='Nampa']").click().press_enter()
    time.sleep(6)

    browser.element('button[type=submit]').perform(command.js.scroll_into_view
                                                   ).click()  # press_enter()
    '''
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


student_registrtion_form()
