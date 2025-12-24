from selene import have, be
from selene import command
from selene.support.shared import browser
import time

from test import resource


class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        time.sleep(3)
        browser.all('[id^=google_ads]').with_(timeout=8).wait_until(have.size_greater_than(3))
        browser.all('[id^=google_ads]').perform(command.js.remove)
        browser.all('.Google-Ad').perform(command.js.remove)

    def fill_name(self, val1: str, val2: str):
        browser.element('#firstName').type(val1)
        browser.element("#lastName").type(val2)
        pass

    def fill_birthday(self, month, year, day):
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view)
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type("May")
        browser.element(".react-datepicker__year-select").type("1999")
        # browser.all("//*[contains(@class, 'react-datepicker__day') and not(contains(@class, 'react-datepicker__day--outside-month'))]").element_by(have.exact_text('27')).click() #get(query.text)
        browser.all(".react-datepicker__day:not(.react-datepicker__day--outside-month)").element_by(
            have.exact_text('27')).click()  # get(query.text)

    @property
    def registered_user_data(self):
        return browser.element('.table').all('td').even

    def should_registered_user_data(self, param0, param1, param2, param3, param4, param5, param6, param7, param8,
                                    param9):
        self.registered_user_data.should(have.exact_texts(
            param0, param1, param2, param3, param4, param5, param6, param7,
            param8, param9
        ))

    def fill_phone(self, phone):
        browser.element("#userNumber").set_value(phone)
        pass

    def fill_email(self, email):
        browser.element("#userEmail").should(be.visible).type(email)

    def select_gender(self, s_gender):
        browser.all('[name=gender]').element_by(have.value(s_gender)).element('..').click()

    def upload_picture(self, picture_name):
        browser.element('#uploadPicture').set_value(resource.script_dir(picture_name))

    def select_state_and_city(self, state, city):
        time.sleep(1)
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()

    def select_hobies(self, hobbies):
        browser.all(".custom-checkbox").element_by(have.exact_text(hobbies)).click()

    def fill_address(self, address):
        browser.element("#currentAddress").type(address)

    def submit(self):
        browser.element("button[id=submit]").perform(command.js.scroll_into_view)
        browser.element("button[id=submit]").perform(command.js.click)


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

    time.sleep(3)

    reg_page.should_registered_user_data('Alex Gladov', 'alex123456@gmail.com', 'Female', '9999999787', '27 May,1999',
                                         '', 'Reading', 'a2.jpg', '161, Magic str.', 'NCR Noida')
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
