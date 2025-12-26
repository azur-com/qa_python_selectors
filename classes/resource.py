import time
from pathlib import Path

from selene import have, command, be
from selene.support.shared import browser


def script_dir(file_n):

    script_dir = Path(__file__).parent.joinpath(f'{file_n}').absolute()
    return script_dir


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

    def fill_phone(self, phone):
        browser.element("#userNumber").set_value(phone)
        pass

    def fill_email(self, email):
        browser.element("#userEmail").should(be.visible).type(email)

    def select_gender(self, s_gender):
        browser.all('[name=gender]').element_by(have.value(s_gender)).element('..').click()

    def upload_picture(self, picture_name):
        browser.element('#uploadPicture').set_value(script_dir(picture_name))

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
        return self

class ProfilePage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def should_profile_have_registered_user_data(self, reg_page: RegistrationPage ):

        reg_page.registered_user_data.should(have.exact_texts('Alex Gladov', 'alex123456@gmail.com', 'Female', '9999999787', '27 May,1999',
        '', 'Reading', 'a2.jpg', '161, Magic str.', 'NCR Noida'
            ))


